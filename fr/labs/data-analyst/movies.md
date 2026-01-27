# Analyse des notes de films Fandango

Les notes en ligne influencent souvent les décisions de spectateurs lorsqu'ils envisagent de voir un film.
Certaines entreprises, comme Fandango, affichent des notes qui peuvent influencer les ventes de billets. Il est donc légitime de se demander :
* Les notes affichées sont-elles influençées à la hausse ?
* Les films reçoivent-ils des notes plus élevées que celles réellement justifiées par les critiques ?

:::warning 🎯 Objecif
1. Charger et explorer les données Fandango et celles des autres sites (Metacritic, IMDb, Rotten Tomatoes).
2. Analyser la distribution des notes.
3. Comparer les notes de Fandango avec celles des autres sites pour détecter un éventuel biais.
4. Visualiser les résultats avec Pandas, Matplotlib et Seaborn.
5. Conclure sur la fiabilité des notes Fandango.
:::

:::tip Data
Les données proviennent de l’article de FiveThirtyEigh *[Be Suspicious Of Online Movie Ratings](https://fivethirtyeight.com/features/fandango-movies-ratings/)* et sont disponibles sur [GitHub](https://github.com/fivethirtyeight/data/tree/master/fandango)
* `all_sites_scores.csv` contient tous les films qui ont une note Rotten Tomatoes, une note RT User, une note Metacritic, une note Metacritic User, une note IMDb, et au moins 30 critiques de fans sur Fandango. Les données de Fandango ont été extraites le 24 août 2015.
* `fandango_scrape.csv` contient tous les films de l'article tirés de Fandango.
:::

:::info Contexte
* Hollywood génère environ 10 milliards de dollars par an au box-office américain.
* Les notes en ligne peuvent influencer la fréquentation des films.
* Sites comme Rotten Tomatoes, Metacritic ou IMDb utilisent différentes méthodes d’agrégation, mais offrent généralement des évaluations fiables.

**Spécificité de Fandango :**
* Fandango utilise une échelle de 3 à 5 étoiles : presque aucun film n’obtient moins de 3 étoiles.
* L'arrondi des notes sur le site a tendance à gonfler les scores :
    * Pour 32 % des films, la note est augmentée de 0,3 à 0,4 étoile par rapport à la note réelle.
    * Pour 8 % des films, une demi-étoile est ajoutée.
* Comparaison avec d’autres sites :
    * Fandango > IMDb dans 79 % des cas
    * Fandango > Metacritic Critics dans 77 % des cas
    * Fandango > Metacritic Users dans 86 % des cas
    * Fandango > Rotten Tomatoes Critics dans 62 % des cas
    * Fandango > Rotten Tomatoes Users dans 74 % des cas
:::

:::details Script
<<< ./scripts/movies.py
:::