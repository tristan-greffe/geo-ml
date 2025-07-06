"""
===========================================================
Analyse des biais de notation : Fandango vs autres plateformes
===========================================================

Objectif :
- Étudier la relation entre popularité et notation
- Comparer les notes affichées par Fandango aux notes réelles
- Comparer Fandango avec Rotten Tomatoes, Metacritic et IMDb
"""

# ===========================================================
# Imports
# ===========================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

# ===========================================================
# Chargement des données
# ===========================================================

all_sites = pd.read_csv('./data/all_sites_scores.csv')
fandango = pd.read_csv('./data/fandango_scrape.csv')


# ===========================================================
# Exploration initiale
# ===========================================================

fandango.info()
fandango.describe()


# ===========================================================
# Relation entre popularité et notation (votes vs rating)
# ===========================================================

plt.figure(figsize=(10, 4), dpi=150)
sns.scatterplot(data=fandango, x='RATING', y='VOTES')
plt.title("Relation entre la note réelle et le nombre de votes")
plt.show()


# ===========================================================
# Corrélations numériques
# ===========================================================

fandango.corr(numeric_only=True)


# ===========================================================
# Extraction de l'année depuis le titre du film
# ===========================================================

fandango['YEAR'] = fandango['FILM'].apply(lambda title: title.split('(')[-1].replace(')', ''))

# Nombre de films par année
fandango['YEAR'].value_counts()

plt.figure(figsize=(10, 4), dpi=150)
sns.countplot(data=fandango, x='YEAR')
plt.title("Nombre de films par année (Fandango)")
plt.show()


# ===========================================================
# Films les plus populaires
# ===========================================================

# Top 10 films avec le plus de votes
fandango.nlargest(10, 'VOTES')

# Films sans aucun vote
no_votes = fandango['VOTES'] == 0
no_votes.sum()

# DataFrame uniquement avec films évalués
fan_reviewed = fandango[fandango['VOTES'] > 0]


# ===========================================================
# Notes affichées (STARS) vs notes réelles (RATING)
# ===========================================================

plt.figure(figsize=(10, 4), dpi=150)
sns.kdeplot(data=fan_reviewed, x='RATING', clip=[0, 5], fill=True, label="Note réelle")
sns.kdeplot(data=fan_reviewed, x='STARS', clip=[0, 5], fill=True, label="Étoiles affichées")
plt.legend()
plt.title("Distribution : note réelle vs étoiles Fandango")
plt.show()


# ===========================================================
# Quantification de la différence STARS - RATING
# ===========================================================

fan_reviewed['STARS_DIFF'] = (fan_reviewed['STARS'] - fan_reviewed['RATING']).round(2)

plt.figure(figsize=(12, 4), dpi=150)
sns.countplot(
    data=fan_reviewed,
    x='STARS_DIFF',
    hue='STARS_DIFF',
    palette='magma',
    legend=False
)
plt.title("Distribution des écarts entre étoiles et notes réelles")
plt.show()

# Film avec un écart proche d'une étoile
fan_reviewed[fan_reviewed['STARS_DIFF'] == 1]


# ===========================================================
# Comparaison avec Rotten Tomatoes
# ===========================================================

plt.figure(figsize=(10, 4), dpi=150)
sns.scatterplot(data=all_sites, x='RottenTomatoes', y='RottenTomatoes_User')
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.title("Critiques RT vs Utilisateurs RT")
plt.show()

# Différence critiques - utilisateurs
all_sites['Rotten_Diff'] = (
    all_sites['RottenTomatoes'] - all_sites['RottenTomatoes_User']
)

# Différence absolue moyenne
all_sites['Rotten_Diff'].abs().mean()

plt.figure(figsize=(10, 4), dpi=200)
sns.histplot(all_sites['Rotten_Diff'], bins=25, kde=True)
plt.title("Distribution des différences RT (critiques - utilisateurs)")
plt.show()

plt.figure(figsize=(10, 4), dpi=200)
sns.histplot(all_sites['Rotten_Diff'].abs(), bins=25, kde=True)
plt.title("Différence absolue RT critiques vs utilisateurs")
plt.show()

# Films adorés par les utilisateurs mais détestés par les critiques
print("Utilisateurs adorent, critiques détestent :")
all_sites.nsmallest(5, 'Rotten_Diff')[['FILM', 'Rotten_Diff']]


# ===========================================================
# Metacritic & IMDb
# ===========================================================

plt.figure(figsize=(10, 4), dpi=150)
sns.scatterplot(data=all_sites, x='Metacritic', y='Metacritic_User')
plt.xlim(0, 100)
plt.ylim(0, 10)
plt.title("Metacritic : critiques vs utilisateurs")
plt.show()

plt.figure(figsize=(10, 4), dpi=150)
sns.scatterplot(
    data=all_sites,
    x='Metacritic_user_vote_count',
    y='IMDB_user_vote_count'
)
plt.title("Votes Metacritic vs IMDb")
plt.show()

# Films les plus votés
all_sites.nlargest(1, 'IMDB_user_vote_count')
all_sites.nlargest(1, 'Metacritic_user_vote_count')


# ===========================================================
# Fusion des datasets
# ===========================================================

df = pd.merge(fandango, all_sites, on='FILM', how='inner')


# ===========================================================
# Normalisation des notes sur une échelle 0–5
# ===========================================================

df['RT_Norm'] = np.round(df['RottenTomatoes'] / 20, 1)
df['RTU_Norm'] = np.round(df['RottenTomatoes_User'] / 20, 1)

df['Meta_Norm'] = np.round(df['Metacritic'] / 20, 1)
df['Meta_U_Norm'] = np.round(df['Metacritic_User'] / 2, 1)

df['IMDB_Norm'] = np.round(df['IMDB'] / 2, 1)

norm_scores = df[
    ['STARS', 'RATING', 'RT_Norm', 'RTU_Norm', 'Meta_Norm', 'Meta_U_Norm', 'IMDB_Norm']
]


# ===========================================================
# Comparaison finale des distributions
# ===========================================================

plt.figure(figsize=(15, 6), dpi=150)
kdes = sns.kdeplot(data=norm_scores, clip=[0, 5], fill=True, palette='Set1')
sns.move_legend(kdes, "upper left")
plt.title("Distribution des notes normalisées")
plt.show()


# ===========================================================
# Clustermap
# ===========================================================

sns.clustermap(norm_scores, cmap='magma', col_cluster=False)
plt.show()


# ===========================================================
# Analyse des pires films (RT)
# ===========================================================

norm_films = df[
    ['STARS', 'RATING', 'RT_Norm', 'RTU_Norm',
     'Meta_Norm', 'Meta_U_Norm', 'IMDB_Norm', 'FILM']
]

worst_films = norm_films.nsmallest(10, 'RT_Norm').drop('FILM', axis=1)

plt.figure(figsize=(15, 6), dpi=150)
sns.kdeplot(data=worst_films, clip=[0, 5], fill=True, palette='Set1')
plt.title("Notes pour les 10 films les plus mal notés par les critiques RT")
plt.show()


# Exemple individuel
norm_films.iloc[25]
