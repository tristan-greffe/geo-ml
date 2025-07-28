# Concepts fondamentaux du Machine Learning

Quand on parle d’intelligence artificielle (IA), on met souvent tout dans le même sac.  
En réalité, il existe **plusieurs grandes familles de modèles**, qui se distinguent par **ce qu’ils font** et **comment ils apprennent**.

:::tip
Les modèles de génération (texte, images, audio…) ne représentent **qu’une partie** de l’écosystème.
:::

## Qu’est-ce que le Machine Learning ?

Le **Machine Learning (ML)** est un sous-domaine de l’intelligence artificielle qui permet aux machines **d’apprendre automatiquement à partir de données**, sans être explicitement programmées.

Au lieu d’écrire des règles manuelles, on fournit :
- des données
- un objectif
- un algorithme

:::info
Le modèle apprend alors les règles **par lui-même**
:::

## Les grandes familles de modèles

Chaque famille répond à une **question fondamentale différente**.

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

## Les types d’apprentissage

| Type | Données utilisées | Objectif |
|----|----|----|
| Supervisé | Étiquetées | Prédire |
| Non supervisé | Non étiquetées | Découvrir |
| Renforcement | Récompenses | Décider |


## Fonctionnement d’un projet de Machine Learning

1. Collecte des données  
2. Nettoyage et préparation  
3. Choix du modèle  
4. Entraînement  
5. Évaluation  
6. Amélioration  
7. Déploiement  

:::tip L’importance des données

> *Un modèle n’est jamais meilleur que ses données.*

Qualité, volume et représentativité sont essentiels.
:::





Voici une **version améliorée, claire et structurée** de ce contenu, avec un français corrigé, un enchaînement logique et une meilleure lisibilité pédagogique. Le ton reste neutre et explicatif.

---

# Introduction au Machine Learning

Bienvenue dans la section du cours consacrée au **machine learning**, également appelé *apprentissage automatique*.

Jusqu’à présent, plusieurs outils essentiels pour l’analyse de données ont été abordés :

* **Python**
* **Pandas**
* **Matplotlib**
* **Seaborn**
* Les notebooks **Jupyter** et **Google Colab**

Ces outils permettent de collecter, nettoyer, analyser et visualiser des données.
À partir de maintenant, l’attention se porte sur une nouvelle étape : **utiliser les données pour résoudre des problèmes automatiquement grâce au machine learning**.

---

## 📌 Où en est-on dans le parcours Data Science ?

Le parcours classique en data science et machine learning peut être résumé ainsi :

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

Jusqu’ici, le travail s’est concentré principalement sur l’analyse de données.
La suite du cours se concentre sur la **construction de modèles** capables de généraliser et de produire des résultats exploitables.

---

## 🤖 Pourquoi utiliser le machine learning ?

Le machine learning est utilisé lorsque :

* Les règles sont trop complexes pour être codées manuellement
* Les relations entre variables ne sont pas évidentes
* Le volume de données est important
* Une prédiction ou une automatisation est nécessaire

Contrairement aux algorithmes classiques, le machine learning **apprend directement à partir des données**.

---

## 🧠 Types de machine learning abordés

Deux grandes catégories sont couvertes dans ce cours :

### 1️⃣ Apprentissage supervisé

* Les données contiennent une **variable cible**
* L’objectif est de **prédire un résultat**
* Exemples :

  * régression linéaire
  * régression logistique
  * arbres de décision
  * random forests

### 2️⃣ Apprentissage non supervisé

* Aucune variable cible
* L’objectif est de **découvrir des structures ou des regroupements**
* Exemples :

  * clustering
  * réduction de dimension

La première partie du cours met l’accent sur **l’apprentissage supervisé**, car c’est le plus utilisé en pratique.

---

## 🔄 Le processus général du machine learning supervisé

Un projet de machine learning supervisé suit généralement ces étapes :

1. Compréhension du problème
2. Préparation des données
3. Séparation des données (entraînement / test)
4. Entraînement du modèle
5. Évaluation des performances
6. Ajustement et amélioration du modèle

Ces concepts seront progressivement introduits et approfondis tout au long du cours.

---

## 📚 Concepts clés abordés plus tard

Certains concepts importants ne sont pas détaillés immédiatement, mais seront vus au bon moment :

* **Biais / variance**
* **Underfitting / Overfitting**
* **Validation croisée**
* **Feature engineering**
* **Métriques de performance**
* **Scikit-learn**

Chaque notion sera introduite lorsqu’elle deviendra nécessaire à la compréhension des algorithmes.

---

## 🧩 Organisation des sections Machine Learning

Chaque algorithme du cours suit une structure similaire :

1. Intuition et idées principales
2. Bases théoriques (sans lourdeur mathématique inutile)
3. Implémentation en Python
4. Paramètres et améliorations possibles
5. Exercice ou projet pratique
6. Correction et analyse des résultats

---

## 📐 Cas particulier : la régression linéaire

La **régression linéaire** est le premier algorithme étudié et bénéficie d’un traitement particulier :

* Introduction progressive des concepts
* Première utilisation de **Scikit-learn**
* Découverte des métriques, de la validation croisée et du feature engineering
* Projet final combinant tous les concepts appris

Les deux premières sections du machine learning sont donc légèrement différentes, afin de poser des bases solides.

---

## 🎯 Objectif global de cette section

Cette section introductive ne contient **pas de code**.
Elle vise à :

* Comprendre ce qu’est le machine learning
* Identifier quand et pourquoi l’utiliser
* Se préparer au changement de paradigme entre analyse de données et modélisation

---

La prochaine étape consiste à comprendre **les cas d’usage du machine learning** et les types de problèmes qu’il permet de résoudre.

➡️ Rendez-vous dans la prochaine vidéo pour commencer cette exploration.
