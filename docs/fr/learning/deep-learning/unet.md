# U-Net

## Le problème de la segmentation avec un CNN classique

Un CNN classique réduit progressivement la taille de l'image (via pooling) pour extraire des informations de haut niveau. À la fin, on obtient une représentation compacte — utile pour classifier ("c'est un arbre") mais inutilisable pour segmenter (on a perdu la position spatiale).

Pour la segmentation, il faut **reconstruire** une image de la même taille que l'entrée. C'est le problème qu'U-Net résout.

## L'architecture en U

U-Net doit son nom à sa forme visuelle : une descente (encodeur) suivie d'une remontée symétrique (décodeur).

```
Image                                              Masque
256×256×3                                        256×256×1
    │                                                 ▲
    ▼                                                 │
┌────────┐                                       ┌────────┐
│  Conv  │ ──────── skip connection ──────────▶ │  Conv  │
│128×128 │                                       │128×128 │
└────┬───┘                                       └───▲────┘
     ▼                                               │
┌────────┐                                       ┌────────┐
│  Conv  │ ──────── skip connection ──────────▶ │  Conv  │
│  64×64 │                                       │  64×64 │
└────┬───┘                                       └───▲────┘
     ▼                                               │
┌────────┐                                       ┌────────┐
│  Conv  │ ──────── skip connection ──────────▶ │  Conv  │
│  32×32 │                                       │  32×32 │
└────┬───┘                                       └───▲────┘
     ▼                                               │
         ┌──────────────────────┐
         │   Bottleneck 16×16   │
         └──────────────────────┘
```

### L'encodeur (descente)

Identique à un CNN classique : des couches de convolution + pooling qui réduisent la résolution et augmentent le nombre de filtres. À chaque étape, le réseau voit des structures de plus en plus abstraites (bords → textures → formes → objets).

### Le décodeur (remontée)

L'opération inverse : des **convolutions transposées** (ou upsampling) qui remontent progressivement vers la résolution d'origine. À chaque étape, la résolution double et le nombre de filtres est divisé par deux.

### Les skip connections — la clé du U-Net

À chaque niveau, la feature map de l'encodeur est **concaténée** avec celle du décodeur correspondant. C'est ce qui différencie U-Net de toutes les architectures précédentes.

**Pourquoi c'est crucial :** l'encodeur compresse l'information (et perd la localisation précise). Les skip connections court-circuitent cette perte : le décodeur reçoit à la fois le contexte global (du bottleneck) et les détails fins (de l'encodeur).

Analogie : imagine que tu dois redessiner une carte de mémoire après l'avoir vue réduite à un timbre-poste. Les skip connections te permettent de consulter la carte originale à chaque zoom — tu gardes les détails tout en comprenant la structure globale.

## Pourquoi U-Net pour GeoML ?

Quatre raisons ont motivé ce choix :

| Critère | U-Net | Alternatives |
|---|---|---|
| **Petits datasets** | Fonctionne avec peu d'exemples | ResNet, VGG → nécessitent des millions d'images |
| **Contours précis** | Skip connections préservent les détails fins | YOLO → boîtes rectangulaires seulement |
| **Images haute résolution** | Conçu pour des patches (256×256) | Transformers vision → très gourmands en mémoire |
| **Origine** | Conçu pour la segmentation d'images médicales (petits objets, formes précises) — très similaire aux couronnes d'arbres vues du ciel | — |

## Les alternatives écartées

**Classification (ResNet, VGG…)** — répond à "y a-t-il un arbre ?", pas à "où exactement". Inutilisable pour extraire des polygones.

**Détection (YOLO, Faster R-CNN)** — prédit des boîtes englobantes rectangulaires. Pour des arbres ronds vus du dessus, la boîte encadre autant de toit ou de route que d'arbre.

**DeepLab / SegFormer** — architectures plus récentes, plus précises sur de grands datasets. Trop lourdes à entraîner depuis zéro sur notre volume de données.

**EGI seul (méthode classique)** — pas de machine learning. Rapide, mais confond gazon/champs/forêts et échoue sur les zones ombragées ou les espèces à feuillage sombre.

## Ce que U-Net apprend que EGI ne voit pas

| Situation | EGI | U-Net |
|---|---|---|
| Arbre en zone ombragée | ❌ Rate (pas assez vert) | ✅ Reconnaît la texture de couronne |
| Gazon / pelouse | ❌ Confond avec arbre | ✅ Distingue par la texture et la forme |
| Toit végétalisé | ❌ Confond | ✅ Apprend la différence de contexte |
| Arbre à feuillage sombre | ❌ Rate | ✅ Reconnaît la forme arrondie |
