# Démarrage rapide

## Prérequis

- Python 3.11+
- Node.js 20+
- Git

## 1. Cloner le dépôt

```bash
git clone https://github.com/tristan-greffe/machine-learning.git
cd machine-learning
```

## 2. Lancer le backend

```bash
cd tree-detection/backend
python -m venv .venv
source .venv/bin/activate      # Windows : .venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

L'API est disponible sur `http://localhost:8000`.  
Vérification : `http://localhost:8000/health` → `{"status":"ok"}`

## 3. Lancer le frontend

Dans un second terminal :

```bash
cd tree-detection/frontend
python -m http.server 3000
```

Ouvrir `http://localhost:3000` dans le navigateur.

## 4. Entraîner le modèle (optionnel)

```bash
cd model
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook
```

Ouvrir le notebook `notebooks/01_exploration.ipynb` pour commencer.

## 5. Lancer la documentation

```bash
cd docs
npm install
npm run docs:dev
```

Documentation disponible sur `http://localhost:5173`.

## Structure des branches

```
master          ← branche principale stable
feature/xxx     ← nouvelles fonctionnalités
fix/xxx         ← corrections de bugs
```
