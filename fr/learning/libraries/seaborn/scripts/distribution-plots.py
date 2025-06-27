"""
===========================================================
Diagrammes de distribution avec Seaborn
===========================================================

Il existe plusieurs façons de visualiser la distribution d'une variable
(numérique) en Data Science.

Dans ce script, nous explorons principalement :
- rugplot : affichage brut des observations
- histplot / displot : histogrammes
- kdeplot : estimation de densité (KDE)

Ces outils permettent de mieux comprendre :
- la forme de la distribution
- la dispersion des valeurs
- la concentration autour de la moyenne
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
# Source : http://roycekimmons.com/tools/generated_data
# ===========================================================

df = pd.read_csv("./data/dm_office_sales.csv")

print(df.head())
print("\n")
df.info()


# ===========================================================
# Rugplot simple
# ===========================================================
# Le rugplot affiche chaque observation sous forme de "tick" sur l'axe.

sns.rugplot(
    x="salary",
    data=df,
    height=0.5
)

plt.show()


# ===========================================================
# Histogrammes : displot() et histplot()
# ===========================================================
"""
Le rugplot devient vite illisible pour de grands ensembles de données.
Une alternative consiste à regrouper les valeurs en intervalles (bins)
et à construire un histogramme.

Le displot() est une interface de haut niveau qui peut inclure :
- histogramme
- KDE (Kernel Density Estimation)
"""

sns.displot(
    data=df,
    x="salary",
    kde=True
)

plt.show()


# ===========================================================
# Focus sur les histogrammes
# ===========================================================

sns.displot(
    data=df,
    x="salary"
)
plt.show()

sns.histplot(
    data=df,
    x="salary"
)
plt.show()


# ===========================================================
# Nombre de bandes (bins)
# ===========================================================

sns.histplot(
    data=df,
    x="salary",
    bins=10
)
plt.show()

sns.histplot(
    data=df,
    x="salary",
    bins=100
)
plt.show()


# ===========================================================
# Styles et thèmes Seaborn
# ===========================================================
# Styles disponibles :
# darkgrid, whitegrid, dark, white, ticks

sns.set_theme(style="darkgrid")
sns.histplot(
    data=df,
    x="salary",
    bins=100
)
plt.show()

sns.set_theme(style="white")
sns.histplot(
    data=df,
    x="salary",
    bins=100
)
plt.show()


# ===========================================================
# Arguments Matplotlib dans Seaborn
# ===========================================================
# Seaborn accepte de nombreux paramètres de style de Matplotlib.

sns.displot(
    data=df,
    x="salary",
    bins=20,
    kde=False,
    color="red",
    edgecolor="black",
    lw=4,
    ls="--"
)

plt.show()


# ===========================================================
# KDE : Kernel Density Estimation
# ===========================================================
"""
Le KDE est une estimation continue de la fonction de densité
de probabilité d'une variable aléatoire.

Il s'agit d'une méthode de lissage basée sur la somme de noyaux
(généralement gaussiens).
"""

np.random.seed(42)

sample_ages = np.random.randint(0, 100, 200)
sample_ages = pd.DataFrame(sample_ages, columns=["age"])


# Rugplot des données simulées
sns.rugplot(
    data=sample_ages,
    x="age"
)
plt.show()


# Histogramme avec rug
plt.figure(figsize=(12, 8))
sns.displot(
    data=sample_ages,
    x="age",
    bins=10,
    rug=True
)
plt.show()


# Histogramme + KDE
plt.figure(figsize=(12, 8))
sns.displot(
    data=sample_ages,
    x="age",
    bins=10,
    rug=True,
    kde=True
)
plt.show()


# KDE simple
sns.kdeplot(
    data=sample_ages,
    x="age"
)
plt.show()


# ===========================================================
# Limitation du KDE (clip)
# ===========================================================
# Utile lorsque les valeurs ont des bornes naturelles.

sns.kdeplot(
    data=sample_ages,
    x="age",
    clip=[0, 100]
)
plt.show()


# ===========================================================
# Bande passante (bandwidth)
# ===========================================================
# Une bande passante plus faible rend le KDE plus sensible.

sns.kdeplot(data=sample_ages, x="age", bw_adjust=0.1)
sns.kdeplot(data=sample_ages, x="age", bw_adjust=0.5)
sns.kdeplot(data=sample_ages, x="age", bw_adjust=1)
plt.show()


# ===========================================================
# Style du KDE
# ===========================================================

sns.kdeplot(
    data=sample_ages,
    x="age",
    bw_adjust=0.5,
    fill=True,
    color="red"
)
plt.show()


# ===========================================================
# KDE bi-dimensionnel (aperçu)
# ===========================================================
# Comparaison de deux variables continues

random_data = pd.DataFrame(
    np.random.normal(0, 1, size=(100, 2)),
    columns=["x", "y"]
)

sns.kdeplot(
    data=random_data,
    x="x",
    y="y"
)
plt.show()
