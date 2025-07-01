# Diagrammes de comparaison

Les **diagrammes de comparaison** permettent d’analyser les **relations entre plusieurs variables numériques**. Ils sont généralement des **extensions bidimensionnelles** des graphiques vus précédemment (histogrammes, scatter plots, KDE).

## Diagramme conjoint (Joint Plot)

Le joint plot combine :
* un diagramme de dispersion (relation entre deux variables)
* les distributions marginales de chaque variable

Il permet donc d’analyser simultanément :
* la relation entre deux variables
* la distribution individuelle de chacune

:::warning Structure d’un joint plot
Un joint plot est composé de :
* un graphique central (relation X–Y)
* un graphique de distribution pour X
* un graphique de distribution pour Y

Par défaut :
* relation : scatter plot
* distributions : histogrammes
:::

:::info Exemple : score en mathématiques (X) - score en lecture (Y)
On peut :
* observer la corrélation
* voir la concentration des valeurs
* détecter des asymétries ou des valeurs extrêmes

➡️ Le joint plot enrichit un scatter plot classique en ajoutant du contexte statistique.
<div style="display: flex; gap: 2rem;">
<div style="flex: 1">
Histogrammes avec des nuages de points
<img src="/learning/libraries/seaborn-joint-plot-histogram-scatter.png" style="display: block; margin: 0 auto;width: 90%; height: auto;">
</div>
<div style="flex: 1">
Histogrammes avec des hexagones
<img src="/learning/libraries/seaborn-joint-plot-histogram-hexagons.png" style="display: block; margin: 0 auto;width: 90%; height: auto;">
</div>
</div>

**Scatter vs Hexbin** - Lorsque les points se chevauchent fortement :
* les hexagones permettent de mieux visualiser la densité
* plus la couleur est foncée, plus il y a de points

📌 Utile pour les grands jeux de données.
:::

:::tip KDE unidimensionnel et bidimensionnel
Les distributions marginales peuvent être remplacées par des KDE plots. Et la relation centrale peut être un KDE bidimensionnel (densité conjointe)

<img src="/learning/libraries/seaborn-joint-plot-kde.png" style="display: block; margin: 0 auto;width: 60%; height: auto;">

⚠️ Ces graphiques sont fréquents en contexte scientifique, mais moins en contexte business.

👉 Toujours adapter le choix du graphique à son audience.
:::

## Diagramme de paires (Pair Plot)

Le pair plot est un outil fondamental pour l’analyse exploratoire de données (EDA). Il permet de :

* comparer toutes les colonnes numériques d’un DataFrame
* visualiser toutes les relations possibles entre variables

<img src="/learning/libraries/seaborn-pair-plot.png" style="display: block; margin: 0 auto;width: 60%; height: auto;">

:::info Fonctionnement
Pour un DataFrame contenant n variables numériques 
* la diagonale affiche les distributions de chaque variable (histogrammes ou KDE)
* les cases hors diagonale affichent des scatter plots pour chaque paire de variables

📌 Le pair plot ne fonctionne que sur des colonnes numériques.
:::

:::tip Lecture du graphique
* Chaque relation apparaît deux fois (symétrie)
* La diagonale permet de comprendre :
    * la distribution
    * l’asymétrie
    * les outliers
:::

:::warning Coloration par catégorie (Hue)
Il est possible d’ajouter une variable catégorielle :
* pour colorer les points
* pour comparer les relations entre sous-groupes

➡️ Très utile pour : classification, détection de séparabilité, compréhension des labels

**Exemple : comparaison des performances selon le genre**
<img src="/learning/libraries/seaborn-pair-plot-colory.png" style="display: block; margin: 0 auto;width: 60%; height: auto;">
:::

:::tip Optimisation et bonnes pratiques
⚠️ Le pair plot peut être très coûteux en mémoire & lent pour les grands DataFrames
:::

:::info Bonnes pratique
* filtrer les colonnes pertinentes
* créer un sous-ensemble du DataFrame
* éviter les DataFrames très larges
:::

## Quand utiliser ces diagrammes ?

| Objectif                   | Diagramme recommandé |
| -------------------------- | -------------------- |
| Relation entre 2 variables | Joint plot           |
| Relation + distributions   | Joint plot           |
| Vue globale des relations  | Pair plot            |
| Exploration ML / EDA       | Pair plot            |
| Données denses             | Joint plot (hexbin)  |
