# Project Guide

This guide covers the technical documentation of GeoML: how the project is structured, how components communicate, and how to run it locally.

## Projects

### Tree detection

First GeoML project. A semantic segmentation model (U-Net) detects tree crowns from IGN 20 cm orthophotos and displays them as polygons on a MapLibre map.

**Components:**
- `model/` — PyTorch training (notebooks + source code)
- `tree-detection/backend/` — FastAPI serving the model
- `tree-detection/frontend/` — MapLibre map + statistics panel
