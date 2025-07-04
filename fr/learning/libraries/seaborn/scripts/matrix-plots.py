"""
===========================================================
Copyright MonCoachData (tous droits réservés)
Pour plus d'informations, visitez notre site moncoachdata.com

Diagrammes Matriciels - Matrix Plots
===========================================================

Dans ce script, nous explorons :
- heatmap : matrice de valeurs avec couleurs
- clustermap : heatmap hiérarchisée avec clustering
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
# Source : https://www.ined.fr/en/everything_about_population/data/all-countries/?lst_continent=900&lst_pays=926
# ===========================================================

"""
World Population Prospects publie des estimations de population pour tous les pays
du monde de 1950 à 2020, ainsi que des projections pour 2020-2100.
Les chiffres ici correspondent aux projections de la variante moyenne.
"""

df = pd.read_csv('./data/country_table.csv')


# ===========================================================
# Heatmap simple
# ===========================================================

# Définir les pays comme index
df = df.set_index('Countries')

# Heatmap de base
sns.heatmap(df)
plt.show()

# Sélectionner uniquement certaines colonnes (exclure "Life expectancy")
rates = df.drop('Life expectancy', axis=1)

# Heatmap simple
sns.heatmap(rates)
plt.show()

# Avec des lignes séparatrices
sns.heatmap(rates, linewidth=0.5)
plt.show()

# Ajouter les valeurs sur chaque cellule
sns.heatmap(rates, linewidth=0.5, annot=True)
plt.show()

# Ajouter une palette de couleurs
sns.heatmap(rates, linewidth=0.5, annot=True, cmap='viridis')
plt.show()

# Centrer la barre de couleurs sur une valeur spécifique
sns.heatmap(rates, linewidth=0.5, annot=True, cmap='viridis', center=40)
plt.show()

sns.heatmap(rates, linewidth=0.5, annot=True, cmap='viridis', center=1)
plt.show()


# ===========================================================
# Clustermap : heatmap hiérarchisée avec clustering
# ===========================================================

# Clustermap simple
sns.clustermap(rates)
plt.show()

# Ne pas clusterer les colonnes
sns.clustermap(rates, col_cluster=False)
plt.show()

# Ajuster la taille de la figure et la position de la barre de couleurs
sns.clustermap(
    rates,
    col_cluster=False,
    figsize=(12, 8),
    cbar_pos=(-0.1, 0.2, 0.03, 0.4)
)
plt.show()

# Supprimer le nom de l'index
rates.index.set_names('', inplace=True)

# Clustermap final avec personnalisation
sns.clustermap(
    rates,
    col_cluster=False,
    figsize=(12, 8),
    cbar_pos=(-0.1, 0.2, 0.03, 0.4)
)
plt.show()
