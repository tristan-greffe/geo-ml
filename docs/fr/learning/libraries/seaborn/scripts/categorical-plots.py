"""
===========================================================
Diagrammes catégoriels — Estimation statistique par catégorie
===========================================================

Les données catégorielles correspondent à des groupes distincts
(exemples : pays, entreprises, niveaux d'éducation).

Contrairement aux variables continues (âge, prix, salaire),
il n'existe pas de valeurs intermédiaires entre deux catégories.

Les diagrammes catégoriels permettent de :
- compter le nombre d'observations par catégorie
- estimer des statistiques (moyenne, écart-type, etc.)
- comparer visuellement des groupes

Dans ce script, nous explorons principalement :
- countplot() : comptage par catégorie
- barplot()   : estimation statistique par catégorie
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

df = pd.read_csv("./data/dm_office_sales.csv")


# ===========================================================
# Countplot : diagramme de comptage
# ===========================================================
# Affiche le nombre total d'observations par catégorie.

plt.figure(figsize=(10, 4), dpi=200)
sns.countplot(
    x="division",
    data=df
)
plt.show()

plt.figure(figsize=(10, 4), dpi=200)
sns.countplot(
    x="level of education",
    data=df
)
plt.show()


# ===========================================================
# Countplot avec séparation par catégorie (hue)
# ===========================================================
# Permet de comparer la distribution au sein d'une autre variable.

plt.figure(figsize=(10, 4), dpi=200)
sns.countplot(
    x="level of education",
    data=df,
    hue="training level"
)
plt.show()

plt.figure(figsize=(10, 4), dpi=200)
sns.countplot(
    x="level of education",
    data=df,
    hue="training level",
    palette="Set1"
)
plt.show()

plt.figure(figsize=(10, 4), dpi=200)
# La palette "Paired" est adaptée lorsque les catégories vont par paires
sns.countplot(
    x="level of education",
    data=df,
    hue="training level",
    palette="Paired"
)
plt.show()


# ===========================================================
# Barplot : estimation statistique par catégorie
# ===========================================================
"""
Contrairement au countplot, le barplot permet d'afficher une statistique
continue sur l'axe Y (par défaut : la moyenne).

⚠️ Attention :
Ces graphiques peuvent suggérer une continuité entre catégories,
ce qui n'est pas toujours pertinent.
"""

plt.figure(figsize=(10, 6), dpi=200)
# Par défaut, barplot() affiche la moyenne
# Les barres noires représentent l'intervalle de confiance (ci)
sns.barplot(
    x="level of education",
    y="salary",
    data=df,
    estimator=np.mean,
    ci="sd"
)
plt.show()


# ===========================================================
# Barplot avec séparation par catégorie (hue)
# ===========================================================

plt.figure(figsize=(12, 6))
sns.barplot(
    x="level of education",
    y="salary",
    data=df,
    estimator=np.mean,
    ci="sd",
    hue="division"
)
plt.show()


# ===========================================================
# Légende à l'extérieur du graphique
# ===========================================================

plt.figure(figsize=(12, 6), dpi=100)
sns.barplot(
    x="level of education",
    y="salary",
    data=df,
    estimator=np.mean,
    ci="sd",
    hue="division"
)

plt.legend(
    bbox_to_anchor=(1.05, 1),
    loc="upper left"
)

plt.show()
