# Segmentation sémantique

## Les trois façons de "voir" une image

Face à une orthophoto aérienne, un modèle peut répondre à trois questions différentes :

| Approche | Question | Réponse | Résultat |
|---|---|---|---|
| **Classification** | "Y a-t-il un arbre dans cette image ?" | Oui / Non | Un label par image |
| **Détection** | "Où sont les arbres ?" | Boîtes englobantes | Des rectangles autour des objets |
| **Segmentation** | "Quels pixels sont des arbres ?" | Masque pixel à pixel | La forme exacte de chaque arbre |

### Pourquoi la segmentation pour GeoML ?

Pour la détection d'arbres sur une carte, on a besoin :
- De la **forme exacte** de la couronne (pas juste un rectangle)
- De la **surface** couverte en m²
- Des **contours** pour dessiner un polygone GeoJSON précis

La segmentation est la seule approche qui répond à ces besoins.

## Sémantique vs instance

Il existe deux types de segmentation :

**Segmentation sémantique** — chaque pixel reçoit une classe (`arbre` ou `fond`). Tous les arbres sont confondus dans la même couleur.

**Segmentation d'instance** — chaque pixel reçoit à la fois une classe *et* un identifiant d'objet. Chaque arbre individuel est colorié différemment.

```
Sémantique        Instance
🟢🟢⬛🟢🟢       🔴🔴⬛🔵🔵
🟢🟢⬛🟢🟢       🔴🔴⬛🔵🔵
⬛⬛⬛⬛⬛       ⬛⬛⬛⬛⬛
  (un masque)       (deux masques)
```

GeoML utilise la **segmentation sémantique** — plus simple à entraîner, suffisante pour extraire des polygones d'arbres.

## Le masque binaire

La sortie d'un modèle de segmentation est un **masque** : un tableau de la même taille que l'image d'entrée, où chaque pixel vaut :
- `1` → arbre
- `0` → fond (bâtiment, route, sol, eau…)

```
Image RGB (256×256×3)   →   Modèle U-Net   →   Masque (256×256×1)
```

Ce masque est ensuite converti en polygones GeoJSON pour être affiché sur la carte.

## Les trois panneaux du script d'exploration

Quand tu lances `explore_dataset.py`, tu vois trois panneaux. Voici ce qu'ils représentent et pourquoi ils sont importants :

### 1. Orthophoto RGB

L'image brute telle que l'IGN la fournit — trois canaux Rouge, Vert, Bleu. C'est l'**entrée du modèle** : les 256×256 pixels que U-Net va analyser.

### 2. Heatmap EGI (Excess Green Index)

$$\text{EGI} = 2 \times G - R - B$$

La végétation reflète beaucoup de lumière verte. L'EGI amplifie cette différence : les pixels d'arbres apparaissent en jaune/vert vif, le reste (routes, toits) est sombre.

C'est un **indice spectral classique** — pas de machine learning, juste de l'arithmétique sur les canaux. Il sert ici de **label faible** : une approximation automatique de la vérité terrain, sans annotation humaine.

### 3. Masque binaire (seuil Otsu)

On applique un seuil sur la heatmap EGI : les pixels au-dessus du seuil deviennent `1` (arbre), en dessous `0` (fond). Le seuil est calculé automatiquement par la méthode Otsu pour maximiser le contraste entre les deux classes.

C'est le **label d'entraînement** : ce que le modèle U-Net va apprendre à reproduire.

::: tip Pourquoi ne pas utiliser EGI directement ?
L'EGI est rapide mais fragile : il confond gazon, champs et forêts. U-Net apprendra à reconnaître les couronnes d'arbres par leur **texture et forme** — pas seulement par leur couleur verte.
:::
