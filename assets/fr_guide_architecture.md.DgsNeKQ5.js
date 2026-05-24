import{b as a,I as n,g as e,j as t}from"./chunks/framework.DUo3J_Qe.js";const h=JSON.parse('{"title":"Architecture","description":"","frontmatter":{},"headers":[],"relativePath":"fr/guide/architecture.md","filePath":"fr/guide/architecture.md"}'),p={name:"fr/guide/architecture.md"};function l(o,s,i,r,c,d){return n(),e("div",null,[...s[0]||(s[0]=[t(`<h1 id="architecture" tabindex="-1">Architecture <a class="header-anchor" href="#architecture" aria-label="Permalink to &quot;Architecture&quot;">​</a></h1><p>Chaque projet GeoML suit la même structure en trois couches indépendantes qui communiquent entre elles.</p><h2 id="structure-du-depot" tabindex="-1">Structure du dépôt <a class="header-anchor" href="#structure-du-depot" aria-label="Permalink to &quot;Structure du dépôt&quot;">​</a></h2><div class="language- vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang"></span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span>machine-learning/</span></span>
<span class="line"><span>├── model/                   ← Entraînement du modèle ML</span></span>
<span class="line"><span>│   ├── data/                   images + masques annotés</span></span>
<span class="line"><span>│   ├── notebooks/              expérimentations Jupyter</span></span>
<span class="line"><span>│   ├── src/                    code réutilisable (model.py, dataset.py, train.py…)</span></span>
<span class="line"><span>│   ├── weights/                modèles entraînés (.pth) — ignorés par git</span></span>
<span class="line"><span>│   └── requirements.txt</span></span>
<span class="line"><span>│</span></span>
<span class="line"><span>├── tree-detection/          ← Application de détection d&#39;arbres</span></span>
<span class="line"><span>│   ├── backend/                API FastAPI</span></span>
<span class="line"><span>│   │   ├── main.py             endpoints HTTP</span></span>
<span class="line"><span>│   │   ├── detection/</span></span>
<span class="line"><span>│   │   │   ├── imagery.py      téléchargement tuiles IGN WMTS</span></span>
<span class="line"><span>│   │   │   ├── detect.py       algorithme de détection</span></span>
<span class="line"><span>│   │   │   └── georef.py       conversion pixels ↔ WGS84</span></span>
<span class="line"><span>│   │   └── requirements.txt</span></span>
<span class="line"><span>│   └── frontend/               Interface cartographique</span></span>
<span class="line"><span>│       ├── index.html</span></span>
<span class="line"><span>│       ├── app.js              MapLibre GL JS</span></span>
<span class="line"><span>│       └── style.css</span></span>
<span class="line"><span>│</span></span>
<span class="line"><span>└── docs/                    ← Cette documentation (VitePress)</span></span></code></pre></div><h2 id="flux-de-donnees" tabindex="-1">Flux de données <a class="header-anchor" href="#flux-de-donnees" aria-label="Permalink to &quot;Flux de données&quot;">​</a></h2><div class="language- vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang"></span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span>IGN WMTS</span></span>
<span class="line"><span>   │  tuiles ortho 20 cm</span></span>
<span class="line"><span>   ▼</span></span>
<span class="line"><span>Backend FastAPI  ──→  modèle U-Net (.pth)</span></span>
<span class="line"><span>   │  GeoJSON + stats</span></span>
<span class="line"><span>   ▼</span></span>
<span class="line"><span>Frontend MapLibre</span></span>
<span class="line"><span>   │  polygones arbres + panneau stats</span></span>
<span class="line"><span>   ▼</span></span>
<span class="line"><span>Navigateur</span></span></code></pre></div><ol><li>Le <strong>frontend</strong> envoie la bbox visible (<code>POST /api/detect</code>)</li><li>Le <strong>backend</strong> télécharge les tuiles IGN correspondantes et les assemble</li><li>Le <strong>modèle</strong> prédit un masque binaire (arbres vs fond)</li><li>Le backend vectorise le masque en polygones GeoJSON</li><li>Le <strong>frontend</strong> affiche les polygones sur la carte et les statistiques dans le panneau</li></ol><h2 id="ports-locaux" tabindex="-1">Ports locaux <a class="header-anchor" href="#ports-locaux" aria-label="Permalink to &quot;Ports locaux&quot;">​</a></h2><table tabindex="0"><thead><tr><th>Service</th><th>Commande</th><th>URL</th></tr></thead><tbody><tr><td>Backend</td><td><code>uvicorn main:app --reload</code></td><td><code>http://localhost:8000</code></td></tr><tr><td>Frontend</td><td><code>python -m http.server 3000</code></td><td><code>http://localhost:3000</code></td></tr><tr><td>Docs</td><td><code>npm run docs:dev</code></td><td><code>http://localhost:5173</code></td></tr><tr><td>Notebook</td><td><code>jupyter notebook</code></td><td><code>http://localhost:8888</code></td></tr></tbody></table>`,9)])])}const m=a(p,[["render",l]]);export{h as __pageData,m as default};
