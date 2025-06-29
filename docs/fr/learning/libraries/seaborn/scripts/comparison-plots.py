"""
===========================================================
Diagrammes de comparaison avec pairplot() et jointplot()
===========================================================

Les diagrammes de comparaison permettent de visualiser les relations
entre plusieurs variables continues.

Dans ce script, nous explorons :
- jointplot() : visualisation bivariée avec histogrammes ou KDE
- pairplot()  : visualisation multivariée, incluant toutes les paires
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
# Jointplot : relations entre deux variables
# ===========================================================

# Diagramme de base
sns.jointplot(
    x="math score",
    y="reading score",
    data=df
)
plt.show()

# Diagramme hexbin
sns.jointplot(
    x="math score",
    y="reading score",
    data=df,
    kind="hex"
)
plt.show()

# Diagramme KDE (estimation de densité)
sns.jointplot(
    x="math score",
    y="reading score",
    data=df,
    kind="kde"
)
plt.show()


# ===========================================================
# Pairplot : relations entre toutes les variables continues
# ===========================================================

# Diagramme de base
sns.pairplot(df)
plt.show()

# Avec segmentation par "gender" et palette de couleurs
sns.pairplot(
    df,
    hue="gender",
    palette="viridis"
)
plt.show()

# Affichage uniquement du triangle inférieur (corner)
sns.pairplot(
    df,
    hue="gender",
    palette="viridis",
    corner=True
)
plt.show()

# Utilisation d'un histogramme sur la diagonale
sns.pairplot(
    df,
    hue="gender",
    palette="viridis",
    diag_kind="hist"
)
plt.show()
