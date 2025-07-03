"""
===========================================================
Grids avec Seaborn
===========================================================

Les "grids" permettent de créer des visualisations multi-graphes
en fonction de variables catégorielles. 

Dans ce script, nous explorons :
- catplot()   : plots catégoriels avec rows/cols
- PairGrid()  : personnalisation avancée des scatterplots et KDE
- FacetGrid() : visualisation de distributions bivariées segmentées
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

df = pd.read_csv('./data/StudentsPerformance.csv')


# ===========================================================
# Catplot : diagrammes catégoriels multi-graphiques
# ===========================================================

# Boxplot simple
sns.catplot(
    x="gender",
    y="math score",
    data=df,
    kind="box"
)
plt.show()

# Boxplot par ligne (row)
sns.catplot(
    x="gender",
    y="math score",
    data=df,
    kind="box",
    row="lunch"
)
plt.show()

# Boxplot par ligne et colonne (row & col)
sns.catplot(
    x="gender",
    y="math score",
    data=df,
    kind="box",
    row="lunch",
    col="test preparation course"
)
plt.show()


# ===========================================================
# PairGrid : personnalisation avancée de pairplot
# ===========================================================

# Grille basique
g = sns.PairGrid(df)
g.map_upper(sns.scatterplot)
g.map_diag(sns.kdeplot, lw=2)
g.map_lower(sns.kdeplot, color="red")
plt.show()

# Grille avec segmentation par hue
g = sns.PairGrid(df, hue="gender", palette="viridis", hue_kws={"marker": ["o", "+"]})
g.map_upper(sns.scatterplot, linewidths=1, edgecolor="w", s=40)
g.map_diag(sns.histplot)
g.map_lower(sns.kdeplot)
g.add_legend()
plt.show()


# ===========================================================
# FacetGrid : visualisation segmentée bivariée
# ===========================================================

# FacetGrid simple
sns.FacetGrid(data=df, col="gender", row="lunch")
plt.show()

# FacetGrid avec scatter
g = sns.FacetGrid(data=df, col="gender", row="lunch")
g.map(plt.scatter, "math score", "reading score", edgecolor="w")
g.add_legend()
plt.show()

# Ajustement des espacements horizontaux et verticaux
plt.subplots_adjust(hspace=0.4, wspace=1)
