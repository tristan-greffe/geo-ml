# Diagrammes catégoriels

Les **diagrammes catégoriels** permettent d’analyser des **statistiques associées à des catégories** et servent à afficher :
* une métrique statistique
* calculée par catégorie

:::warning Exemples
* nombre d’observations par catégorie
* moyenne par catégorie
* médiane, quartiles ou distribution par catégorie
:::

👉 On peut les voir comme l’équivalent visuel d’un `groupby` en Pandas.

## Diagrammes catégoriels basés sur une statistique unique

### Le Count Plot (diagramme de comptage)

Le count plot affiche simplement le nombre d’observations par catégorie

:::info Equivalent
C’est l’équivalent visuel de :
```py
df.groupby("categorie").count()
```
* Axe X : catégories
* Axe Y : nombre de lignes / instances
:::

:::warning Exemple : divisions d’entreprise
<img src="/learning/libraries/seaborn-count-plot.png" style="display: block; margin: 0 auto;width: 80%; height: auto;">

On voit immédiatement quelles catégories sont sur-représentées ou sous-représentées

➡️ Les comparaisons relatives sont faciles

📌 Limite importante :
* lorsque les différences sont très grandes, les catégories minoritaires deviennent difficiles à lire
* le graphique permet une comparaison relative, mais pas une lecture précise des valeurs

➡️ Pour des valeurs exactes, un tableau est souvent préférable.
:::

:::info Hue (sous-catégories)
Le count plot permet d’ajouter une deuxième dimension catégorielle (via la couleur).

Exemple: niveau d’éducation découpé par niveau de formation

<img src="/learning/libraries/seaborn-count-plot-hue.png" style="display: block; margin: 0 auto;width: 80%; height: auto;">
Cela permet de visualiser une hiérarchie de catégories.
:::

### Le Bar Plot (diagramme en barres)

Le bar plot est une forme plus générale que le count plot. Il permet d’afficher n’importe quelle statistique par catégorie :

* moyenne
* médiane
* écart-type
* quartiles
* etc.

L’argument clé est l’estimateur statistique.

:::warning Exemple : moyenne et écart-type
* La hauteur de la barre représente la moyenne
* Les barres d’erreur représentent souvent l’écart-type

<img src="/learning/libraries/seaborn-bar-plot-average.png" style="display: block; margin: 0 auto;width: 80%; height: auto;">

➡️ On peut ainsi comparer :

* les moyennes entre catégories
* la variabilité au sein de chaque catégorie
:::

:::warning ⚠️ Attention aux diagrammes en barres
Un diagramme en barres remplit visuellement l’axe Y depuis zéro jusqu’à la moyenne. Cela peut être trompeur, car :

* une moyenne n’est pas une quantité cumulative
* la continuité visuelle peut être mal interprétée

📌 Dans certains cas, un tableau est plus clair qu’un graphique.

| Level of education | mean | std |
| ----------- | --- | --- |
| associate's degree   | 93156.41 | 17066.06 |
| bachlor's degree | 94133.76 | 17007.09 |
| high school    | 83887.35 | 17674.44 |
| master's degree    | 93718.00 | 2497.63 |
| some college    | 88115.845 | 17076.28 |

👉 Règle clé : La visualisation doit simplifier la compréhension, pas la compliquer.
:::

## Les principaux diagrammes de distribution par catégorie

Jusqu’ici, nous avons vu : une statistique par catégorie. Mais que faire si nous voulons comparer toute la distribution d’une variable continue entre catégories ?

### Le Box Plot (diagramme en boîte)

Le `box plot` est le diagramme le plus courant pour comparer des distributions entre catégories.

<img src="/learning/libraries/seaborn-box-plot.png" style="display: block; margin: 0 auto;width: 80%; height: auto;">

👉 C’est le diagramme catégoriel le plus important à maîtriser.

#### Composants d’un box plot

* Un box plot repose sur les **quartiles** :
    * Q1 (25ᵉ percentile)
    * Q2 (50ᵉ percentile) → médiane
    * Q3 (75ᵉ percentile)
    <img src="/learning/libraries/seaborn-box-plot-mediane.png" style="display: block; margin: 0 auto;width: 80%; height: auto;">

* La boîte représente l’intervalle interquartile (EI ou IQR) = Q3 − Q1, soit les 50 % centraux des données

