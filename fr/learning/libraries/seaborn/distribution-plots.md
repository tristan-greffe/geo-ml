# Diagrammes de distribution

Un **diagramme de distribution** permet de visualiser **une seule variable continue** afin d’en analyser :
* la répartition des valeurs
* la moyenne
* la dispersion
* la présence de valeurs extrêmes (outliers)
* la forme globale (symétrie, asymétrie, multimodalité)

:::warning info
Contrairement au scatter plot, on ne cherche **pas une relation entre deux variables**, mais à **comprendre le comportement d’une seule variable**.
:::

## Les trois principaux types de diagrammes de distribution

Les diagrammes de distribution se complètent mutuellement. Les trois formes fondamentales sont :
1. Rug plot (diagramme rug)
2. Histogramme
3. KDE plot (Kernel Density Estimation)

## Le Rug Plot (diagramme rug)

Un **rug plot est la forme la plus simple de visualisation** d’une distribution.
* Chaque observation est représentée par un trait vertical
* Tous les traits sont positionnés le long de l’axe X
* L’axe Y n’a pas de signification

> ➡️ Un trait = une observation

:::info Exemple : distribution des salaires
* Chaque salaire est représenté par un trait
* Les zones où les traits sont nombreux indiquent une forte densité
* Les traits isolés indiquent des valeurs extrêmes
<img src="/learning/libraries/seaborn-rug-plot.png" style="display: block; margin: 0 auto;width: 70%; height: auto;">

> ➡️ Avantage : permet d’identifier immédiatement les outliers

> ➡️ Limite : l’axe Y n’est pas interprétable & difficile à lire lorsque beaucoup de points se chevauchent
:::

## De Rug Plot à Histogramme

Un histogramme est construit directement à partir d’un rug plot. Principe :

1. Découper l’axe X en intervalles appelés `bins` (*Exemple: 3 `bins`*)
<img src="/learning/libraries/seaborn-rug-plot-bins.png" style="display: block; margin: 0 auto;width: 70%; height: auto;">

2. Compter le nombre d’observations dans chaque `bin`
<img src="/learning/libraries/seaborn-rug-plot-bins-count.png" style="display: block; margin: 0 auto;width: 70%; height: auto;">

3. Tracer une barre dont la hauteur correspond à ce nombre
<img src="/learning/libraries/seaborn-rug-plot-bins-trace.png" style="display: block; margin: 0 auto;width: 70%; height: auto;">

:::warning Histogramme normalisé
Parfois, l’axe Y ne représente pas un comptage mais une proportion ou un pourcentage.
<img src="/learning/libraries/seaborn-rug-plot-bins-normalize.png" style="display: block; margin: 0 auto;width: 70%; height: auto;">
:::

:::warning Choix du nombre de bins
Le nombre de bins est un compromis :
<div style="display: flex; gap: 2rem;">
<div style="flex: 1">
Peu de bins → vision globale, perte de détails
<img src="/learning/libraries/seaborn-rug-plot-min-bins.png" style="display: block; margin: 0 auto;width: 90%; height: auto;">
</div>
<div style="flex: 1">
Beaucoup de bins → plus de détails, mais bruit possible
<img src="/learning/libraries/seaborn-rug-plot-max-bins.png" style="display: block; margin: 0 auto;width: 90%; height: auto;">
</div>
</div>
:::

## Le KDE Plot (Kernel Density Estimation / Estimation de la densité par noyau)

Un **KDE plot est une estimation continue de la densité de probabilité** d’une variable.

➡️ Il permet de transformer un échantillon discret en une courbe continue.

:::warning Intuition
Nous disposons :
* d’un ensemble fini de données
* sans connaissance de la distribution réelle sous-jacente

Le KDE permet de répondre à des questions du type : Quelle est la probabilité qu’une valeur se situe autour de x ?
:::

:::info Interprétation
* Les pics indiquent les zones de forte densité
* La largeur indique la dispersion
* La forme révèle : asymétrie / multimodalité / concentration centrale
:::

:::warning Construction conceptuelle
1. Partir d’un rug plot
2. Associer à chaque point une fonction de probabilité
3. Le noyau le plus courant est la distribution gaussienne
4. Centrer une gaussienne sur chaque observation
5. Additionner toutes les courbes
➡️ Le résultat est une courbe lisse continue
<img src="/learning/libraries/seaborn-kde-plot.png" style="display: block; margin: 0 auto;width: 70%; height: auto;">
:::

:::info Effets de bord et limites
Le KDE peut :
* dépasser les valeurs minimales ou maximales observées
* produire des probabilités en dehors du domaine réel
➡️ Exemple :
* Un salaire ne peut pas être négatif
* Pourtant, un KDE peut afficher une densité < 0
:::

:::warning Paramètres clés du KDE
* Noyau (kernel) : souvent gaussien
* Bande passante (bandwidth) :
    * faible → courbe très détaillée
    * élevée → courbe très lisse

➡️ Ces paramètres influencent fortement la visualisation.
:::

## Complémentarité des diagrammes

| Diagramme   | Utilité principale             |
| ----------- | ------------------------------ |
| Rug plot    | voir les valeurs individuelles |
| Histogramme | comprendre la répartition      |
| KDE plot    | estimer une densité continue   |

> 📌 En pratique, on combine souvent : histogramme + KDE

## Fichier Python associé

:::details distribution-plots
<<< ./scripts/distribution-plots.py
:::