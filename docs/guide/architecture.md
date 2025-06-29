# Architecture

Each GeoML project follows the same three-layer structure.

## Repository layout

```
machine-learning/
├── model/                   ← ML model training
│   ├── data/                   annotated images + masks
│   ├── notebooks/              step-by-step Jupyter experiments
│   ├── src/                    reusable code (model.py, dataset.py, train.py…)
│   ├── weights/                trained models (.pth) — git-ignored
│   └── requirements.txt
│
├── tree-detection/          ← Tree detection application
│   ├── backend/                FastAPI
│   │   ├── main.py             HTTP endpoints
│   │   ├── detection/
│   │   │   ├── imagery.py      IGN WMTS tile downloader
│   │   │   ├── detect.py       detection algorithm
│   │   │   └── georef.py       pixel ↔ WGS84 conversion
│   │   └── requirements.txt
│   └── frontend/               Map interface
│       ├── index.html
│       ├── app.js              MapLibre GL JS
│       └── style.css
│
└── docs/                    ← This documentation (VitePress)
```

## Data flow

```
IGN WMTS
   │  20 cm ortho tiles
   ▼
FastAPI backend  ──→  U-Net model (.pth)
   │  GeoJSON polygons + stats
   ▼
MapLibre frontend
   │  tree outlines + statistics panel
   ▼
Browser
```

1. **Frontend** sends the visible bbox (`POST /api/detect`)
2. **Backend** downloads the corresponding IGN tiles and assembles them
3. **Model** predicts a binary mask (trees vs. background)
4. Backend vectorizes the mask into GeoJSON polygons
5. **Frontend** displays polygons on the map and stats in the side panel

## Local ports

| Service | Command | URL |
|---|---|---|
| Backend | `uvicorn main:app --reload` | `http://localhost:8000` |
| Frontend | `python -m http.server 3000` | `http://localhost:3000` |
| Docs | `npm run docs:dev` | `http://localhost:5173` |
| Notebook | `jupyter notebook` | `http://localhost:8888` |
