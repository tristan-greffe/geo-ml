Voici un **mémo clair et complet des commandes Conda les plus importantes**, avec focus sur **lister et supprimer les environnements** 👇

---

# 📋 🔎 Lister les environnements

```bash
conda env list
```

ou

```bash
conda info --envs
```

👉 L’environnement actif est marqué avec `*`

---

# ❌ 🗑️ Supprimer un environnement

```bash
conda remove -n nom_env --all
```

👉 Exemple :

```bash
conda remove -n mon_projet --all
```

---

# ⚙️ 🧱 Commandes essentielles Conda

## 📦 Créer un environnement

```bash
conda create -n mon_env python=3.11
```

Avec packages :

```bash
conda create -n mon_env python=3.11 numpy pandas
```

---

## ▶️ Activer / désactiver

```bash
conda activate mon_env
```

```bash
conda deactivate
```

---

## 📥 Installer des packages

```bash
conda install numpy
```

Avec conda-forge :

```bash
conda install -c conda-forge numpy
```

---

## 🔄 Mettre à jour

### Un package

```bash
conda update numpy
```

### Tout l’environnement

```bash
conda update --all
```

---

## 📤 Exporter un environnement

```bash
conda env export > environment.yml
```

---

## 📥 Recréer un environnement

```bash
conda env create -f environment.yml
```

---

## 📃 Voir les packages installés

```bash
conda list
```

---

## 🧹 Supprimer un package

```bash
conda remove numpy
```

---

## 🔍 Chercher un package

```bash
conda search nom_package
```

---

## ⚡ Infos générales

```bash
conda info
```

---

## 🧼 Nettoyer cache (très utile)

```bash
conda clean --all
```

---

# 🧠 Bon workflow recommandé

```bash
conda create -n projet python=3.11
conda activate projet
conda install -c conda-forge numpy pandas matplotlib
conda env export > environment.yml
```

---

# ⚠️ Erreurs fréquentes à éviter

* ❌ Oublier d’activer l’env
* ❌ Mélanger `pip` et `conda` sans réfléchir
* ❌ Mélanger `defaults` et `conda-forge` sans `strict`

---

Si tu veux, je peux te faire une **cheat sheet ultra courte (10 commandes max)** ou un **setup parfait pour data science / dev web** 👍
