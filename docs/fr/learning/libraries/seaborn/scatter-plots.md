# Diagrammes de dispersion

Les **diagrammes de dispersion**, aussi appelés nuages de points (*scatter plots en anglais*), sont l’un des outils les plus fondamentaux en analyse exploratoire des données (EDA). Ils permettent de:

* visualiser la **relation entre deux variables continues**
* détecter des **tendances**
* identifier des **corrélations**
* repérer des **valeurs aberrantes (outliers)**

:::info Exemple
Imaginons une entreprise avec des commerciaux. Variables disponibles :
* **Salaire** (numérique continu)
* **Ventes annuelles** (numérique continu)
* **Expérience professionnelle**
* **Niveau d’éducation**

> ❓ existe-t-il une relation entre le salaire et les ventes ?



<img src="/learning/libraries/seaborn-scatter-plots-1.png" style="display: block; margin: 0 auto;width: 70%; height: auto;">

* Chaque point représente un employé.
* Axe X → salaire
* Axe Y → ventes

Si les points montent globalement vers la droite, cela suggère une relation positive : plus les ventes sont élevées, plus le salaire tend à augmenter.
:::

## Fichier Python associé

:::details scatter-plots
<<< ./scripts/scatter-plots.py
:::