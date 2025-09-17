# Introduction à la régression linéaire

La `régression linéaire` est l’un des algorithmes les plus fondamentaux en machine learning… et aussi l’un des plus anciens. Une relation linéaire, c’est simplement : **une relation en ligne droite**

:::info Exemple : x = y
On peut modéliser parfaitement ces données avec une droite

![régression linéaire](/learning/algorithms/linear-regression.png)

➡️ Cela implique que pour une nouvelle valeur de x, je peux prédire la valeur de y qui lui est associée.
:::

## Problème dans la vraie vie

❌ **les données ne sont jamais parfaitement alignées** : Où tracer la ligne droite ?

![régression linéaire 1](/learning/algorithms/linear-regression1.png)

➡️ Nous comprenons que l'objectif est de minimiser la distance gloable entre les points et la ligne donc de **trouver la meilleure droite qui approxime les données avec la plus petite erreur résiduelle** → `La droite de “meilleur ajustement”`

![régression linéaire 2](/learning/algorithms/linear-regression2.png)

:::tip L'erreur résiduelle
L'erreur résiduelle est la distance entre un point et la droite. Elle être positive ou négative.

![régression linéaire 3](/learning/algorithms/linear-regression3.png)
:::

## Méthode des Moindres Carrés Ordinaires MCO (Ordinary Least Squares - OLS) 

➡️ minimiser l’erreur globale entre les prédictions et les données réelles

$$\sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$

👉 On minimise la somme des erreurs au carré

:::tip Pourquoi le carré ?
* évite l’annulation des erreurs (+ / -)
* pénalise fortement les grosses erreurs
* facilite les calculs mathématiques (dérivées)

➡️ Visiualisation de l'erreur quadratique à minimiser 
![régression linéaire 4](/learning/algorithms/linear-regression4.png)
:::

## Workflow régression linéaire

```mermaid
flowchart LR
    A[Tracer une droite]:::de --> B[Mesurer les erreurs résiduelles]:::da
    B --> C[Ajuster la droite]:::da
    C --> D[Minimiser les erreurs totales]:::ml
    D --> C:::ml

    classDef de fill:#D0DCF4,stroke:#333,stroke-width:1px;
    classDef da fill:#F9C493,stroke:#333,stroke-width:1px;
    classDef ml fill:#D09CB6,stroke:#333,stroke-width:1px;
```

