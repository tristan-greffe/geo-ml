# Types d’apprentissage

![familles de modèles](/learning/concepts/model-families.png)

## 1. Apprentissage supervisé

L’apprentissage supervisé repose sur deux concepts clés :

* **Données historiques** : on dispose d’exemples passés avec résultats connus.
* **Données étiquetées** : chaque exemple possède une sortie ou un label associé.

:::info 👉 Exemple : prédiction du prix d’une maison
* Caractéristiques (features) : surface, nombre de chambres, type de sol, etc.
* Label (étiquette) : prix de vente réel.

Le modèle apprend à **associer les caractéristiques au prix** à partir des données passées.
Lorsqu’une nouvelle maison apparaît, il prédit son prix de vente à partir de ses caractéristiques.
:::

:::tip Deux types de tâches supervisées
1. **Classification** : prédire une catégorie (valeur discrète)
> 👉 Exemple : déterminer si une tumeur est **maligne ou bénigne**, ou si un client remboursera ou fera défaut sur son prêt.

2. **Régression** : prédire une valeur continue
>  👉 Exemple : prédire le **prix d’une maison**, la consommation d’électricité ou les résultats scolaires.
:::

## 2. Apprentissage non supervisé

L’apprentissage non supervisé utilise des **données non étiquetées**. Le modèle doit **découvrir lui-même des motifs ou des groupes** dans les données.

:::info 👉 Exemple 
**segmenter des clients** en groupes en fonction de leurs comportements d’achat.
:::

:::tip Limite
Évaluer la performance d’un modèle non supervisé est plus difficile, car il n’y a pas de labels connus au départ.
:::

## Conclusion

1. **Supervisé** : utiliser des données étiquetées pour prédire un résultat futur.
2. **Non supervisé** : trouver des motifs dans des données sans labels.

| Type | Données utilisées | Objectif |
|----|----|----|
| Supervisé | Étiquetées | Prédire |
| Non supervisé | Non étiquetées | Découvrir |
| Renforcement | Récompenses | Décider |
