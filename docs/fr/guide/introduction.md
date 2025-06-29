# Guide du projet

Ce guide couvre la documentation technique de GeoML : comment le projet est structuré, comment les composants communiquent, et comment le lancer localement.

## Projets

### Détection d'arbres

Premier projet GeoML. Un modèle de segmentation sémantique (U-Net) détecte les couronnes d'arbres depuis une orthophoto IGN 20 cm, et les affiche sous forme de polygones sur une carte MapLibre.

**Composants :**
- `model/` — entraînement PyTorch (notebooks + code source)
- `tree-detection/backend/` — API FastAPI qui appelle le modèle
- `tree-detection/frontend/` — carte MapLibre + panneau de statistiques
