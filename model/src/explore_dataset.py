"""
Télécharge des tuiles IGN orthophoto (WMTS public) sur une zone forestière
et génère un masque EGI (Excess Green Index) — la baseline classique
avant d'entraîner le modèle U-Net.

Zone : Forêt de Fontainebleau (bien pourvue en feuillage, zoom 18 IGN).
"""

import math
from io import BytesIO
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
import requests
from PIL import Image

DATA_DIR = Path(__file__).parent.parent / "data" / "ign-sample"
DATA_DIR.mkdir(parents=True, exist_ok=True)

# --- Paramètres de la zone ---
CENTER_LAT = 48.404
CENTER_LON = 2.699
ZOOM = 18
GRID = 3  # grille GRID×GRID tuiles (chaque tuile = 256×256 px)

IGN_WMTS = (
    "https://data.geopf.fr/wmts"
    "?SERVICE=WMTS&REQUEST=GetTile&VERSION=1.0.0"
    "&LAYER=ORTHOIMAGERY.ORTHOPHOTOS"
    "&STYLE=normal&FORMAT=image/jpeg"
    "&TILEMATRIXSET=PM"
    "&TILEMATRIX={z}&TILEROW={y}&TILECOL={x}"
)


# ── Coordonnées ────────────────────────────────────────────────────────────────

def latlon_to_tile(lat: float, lon: float, zoom: int) -> tuple[int, int]:
    n = 2 ** zoom
    x = int((lon + 180) / 360 * n)
    lat_r = math.radians(lat)
    y = int((1 - math.log(math.tan(lat_r) + 1 / math.cos(lat_r)) / math.pi) / 2 * n)
    return x, y


# ── Téléchargement ─────────────────────────────────────────────────────────────

def fetch_tile(tx: int, ty: int, zoom: int) -> np.ndarray:
    cache = DATA_DIR / f"{zoom}_{tx}_{ty}.jpg"
    if cache.exists():
        return np.array(Image.open(cache).convert("RGB"))
    url = IGN_WMTS.format(z=zoom, x=tx, y=ty)
    r = requests.get(url, headers={"User-Agent": "GeoML/1.0"}, timeout=15)
    r.raise_for_status()
    img = Image.open(BytesIO(r.content)).convert("RGB")
    img.save(cache)
    return np.array(img)


def fetch_mosaic(center_lat: float, center_lon: float, zoom: int, grid: int) -> np.ndarray:
    cx, cy = latlon_to_tile(center_lat, center_lon, zoom)
    half = grid // 2
    rows = []
    for dy in range(-half, half + 1):
        cols = []
        for dx in range(-half, half + 1):
            print(f"  tuile ({cx + dx}, {cy + dy})…", end="\r")
            tile = fetch_tile(cx + dx, cy + dy, zoom)
            cols.append(tile)
        rows.append(np.concatenate(cols, axis=1))
    print()
    return np.concatenate(rows, axis=0)


# ── EGI + masque ──────────────────────────────────────────────────────────────

def compute_egi(img: np.ndarray) -> np.ndarray:
    """EGI = 2G - R - B, normalisé [0, 255]."""
    f = img.astype(np.float32)
    egi = 2 * f[:, :, 1] - f[:, :, 0] - f[:, :, 2]
    mn, mx = egi.min(), egi.max()
    return ((egi - mn) / (mx - mn) * 255).astype(np.uint8) if mx > mn else np.zeros_like(egi, dtype=np.uint8)


def otsu_threshold(arr: np.ndarray) -> np.ndarray:
    """Seuillage Otsu sans OpenCV (numpy uniquement)."""
    hist, edges = np.histogram(arr.ravel(), bins=256, range=(0, 256))
    total = arr.size
    sum_all = np.dot(np.arange(256), hist)
    sum_b, w_b, best_t, best_var = 0.0, 0, 0, 0.0
    for t in range(256):
        w_b += hist[t]
        w_f = total - w_b
        if w_b == 0 or w_f == 0:
            continue
        sum_b += t * hist[t]
        mb = sum_b / w_b
        mf = (sum_all - sum_b) / w_f
        var = w_b * w_f * (mb - mf) ** 2
        if var > best_var:
            best_var, best_t = var, t
    return (arr > best_t).astype(np.uint8)


# ── Visualisation ─────────────────────────────────────────────────────────────

def show(img: np.ndarray):
    egi = compute_egi(img)
    mask = otsu_threshold(egi)

    h, w = img.shape[:2]
    coverage = mask.sum() / (h * w) * 100

    print(f"Image : {h}×{w} px")
    print(f"Couverture végétale EGI : {coverage:.1f} %")

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle(
        f"IGN orthophoto — Forêt de Fontainebleau (zoom {ZOOM})\n"
        f"Couverture végétale EGI : {coverage:.1f} %",
        fontsize=12, fontweight="bold",
    )

    axes[0].imshow(img)
    axes[0].set_title("Orthophoto RGB")
    axes[0].axis("off")

    axes[1].imshow(egi, cmap="YlGn")
    axes[1].set_title("Indice EGI (2G - R - B)")
    axes[1].axis("off")

    overlay = img.copy()
    overlay[mask == 1] = [80, 200, 80]  # vert = arbre détecté
    axes[2].imshow(overlay)
    axes[2].set_title("Masque EGI (seuil Otsu)")
    axes[2].axis("off")

    plt.tight_layout()
    out = DATA_DIR / "preview.png"
    plt.savefig(out, dpi=150)
    print(f"Preview sauvegardé → {out}")
    plt.show()


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    print(f"Téléchargement {GRID}×{GRID} tuiles IGN zoom {ZOOM}…")
    img = fetch_mosaic(CENTER_LAT, CENTER_LON, ZOOM, GRID)
    show(img)


if __name__ == "__main__":
    main()
