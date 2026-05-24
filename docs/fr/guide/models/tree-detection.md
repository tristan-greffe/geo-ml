# Détection d'arbres

## Vue d'ensemble

Le modèle de détection d'arbres prend en entrée une **orthophoto RGB** (tuile IGN 20 cm/px) et produit un **masque de segmentation** pixel à pixel. Ce masque est ensuite converti en polygones GeoJSON affichés sur la carte.

```
Tuile IGN (RGB)  →  U-Net  →  Masque binaire  →  Polygones GeoJSON
```

## Pipeline en trois étapes

### 1. Exploration du dataset (`explore_dataset.py`)

Avant d'entraîner quoi que ce soit, on visualise les données brutes pour comprendre ce que le modèle va recevoir en entrée et ce qu'il devra apprendre à produire.

```bash
conda activate geoml
python model/src/explore_dataset.py
```

Le script télécharge une mosaïque 3×3 de tuiles IGN sur la **Forêt de Fontainebleau** (zone riche en feuillage, idéale pour tester) et affiche trois panneaux :

**Panneau 1 — Orthophoto RGB**
L'image brute IGN. C'est l'entrée exacte que recevra U-Net. Chaque pixel a trois valeurs : Rouge, Vert, Bleu (0–255).

**Panneau 2 — Heatmap EGI**
L'Excess Green Index : `EGI = 2×Vert - Rouge - Bleu`. La végétation reflète beaucoup de vert → valeur EGI élevée → pixel jaune/vif sur la heatmap. Le béton, l'asphalte et les toits ont une valeur EGI faible → pixel sombre.

**Panneau 3 — Masque binaire**
On applique un seuil automatique (méthode Otsu) sur la heatmap EGI : pixels au-dessus du seuil = arbre (`1`), en dessous = fond (`0`). Ce masque est la **vérité terrain approximative** utilisée pour entraîner U-Net.

::: info Pourquoi "approximative" ?
L'EGI confond parfois gazon et arbre, rate les arbres en zone ombragée. C'est un **label faible** — suffisant pour démarrer l'entraînement, mais à améliorer ensuite avec des annotations manuelles ou un dataset externe.
:::

### 2. Préparation des patches

U-Net travaille sur des **patches carrés de 256×256 px**. L'orthophoto complète est découpée en grille de patches avec chevauchement pour éviter les effets de bord.

Chaque patch donne une paire :
- `image.npy` — tableau 256×256×3 (RGB normalisé 0–1)
- `mask.npy` — tableau 256×256×1 (binaire 0/1)

### 3. Entraînement U-Net

Le modèle apprend à reproduire le masque à partir de l'image RGB. Après entraînement, il généralise : il reconnaît les couronnes d'arbres par leur **texture et leur forme**, pas seulement par leur couleur verte.

## Structure des fichiers

```
model/
├── src/
│   ├── explore_dataset.py   # Étape 1 — visualiser données brutes
│   ├── dataset.py           # Étape 2 — Dataset PyTorch (patches)
│   ├── model.py             # Définition U-Net
│   └── train.py             # Boucle d'entraînement
├── data/
│   └── ign-sample/          # Tuiles IGN téléchargées + preview
├── weights/                 # Poids entraînés (.pth) — ignoré par git
└── environment.yml          # Dépendances conda
```

## Lien avec la méthode classique (EGI)

L'application utilise déjà une détection par EGI (`tree-detection/backend/detection/detect.py`). Le U-Net ne remplace pas cet algorithme immédiatement — il apprend d'abord *à partir* de ses résultats (les masques EGI servent de labels d'entraînement).

Une fois le modèle entraîné et validé, il prendra la relève : même entrée (tuile RGB), même sortie (masque/polygones), mais une précision bien supérieure sur les cas difficiles.
