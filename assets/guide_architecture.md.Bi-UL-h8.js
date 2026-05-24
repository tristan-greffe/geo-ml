import{b as s,I as n,g as e,j as t}from"./chunks/framework.DUo3J_Qe.js";const u=JSON.parse('{"title":"Architecture","description":"","frontmatter":{},"headers":[],"relativePath":"guide/architecture.md","filePath":"guide/architecture.md"}'),p={name:"guide/architecture.md"};function o(l,a,i,c,r,d){return n(),e("div",null,[...a[0]||(a[0]=[t(`<h1 id="architecture" tabindex="-1">Architecture <a class="header-anchor" href="#architecture" aria-label="Permalink to &quot;Architecture&quot;">​</a></h1><p>Each GeoML project follows the same three-layer structure.</p><h2 id="repository-layout" tabindex="-1">Repository layout <a class="header-anchor" href="#repository-layout" aria-label="Permalink to &quot;Repository layout&quot;">​</a></h2><div class="language- vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang"></span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span>machine-learning/</span></span>
<span class="line"><span>├── model/                   ← ML model training</span></span>
<span class="line"><span>│   ├── data/                   annotated images + masks</span></span>
<span class="line"><span>│   ├── notebooks/              step-by-step Jupyter experiments</span></span>
<span class="line"><span>│   ├── src/                    reusable code (model.py, dataset.py, train.py…)</span></span>
<span class="line"><span>│   ├── weights/                trained models (.pth) — git-ignored</span></span>
<span class="line"><span>│   └── requirements.txt</span></span>
<span class="line"><span>│</span></span>
<span class="line"><span>├── tree-detection/          ← Tree detection application</span></span>
<span class="line"><span>│   ├── backend/                FastAPI</span></span>
<span class="line"><span>│   │   ├── main.py             HTTP endpoints</span></span>
<span class="line"><span>│   │   ├── detection/</span></span>
<span class="line"><span>│   │   │   ├── imagery.py      IGN WMTS tile downloader</span></span>
<span class="line"><span>│   │   │   ├── detect.py       detection algorithm</span></span>
<span class="line"><span>│   │   │   └── georef.py       pixel ↔ WGS84 conversion</span></span>
<span class="line"><span>│   │   └── requirements.txt</span></span>
<span class="line"><span>│   └── frontend/               Map interface</span></span>
<span class="line"><span>│       ├── index.html</span></span>
<span class="line"><span>│       ├── app.js              MapLibre GL JS</span></span>
<span class="line"><span>│       └── style.css</span></span>
<span class="line"><span>│</span></span>
<span class="line"><span>└── docs/                    ← This documentation (VitePress)</span></span></code></pre></div><h2 id="data-flow" tabindex="-1">Data flow <a class="header-anchor" href="#data-flow" aria-label="Permalink to &quot;Data flow&quot;">​</a></h2><div class="language- vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang"></span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span>IGN WMTS</span></span>
<span class="line"><span>   │  20 cm ortho tiles</span></span>
<span class="line"><span>   ▼</span></span>
<span class="line"><span>FastAPI backend  ──→  U-Net model (.pth)</span></span>
<span class="line"><span>   │  GeoJSON polygons + stats</span></span>
<span class="line"><span>   ▼</span></span>
<span class="line"><span>MapLibre frontend</span></span>
<span class="line"><span>   │  tree outlines + statistics panel</span></span>
<span class="line"><span>   ▼</span></span>
<span class="line"><span>Browser</span></span></code></pre></div><ol><li><strong>Frontend</strong> sends the visible bbox (<code>POST /api/detect</code>)</li><li><strong>Backend</strong> downloads the corresponding IGN tiles and assembles them</li><li><strong>Model</strong> predicts a binary mask (trees vs. background)</li><li>Backend vectorizes the mask into GeoJSON polygons</li><li><strong>Frontend</strong> displays polygons on the map and stats in the side panel</li></ol><h2 id="local-ports" tabindex="-1">Local ports <a class="header-anchor" href="#local-ports" aria-label="Permalink to &quot;Local ports&quot;">​</a></h2><table tabindex="0"><thead><tr><th>Service</th><th>Command</th><th>URL</th></tr></thead><tbody><tr><td>Backend</td><td><code>uvicorn main:app --reload</code></td><td><code>http://localhost:8000</code></td></tr><tr><td>Frontend</td><td><code>python -m http.server 3000</code></td><td><code>http://localhost:3000</code></td></tr><tr><td>Docs</td><td><code>npm run docs:dev</code></td><td><code>http://localhost:5173</code></td></tr><tr><td>Notebook</td><td><code>jupyter notebook</code></td><td><code>http://localhost:8888</code></td></tr></tbody></table>`,9)])])}const m=s(p,[["render",o]]);export{u as __pageData,m as default};
