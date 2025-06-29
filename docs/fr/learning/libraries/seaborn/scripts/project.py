import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ===========================================================
# Chargement des données
# Source : https://www.kaggle.com/rikdifos/credit-card-approval-prediction
# ===========================================================

"""
Les cartes de credit Scoring (évaluation des risques) sont une méthode courante de contrôle des risques dans le secteur financier.
Il utilise les informations personnelles et les données soumises par les demandeurs de carte de crédit pour prédire la probabilité de futurs défauts de paiement et d'emprunts de carte de crédit.
La banque est en mesure de décider d'émettre une carte de crédit au demandeur. Les Credit Scores peuvent quantifier objectivement l'ampleur du risque.
"""

list_url = ['https://raw.githubusercontent.com/moncoachdata/MasterClass_DS_ML/main/application_record-1.csv',
            'https://raw.githubusercontent.com/moncoachdata/MasterClass_DS_ML/main/application_record-2.csv',
            'https://raw.githubusercontent.com/moncoachdata/MasterClass_DS_ML/main/application_record-3.csv']

df = pd.concat([pd.read_csv(f) for f in list_url],ignore_index=True)

df.info()

# ===========================================================
# Diagrammes de dispersion
# ===========================================================

# RETIRER LES PERSONNES SANS EMPLOI
employed = df[df['DAYS_EMPLOYED']<0]

# RENDRE LES 2 COLONNES POSITIVES
employed['DAYS_EMPLOYED'] = -1*employed['DAYS_EMPLOYED']
employed['DAYS_BIRTH'] = -1*employed['DAYS_BIRTH']
sns.scatterplot(
    x="DAYS_BIRTH",
    y="DAYS_EMPLOYED",
    data=employed,
    linewidth=0
)

plt.show()

# ===========================================================
# Diagrammes de distribution
# ===========================================================

df['DAYS_BIRTH'] = -1*df['DAYS_BIRTH']
df['AGE'] = round(df['DAYS_BIRTH'] / 365)

plt.xlabel("Âge en années")
plt.ylabel("Nombre")

sns.histplot(
    x="AGE",
    data=df,
    bins=50
)

plt.show()

# ===========================================================
# Diagrammes catégoriels
# ===========================================================

plt.figure(figsize=(12,5))

bottom_half_income = df.nsmallest(n=int(0.5*len(df)),columns='AMT_INCOME_TOTAL')
sns.boxplot(x='NAME_FAMILY_STATUS',y='AMT_INCOME_TOTAL',data=bottom_half_income,hue='FLAG_OWN_REALTY')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.,title='FLAG_OWN_REALTY')
plt.title('Revenus totaux par situation familiale pour la moitié inférieure des salariés')

plt.show()

# ===========================================================
# Diagrammes Matriciels
# ===========================================================

sns.heatmap(df.drop('FLAG_MOBIL',axis=1).corr(),cmap="viridis")

plt.show()