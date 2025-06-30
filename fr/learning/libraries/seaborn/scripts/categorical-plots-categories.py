"""
===========================================================
Diagrammes catégoriels — Distribution au sein des catégories
===========================================================

Jusqu'à présent, nous avons utilisé des diagrammes catégoriels pour
comparer des statistiques (moyenne, comptage) entre différentes
catégories.

Dans ce script, nous allons plus loin en visualisant la distribution
complète d'une variable numérique à l'intérieur de chaque catégorie.

Nous explorerons notamment :
- boxplot
- violinplot
- swarmplot
- boxenplot (letter-value plot)
"""

# ===========================================================
# Imports
# ===========================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ===========================================================
# Chargement des données
# ===========================================================

df = pd.read_csv("./data/StudentsPerformance.csv")


# ===========================================================
# Boxplot
# ===========================================================
"""
Le boxplot (boîte à moustaches) représente la distribution d'une variable
à l'aide :
- des quartiles
- de la médiane
- de l'écart interquartile (IQR)
- des valeurs aberrantes (outliers)
"""

plt.figure(figsize=(12, 6))
sns.boxplot(
    x="parental level of education",
    y="math score",
    data=df
)
plt.show()


# ===========================================================
# Boxplot avec segmentation (hue)
# ===========================================================

plt.figure(figsize=(12, 6))
sns.boxplot(
    x="parental level of education",
    y="math score",
    data=df,
    hue="gender"
)

plt.legend(
    bbox_to_anchor=(1.05, 1),
    loc="upper left"
)
plt.show()


# ===========================================================
# Orientation du boxplot
# ===========================================================
# Il suffit d'inverser les axes X et Y.

plt.figure(figsize=(12, 6))
sns.boxplot(
    x="math score",
    y="parental level of education",
    data=df,
    orient="h"
)
plt.show()


# ===========================================================
# Largeur des boîtes
# ===========================================================

plt.figure(figsize=(12, 6))
sns.boxplot(
    x="parental level of education",
    y="math score",
    data=df,
    hue="gender",
    width=0.3
)
plt.show()


# ===========================================================
# Violinplot
# ===========================================================
"""
Le violinplot combine :
- un KDE (estimation de densité)
- une représentation symétrique de la distribution

Il est particulièrement utile pour comparer la forme des distributions
entre catégories.
"""

plt.figure(figsize=(12, 6))
sns.violinplot(
    x="parental level of education",
    y="math score",
    data=df
)
plt.show()

plt.figure(figsize=(12, 6))
sns.violinplot(
    x="parental level of education",
    y="math score",
    data=df,
    hue="gender"
)
plt.show()


# ===========================================================
# Violinplot — paramètre split
# ===========================================================
"""
Lorsque la variable utilisée pour 'hue' possède exactement deux niveaux,
le paramètre split=True permet de diviser le violon en deux moitiés.
"""

plt.figure(figsize=(12, 6))
sns.violinplot(
    x="parental level of education",
    y="math score",
    data=df,
    hue="gender",
    split=True
)
plt.show()


# ===========================================================
# Violinplot — paramètre inner
# ===========================================================
"""
Contrôle l'affichage interne du violon :
- None       : aucun élément interne
- 'box'      : mini boxplot
- 'quartile' : quartiles
- 'stick'    : chaque observation
"""

plt.figure(figsize=(12, 6))
sns.violinplot(
    x="parental level of education",
    y="math score",
    data=df,
    inner=None
)
plt.show()

plt.figure(figsize=(12, 6))
sns.violinplot(
    x="parental level of education",
    y="math score",
    data=df,
    inner="box"
)
plt.show()

plt.figure(figsize=(12, 6))
sns.violinplot(
    x="parental level of education",
    y="math score",
    data=df,
    inner="quartile"
)
plt.show()

plt.figure(figsize=(12, 6))
sns.violinplot(
    x="parental level of education",
    y="math score",
    data=df,
    inner="stick"
)
plt.show()


# ===========================================================
# Orientation du violinplot
# ===========================================================

plt.figure(figsize=(12, 6))
sns.violinplot(
    x="math score",
    y="parental level of education",
    data=df
)
plt.show()


# ===========================================================
# Bande passante (bandwidth)
# ===========================================================
# Similaire au paramètre bw_adjust du KDE

plt.figure(figsize=(12, 6))
sns.violinplot(
    x="parental level of education",
    y="math score",
    data=df,
    bw=0.1
)
plt.show()


# ===========================================================
# Diagrammes avancés
# ===========================================================
"""
Les diagrammes avancés fournissent davantage de détails mais peuvent être
plus difficiles à interpréter pour un public non averti.
À utiliser avec précaution.
"""

# -----------------------------------------------------------
# Swarmplot
# -----------------------------------------------------------

sns.swarmplot(
    x="math score",
    data=df
)
plt.show()

sns.swarmplot(
    x="math score",
    data=df,
    size=2
)
plt.show()

sns.swarmplot(
    x="math score",
    y="race/ethnicity",
    data=df,
    size=3
)
plt.show()

sns.swarmplot(
    x="race/ethnicity",
    y="math score",
    data=df,
    size=3
)
plt.show()

plt.figure(figsize=(12, 6))
sns.swarmplot(
    x="race/ethnicity",
    y="math score",
    data=df,
    hue="gender"
)
plt.show()

plt.figure(figsize=(12, 6))
sns.swarmplot(
    x="race/ethnicity",
    y="math score",
    data=df,
    hue="gender",
    dodge=True
)
plt.show()


# -----------------------------------------------------------
# Boxenplot (Letter-Value Plot)
# -----------------------------------------------------------
"""
Le boxenplot est une extension du boxplot classique qui affiche
davantage de quantiles.

Il est particulièrement utile pour :
- les grands ensembles de données
- l'analyse des queues de distribution (tails)

Référence :
https://vita.had.co.nz/papers/letter-value-plot.html
"""

sns.boxenplot(
    x="math score",
    y="race/ethnicity",
    data=df
)
plt.show()

plt.figure(figsize=(12, 6))
sns.boxenplot(
    x="race/ethnicity",
    y="math score",
    data=df,
    hue="gender"
)
plt.show()
