# Processus de machine learning supervisé

![Machine Learning Process](/learning/concepts/ml-process.svg)

1. **Collecter et stocker des données** du monde réel.
2. **Nettoyer et organiser les données** pour les rendre exploitables.
3. **Effectuer une analyse exploratoire** (statistiques, visualisations).
4. **Créer un produit de données** avec le machine learning :
   * **Supervisé** : prédire un résultat futur.
   * **Non supervisé** : découvrir des patterns dans les données.

:::tip 
Pour le machine learning, nous utiliserons principalement la bibliothèque python `scikit-learn`
:::

:::info 👉 Exemple : prédiction du prix d’une maison

* **Caractéristiques (features, X)** : superficie, nombre de chambres, nombre de salles de bain, etc.
* **Label (étiquette, Y)** : prix de vente de la maison.

**But :** Utiliser les données historiques étiquetées pour prédire le prix d’une nouvelle maison.

Ce processus illustre parfaitement la définition de l’apprentissage supervisé : **prédire un résultat à partir de données historiques et étiquetées**.
:::

## Étapes clés de l’apprentissage supervisé

### 1. Séparer les données en features & labels

![Machine Learning Process](/learning/concepts/ml-process1.png)

* `X` : caractéristiques connues de la maison.
* `Y` : label à prédire (prix de vente).

### 2. Diviser les données en ensembles d’entraînement et de tests

![Machine Learning Process](/learning/concepts/ml-process2.png)

* **Training set (entraînement)** : 70 % des données pour apprendre les relations entre X et Y.
* **Test set (tests)** : 30 % des données pour évaluer les performances du modèle sur des données **jamais vues**.

:::tip Pourquoi ?
* On ne peut pas évaluer le modèle sur les données utilisées pour l’entraînement, car il pourrait simplement les mémoriser.
* Les données de test permettent une **évaluation honnête et équitable**.
:::

### 3. Entraîner le modèle

* Le modèle apprend à partir des données d’entraînement (`X_train`, `Y_train`).
* Il détermine comment les features influencent le label.

### 4. Tester le modèle

* Le modèle reçoit uniquement les features de test (`X_test`) et fait des prédictions.
* On compare ensuite les prédictions aux labels réels (`Y_test`).

### 5. Ajuster les hyperparamètres

![Machine Learning Process](/learning/concepts/ml-process5.png)

* Si les performances sont insuffisantes, on ajuste les paramètres du modèle.
* On répète l’entraînement et le test jusqu’à obtenir un modèle satisfaisant.

## Récapitulatif du flux de travail

![Machine Learning Process](/learning/concepts/ml-process4.png)

1. Collecter et nettoyer les données.
2. Identifier les features (X) et le label (Y).
3. Séparer les données en ensembles d’entraînement et de tests.
4. Entraîner le modèle sur l’ensemble d’entraînement.
5. Évaluer le modèle sur l’ensemble de tests.
6. Ajuster les hyperparamètres si nécessaire et répéter.
7. Déployer le modèle pour prédire de nouvelles données ou créer un produit de données.


## Conclusion

Le machine learning supervisé consiste à :

![Machine Learning Process](/learning/concepts/ml-process3.png)

* Utiliser des **données historiques et étiquetées**.
* Apprendre les relations entre features et labels.
* Évaluer le modèle de manière équitable sur des données non vues.
* Ajuster le modèle pour améliorer ses prédictions avant le déploiement.
