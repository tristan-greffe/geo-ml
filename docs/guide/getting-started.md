# Getting started

## Prerequisites

- Python 3.11+
- Node.js 20+
- Git

## 1. Clone the repository

```bash
git clone https://github.com/tristan-greffe/machine-learning.git
cd machine-learning
```

## 2. Run the backend

```bash
cd tree-detection/backend
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

API available at `http://localhost:8000`.  
Health check: `http://localhost:8000/health` → `{"status":"ok"}`

## 3. Run the frontend

In a second terminal:

```bash
cd tree-detection/frontend
python -m http.server 3000
```

Open `http://localhost:3000`.

## 4. Train the model (optional)

```bash
cd model
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook
```

Open `notebooks/01_exploration.ipynb` to get started.

## 5. Run the documentation

```bash
cd docs
npm install
npm run docs:dev
```

Documentation available at `http://localhost:5173`.
