# Réseaux de neurones convolutifs (CNN)

Les CNN sont une famille de réseaux de neurones conçus pour traiter des données organisées en **grille** — images (2D), vidéos (3D), signaux audio (1D). Ils sont la brique de base de quasiment toutes les tâches de vision par ordinateur.

## Pourquoi pas un réseau classique ?

Un réseau de neurones classique (ANN) connecte chaque neurone à tous ceux de la couche suivante. Sur une image 256×256 en RGB, ça donne **196 608 entrées** — et chaque connexion a un poids à apprendre. C'est massif, lent, et surtout inutile : un pixel n'a de sens que dans le contexte de ses voisins immédiats.

Un CNN résout ce problème avec deux idées simples :

- **Localité** — un filtre ne regarde qu'une petite zone à la fois (ex. 3×3 pixels)
- **Partage de poids** — le même filtre est appliqué partout sur l'image

## La convolution

Un filtre (ou *kernel*) est une petite matrice de poids. On le fait glisser sur l'image : à chaque position, on multiplie les valeurs du filtre par les pixels sous-jacents et on additionne. Le résultat est un pixel dans la **carte d'activation** (*feature map*).

```
Image 5×5          Filtre 3×3        Feature map 3×3
┌─────────────┐    ┌───┬───┬───┐     ┌─────────────┐
│ 1  2  3  0  │    │ 1 │ 0 │-1 │     │    ...      │
│ 4  5  6  1  │  × │ 1 │ 0 │-1 │  =  │    ...      │
│ 7  8  9  2  │    │ 1 │ 0 │-1 │     │    ...      │
│ 0  1  2  3  │    └───┴───┴───┘     └─────────────┘
└─────────────┘
```

Ce filtre détecte les **bords verticaux**. D'autres filtres détectent des bords horizontaux, des coins, des textures — le réseau les apprend automatiquement pendant l'entraînement.

## Architecture typique

Un CNN est une succession de blocs, chacun réduisant la résolution spatiale tout en augmentant le nombre de filtres :

```
Image                Conv + ReLU         Pooling          ...       Sortie
(256×256×3)    →    (256×256×32)    →   (128×128×32)    →  ...  →  classes
```

**Couche de convolution** — applique N filtres en parallèle → produit N feature maps.

**ReLU** — `max(0, x)` sur chaque pixel. Supprime les valeurs négatives, introduit la non-linéarité.

**Pooling** — réduit la résolution (ex. garder le max dans chaque fenêtre 2×2). Le réseau devient insensible aux petits décalages de position.

**Couche fully connected** — à la fin, les feature maps sont aplaties et connectées à la sortie (classification).

## Ce que le CNN apprend couche par couche

| Couche | Ce qu'elle détecte |
|---|---|
| 1 | Bords, gradients de couleur |
| 2 | Textures, motifs simples |
| 3 | Formes géométriques |
| Profondes | Objets complexes (couronne d'arbre, fenêtre, toit…) |

Les premières couches sont génériques (détection de bords), les couches profondes sont spécifiques au domaine. C'est pourquoi on peut **réutiliser** un CNN pré-entraîné sur une grande base d'images et l'adapter à une tâche spécifique (*transfer learning*).

## CNN pour la segmentation

Un CNN classique produit **un vecteur de sortie** (une classe par image). Pour la segmentation, on a besoin d'**un label par pixel** — une sortie de la même taille que l'entrée. C'est le problème que résout l'architecture **U-Net**, qui ajoute un décodeur symétrique au CNN encodeur.
