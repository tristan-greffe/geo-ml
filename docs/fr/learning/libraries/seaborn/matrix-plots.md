# Diagrammes matriciels

Les **diagrammes matriciels** permettent de visualiser toutes les valeurs numériques d’un DataFrame.
Ils sont équivalents à un **tableau croisé dynamique visuel**, et permettent de **comparer rapidement les valeurs et les tendances**.

## Types de diagrammes matriciels

### Heatmap (carte thermique / carte de fréquentation)

* Représente les valeurs numériques d’un DataFrame via un **mapping de couleur**.
* Utile pour comparer **rapidement les régions, catégories ou valeurs entre elles**.
* Exige que **toutes les colonnes soient de la même unité** (ex. pourcentages, pas mélanger années et taux).

<img src="/learning/libraries/seaborn-heatmap.png" style="display: block; margin: 0 auto;width: 70%; height: auto;">

### Clustermap (carte de regroupement)

* Similaire à la heatmap mais **effectue un clustering automatique** sur les lignes et/ou colonnes.
* Les lignes et colonnes sont réorganisées pour regrouper **les valeurs et régions similaires**.
* Permet de visualiser rapidement **quels groupes ou variables sont proches entre eux**.

<img src="/learning/libraries/seaborn-clustermap.png" style="display: block; margin: 0 auto;width: 70%; height: auto;">

## Points clés à retenir

* **Heatmap** : visualisation simple des valeurs numériques avec une palette de couleur.
* **Clustermap** : heatmap + clustering pour regrouper automatiquement les lignes et colonnes similaires.
* **Toujours homogénéiser les unités** des colonnes pour que la cartographie des couleurs ait un sens.
* **Personnalisation** : couleurs, annotations, lignes et clustering selon les besoins.

## Fichier Python associé

:::details matrix-plots
<<< ./scripts/matrix-plots.py
:::