# Deep Learning

Le Deep Learning est une branche du Machine Learning basée sur des **réseaux de neurones artificiels** profonds.


:::tip Définition
Un réseau de neurones artificiel s’inspire (de manière simplifiée) du fonctionnement du cerveau : des neurones interconnectés reçoivent des signaux en entrée, appliquent une transformation mathématique (poids + biais + fonction d’activation), et transmettent le résultat aux neurones suivants.
:::

![neural-network](/learning/deep-learning/neural-network.png)

La différence entre un réseau classique et le Deep Learning réside dans la profondeur :
* Réseau peu profond (shallow) = entrée → 1 ou 2 couches cachées → sortie
* Réseau profond (deep learning) = entrée → dizaines voire centaines de couches → sortie

:::info
Plus le réseau est profond, plus il peut apprendre des représentations hiérarchiques complexes (caractéristiques simples → motifs intermédiaires → concepts abstraits).
:::

## Principaux types de réseaux

| Réseau | Nom complet | Idée clé | Usage typique |
|---|---|---|---|
| **ANN** | Artificial Neural Network | Neurones entièrement connectés - chaque neurone reçoit tous les signaux de la couche précédente | Données tabulaires, classification générale |
| **CNN** | Convolutional Neural Network | Filtres qui glissent sur l'image pour détecter des motifs locaux (bords, textures, formes) | Images, vidéos, données spatiales |
| **RNN** | Recurrent Neural Network | Boucle de mémoire interne - la sortie d'un pas de temps est réinjectée en entrée du suivant | Séries temporelles, texte, audio |
| **LSTM** | Long Short-Term Memory | Variante de RNN avec une mémoire longue durée (évite l'oubli des informations anciennes) | Traduction, prévision météo, speech |
| **Transformer** | — | Mécanisme d'attention - chaque élément regarde tous les autres pour se contextualiser | LLMs (GPT, Claude), vision (ViT) |
| **GAN** | Generative Adversarial Network | Deux réseaux en compétition : un générateur crée des données, un discriminateur les évalue | Génération d'images, augmentation de données |

:::tip Dans GeoML
On utilise un **CNN** comme bloc de base, intégré dans une architecture **U-Net** pour la segmentation sémantique. Les Transformers (ViT, SegFormer) sont une alternative plus récente mais plus gourmande en données.
:::