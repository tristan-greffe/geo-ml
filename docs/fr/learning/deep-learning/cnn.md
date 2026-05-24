# Réseaux de neurones convolutifs (CNN)

## Pourquoi pas un réseau classique ?

Un réseau de neurones classique (fully connected) traite chaque pixel indépendamment. Une image 256×256 en RGB → 196 608 valeurs en entrée. Le réseau ne "voit" aucune relation spatiale : le pixel en haut à gauche et celui juste à côté sont traités comme s'ils n'avaient aucun lien.

Un **CNN** résout ce problème avec des **filtres convolutifs** — de petites fenêtres qui glissent sur l'image et détectent des motifs locaux (bords, textures, formes).

## La convolution en images

Un filtre est une petite matrice (ex. 3×3) qu'on fait glisser sur l'image. À chaque position, on multiplie les valeurs du filtre par les pixels sous-jacents et on additionne. Le résultat est un nouveau pixel dans la **carte d'activation** (feature map).

```
Image                Filtre 3×3           Feature map
┌─────────────┐      ┌───┬───┬───┐        ┌──────────┐
│ 10  20  30  │  ×   │ 1 │ 0 │-1 │   =    │   ...    │
│ 40  50  60  │      │ 1 │ 0 │-1 │        │   ...    │
│ 70  80  90  │      │ 1 │ 0 │-1 │        └──────────┘
└─────────────┘      └───┴───┴───┘
```

Ce filtre détecte les bords verticaux. D'autres filtres détectent des bords horizontaux, des coins, des textures, etc.

## Ce que le CNN apprend

Un CNN est organisé en **couches successives** :

| Couche | Ce qu'elle détecte |
|---|---|
| Couche 1 | Bords, contrastes locaux |
| Couche 2 | Textures, motifs simples |
| Couche 3 | Formes (cercles, arcs) |
| Couches profondes | Objets complexes (couronne d'arbre, toit) |

Les filtres ne sont **pas programmés à la main** — le réseau les apprend automatiquement à partir des exemples d'entraînement.

## Opérations clés

**Pooling** — réduit la taille de la feature map (ex. garder le max dans une fenêtre 2×2). Le réseau devient insensible aux petits décalages de position.

**ReLU** — fonction d'activation `max(0, x)`. Elle introduit de la non-linéarité : sans elle, empiler des couches ne servirait à rien (une somme de fonctions linéaires reste linéaire).

**Padding** — ajoute des pixels nuls autour de l'image pour que la feature map garde la même taille après convolution.

## Analogie web

Pense à un CNN comme à une pipeline de transformations CSS/SVG : chaque couche applique un filtre (blur, sharpen, edge-detect) sur l'image précédente. La différence : les filtres sont appris, pas codés.

## CNN → segmentation

Un CNN classique se termine par une couche fully connected qui produit **un seul vecteur de probabilités** (classification). Pour la segmentation, on a besoin d'une sortie de la même taille que l'entrée (un label par pixel). C'est le rôle de l'architecture **U-Net**.