<img src="/learning/libraries/seaborn-box-plot-ei.png" style="display: block; margin: 0 auto;width: 80%; height: auto;">

* Les moustaches s’étendent généralement jusqu’à 1,5 × IQR

<img src="/learning/libraries/seaborn-box-plot-moustache.png" style="display: block; margin: 0 auto;width: 80%; height: auto;">

* Les points au-delà des moustaches sont considérés comme des outliers

<img src="/learning/libraries/seaborn-box-plot-outliers.png" style="display: block; margin: 0 auto;width: 80%; height: auto;">

:::info Le box plot permet de visualiser rapidement :
* médiane
* dispersion
* asymétrie
* valeurs aberrantes
:::

:::warning Box plot par catégorie
On peut afficher un box plot par catégorie :
* Axe X : catégories
* Axe Y : variable continue

<img src="/learning/libraries/seaborn-box-plot-categories.png" style="display: block; margin: 0 auto;width: 80%; height: auto;">
<img src="/learning/libraries/seaborn-box-plot-categories2.png" style="display: block; margin: 0 auto;width: 80%; height: auto;">
➡️ Cela permet une comparaison directe des distributions.

⚠️ Limite importante : le box plot ne montre pas le nombre d’observations par catégorie
:::

### Le Violin Plot (diagramme en violon)

Le violin plot combine :
* un KDE plot
* avec les statistiques du box plot

<img src="/learning/libraries/seaborn-violin-plot.png" style="display: block; margin: 0 auto;width: 80%; height: auto;">

👉 Il peut être vu comme : un KDE symétrique autour de l’axe central

:::info Construction intuitive
1. Calculer un KDE
2. Le refléter horizontalement
3. Assembler les deux côtés

➡️ La forme obtenue ressemble à un violon
:::

<img src="/learning/libraries/seaborn-violin-plot-reflect.png" style="display: block; margin: 0 auto;width: 80%; height: auto;">

:::warning
Un violin plot montre :
* la densité de probabilité
* la médiane
* l’intervalle interquartile

📌 Avantage : donne une meilleure idée de la forme réelle de la distribution

📌 Limite : ne montre pas explicitement le nombre de points
:::

<img src="/learning/libraries/seaborn-violin-plot-reflect-combine.png" style="display: block; margin: 0 auto;width: 80%; height: auto;">

<img src="/learning/libraries/seaborn-violin-plot-categories.png" style="display: block; margin: 0 auto;width: 80%; height: auto;">

### Le Swarm Plot (diagramme en essaim)

Le swarm plot affiche :
* tous les points de données
* répartis pour éviter les chevauchements

➡️ Chaque point correspond à une observation réelle.

<img src="/learning/libraries/seaborn-swarm-plot.png" style="display: block; margin: 0 auto;width: 80%; height: auto;">

:::info Avantages
* montre la distribution brute
* montre le nombre réel d’observations par catégorie
* rend visibles les outliers

📌 Très utile pour des jeux de données de taille modérée.

:::

:::warning Limite
peu adapté aux très grands jeux de données
:::

### Le Boxen Plot (Letter Value Plot)

Le boxen plot est une extension moderne du box plot (2011).
* utilise plusieurs quantiles
* donne une vision plus détaillée des distributions complexes
* conçu pour les grands jeux de données

<img src="/learning/libraries/seaborn-boxenplot-plot-categories.png" style="display: block; margin: 0 auto;width: 80%; height: auto;">

:::info Particularités
* remplace les quartiles par une hiérarchie de quantiles
* permet de mieux représenter les longues queues & les distributions asymétriques
:::

:::warning ⚠️ Usage recommandé avec prudence
* très peu connu du grand public
* rarement utilisé en contexte business
:::

## Choisir le bon diagramme catégoriel

| Objectif                   | Diagramme recommandé |
| -------------------------- | -------------------- |
| Compter des catégories     | Count plot           |
| Comparer une statistique   | Bar plot             |
| Comparer des distributions | Box plot             |
| Voir la forme complète     | Violin plot          |
| Voir les données brutes    | Swarm plot           |
| Données massives complexes | Boxen plot           |

## Fichier Python associé

:::details Diagrammes catégoriels basés sur une statistique unique
<<< ./scripts/categorical-plots.py
:::

:::details Diagrammes de distribution par catégorie
<<< ./scripts/categorical-plots-categories.py
:::