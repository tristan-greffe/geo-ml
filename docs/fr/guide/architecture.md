# Architecture

Chaque projet GeoML suit la même structure en trois couches indépendantes qui communiquent entre elles.

## Structure du dépôt

```
machine-learning/
├── model/                   ← Entraînement du modèle ML
│   ├── data/                   images + masques annotés
│   ├── notebooks/              expérimentations Jupyter
│   ├── src/                    code réutilisable (model.py, dataset.py, train.py…)
│   ├── weights/                modèles entraînés (.pth) — ignorés par git
│   └── requirements.txt
│
├── tree-detection/          ← Application de détection d'arbres
│   ├── backend/                API FastAPI
│   │   ├── main.py             endpoints HTTP
│   │   ├── detection/
│   │   │   ├── imagery.py      téléchargement tuiles IGN WMTS
│   │   │   ├── detect.py       algorithme de détection
│   │   │   └── georef.py       conversion pixels ↔ WGS84
│   │   └── requirements.txt
│   └── frontend/               Interface cartographique
│       ├── index.html
│       ├── app.js              MapLibre GL JS
│       └── style.css
│
└── docs/                    ← Cette documentation (VitePress)
```

## Flux de données

```
IGN WMTS
   │  tuiles ortho 20 cm
   ▼
Backend FastAPI  ──→  modèle U-Net (.pth)
   │  GeoJSON + stats
   ▼
Frontend MapLibre
   │  polygones arbres + panneau stats
   ▼
Navigateur
```

1. Le **frontend** envoie la bbox visible (`POST /api/detect`)
2. Le **backend** télécharge les tuiles IGN correspondantes et les assemble
3. Le **modèle** prédit un masque binaire (arbres vs fond)
4. Le backend vectorise le masque en polygones GeoJSON
5. Le **frontend** affiche les polygones sur la carte et les statistiques dans le panneau

## Ports locaux

| Service | Commande | URL |
|---|---|---|
| Backend | `uvicorn main:app --reload` | `http://localhost:8000` |
| Frontend | `python -m http.server 3000` | `http://localhost:3000` |
| Docs | `npm run docs:dev` | `http://localhost:5173` |
| Notebook | `jupyter notebook` | `http://localhost:8888` |
