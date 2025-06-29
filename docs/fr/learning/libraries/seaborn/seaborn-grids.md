# Grilles Seaborn (Grids)

Seaborn propose des **grilles de tracés** qui permettent de créer facilement des sous-graphes organisés par **catégories**. Elles sont analogues à `subplot` de Matplotlib, mais **automatisent la création de la grille** selon les colonnes catégorielles.

<img src="/learning/libraries/seaborn-pair-grid.png" style="display: block; margin: 0 auto;width: 70%; height: auto;">

## FacetGrid

* `sns.catplot` (anciennement appelé “four plots”) crée automatiquement une **grille de sous-graphes**.
* L’organisation se fait selon les colonnes ou lignes d’une **variable catégorielle**.
* Plus besoin de calculer manuellement le nombre de lignes ou colonnes dans `subplot`.

## PairGrid

Le `PairGrid` est une version avancée du `pairplot` :

* Permet de personnaliser les diagrammes sur la diagonale et hors-diagonale
* Offre une grande flexibilité pour les visualisations complexes

## Comparaison entre `catplot` et `FacetGrid` / `PairGrid`

| Objectif                                               | Utiliser                                           |
| ------------------------------------------------------ | -------------------------------------------------- |
| Grille simple de diagrammes catégoriels                | `sns.catplot` avec `row` et `col`                  |
| Grille personnalisée pour pairs de variables continues | `sns.PairGrid`                                     |
| Visualisation simple d’un pair plot                    | `sns.pairplot` (suffisant dans la plupart des cas) |

* `PairGrid` : souplesse maximale, mais plus complexe
* `catplot` : facilité d’utilisation, suffisant pour la majorité des cas

## Fichier Python associé

:::details seaborn-grids
<<< ./scripts/seaborn-grids.py
:::