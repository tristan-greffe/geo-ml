# Concepts fondamentaux

Quand on parle d’intelligence artificielle, on met souvent tout dans le même sac.  
En réalité, il existe **plusieurs grandes familles de modèles**, qui se distinguent par **ce qu’ils font** et **comment ils apprennent**.

:::tip
Les modèles de génération (texte, images, audio…) ne représentent qu’une partie de l’écosystème.
:::

## Le parcours classique en data science

![Machine Learning](/learning/concepts/machine-learning.svg)

1. Le point de départ est toujours le **monde réel**
2. Un **problème** ou une **question** se pose, par exemple :
   * Comment prédire une valeur future ?
   * Comment expliquer l’influence d’une variable sur une autre ?
3. Les données sont :
   * collectées
   * stockées
   * nettoyées
   * explorées (EDA)
4. Enfin, des **modèles de machine learning** sont utilisés pour :
   * faire des prédictions
   * découvrir des structures cachées dans les données



:::info Fonctionnement d’un projet de Machine Learning
1. Collecte des données  
2. Nettoyage et préparation  
3. Choix du modèle  
4. Entraînement  
5. Évaluation  
6. Amélioration  
7. Déploiement  
:::

## Les types d’apprentissage

| Type | Données utilisées | Objectif |
|----|----|----|
| Supervisé | Étiquetées | Prédire |
| Non supervisé | Non étiquetées | Découvrir |
| Renforcement | Récompenses | Décider |

### 1️⃣ Apprentissage supervisé
* Les données contiennent une **variable cible**
* L’objectif est de **prédire un résultat**

:::tip Le processus général du machine learning supervisé
1. Compréhension du problème
2. Préparation des données
3. Séparation des données (entraînement / test)
4. Entraînement du modèle
5. Évaluation des performances
6. Ajustement et amélioration du modèle
:::

:::info Exemples
  * régression linéaire
  * régression logistique
  * arbres de décision
  * random forests
:::

### 2️⃣ Apprentissage non supervisé
* Aucune variable cible
* L’objectif est de **découvrir des structures ou des regroupements**

:::info Exemples
  * clustering
  * réduction de dimension
:::

## Les grandes familles de modèles

Chaque famille répond à une **question fondamentale différente**.

![familles de modèles](/learning/concepts/model-families.png)

### Modèles de classification
👉 *« C’est quoi ? »*

Décider dans quelle **catégorie** appartient une donnée.

:::details **Exemples**
- Email → spam / non spam
- Image → chat / chien
- Transaction → fraude / normale
:::

### Modèles de régression
👉 *« Combien ? »*

Prédire une **valeur numérique continue**.

:::details **Exemples**
- Prix d’un appartement
- Temps de livraison
- Consommation électrique
:::

### Modèles de clustering (non supervisés)
👉 *« Qui ressemble à qui ? »*

Regrouper les données **sans labels**.

:::details **Exemples**
- Segmentation client
- Regroupement d’articles
- Analyse de comportements
:::

### Modèles de détection d’anomalies
👉 *« Qu’est-ce qui est anormal ? »*

Identifier les comportements atypiques.

:::details **Exemples**
- Fraude bancaire
- Pannes industrielles
- Intrusions réseau
:::

### Modèles de recommandation
👉 *« Qu’est-ce qui pourrait t’intéresser ? »*

Proposer du contenu pertinent.

:::details **Exemples**
- Netflix
- Spotify
- Amazon
:::

### Modèles de réduction de dimension
👉 *« Comment simplifier ? »*

Réduire le nombre de variables tout en conservant l’essentiel.

:::details **Objectifs**
- Visualisation
- Accélération des modèles
- Compression
:::

### Modèles de séries temporelles
👉 *« Que va-t-il se passer ? »*

Prédire le futur à partir du passé.

:::details **Exemples**
- Prévisions de ventes
- Charge serveur
- Météo
:::

### Apprentissage par renforcement
👉 *« Quelle action choisir ? »*

Apprendre par **essai-erreur** à l’aide de récompenses.

:::details **Concepts clés**
- Agent
- Environnement
- Récompense
- Politique
:::

### Modèles de génération
👉 *« Que puis-je créer ? »*

Créer du **nouveau contenu**.

:::details **Exemples**
- Texte
- Images
- Audio
- Code
:::
