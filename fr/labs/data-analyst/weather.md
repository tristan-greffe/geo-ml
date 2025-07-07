# Analyse climatique d’une ville

Les données météorologiques permettent de mieux comprendre l’évolution du climat d’une ville au fil du temps.

:::warning 🎯 Objectif 
Analyser plusieurs années de données météo afin d’identifier des tendances saisonnières et de construire un dashboard visuel clair et informatif.
* Comprendre l’évolution des températures
* Comparer les saisons (été / hiver)
* Étudier la fréquence des précipitations
* Visualiser les données sous forme de graphiques synthétiques
:::

:::tip Dataset: kaggle
* **Kaggle** : Daily Weather Data
* **data.gouv** : données météorologiques locales (stations météo)
Le dataset doit contenir au minimum :
* Une colonne de date
* Une température (moyenne, minimale ou maximale)
* Une information sur les précipitations (pluie ou non)
:::

## Étapes de l’analyse

1. Préparation des données
2. Température moyenne par mois : Calculer la température moyenne pour chaque mois & visualiser le résultat avec un graphique en ligne ou un graphique en barres
3. Comparaison été (juin, juillet, août) / hiver (décembre, janvier, février) : Comparer les températures moyennes & visualiser la comparaison avec un boxplot ou un barplot
4. Jours de pluie par mois : Identifier les jours avec précipitations puis compter le nombre de jours de pluie par mois & visualiser les résultats avec un graphique en barres
5. Heatmap température jour / mois : Créer une table pivot (lignes : jours / colonnes : mois / valeurs : température moyenne) & Afficher une heatmap avec Seaborn

:::details Script
<<< ./scripts/movies.py
:::