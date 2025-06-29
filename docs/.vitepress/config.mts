import { withMermaid } from 'vitepress-plugin-mermaid'

export default withMermaid({
  base: '/machine-learning',
  title: 'GeoML',
  ignoreDeadLinks: true,
  appearance: false,
  head: [
    ['link', { href: 'https://cdnjs.cloudflare.com/ajax/libs/line-awesome/1.3.0/line-awesome/css/line-awesome.min.css', rel: 'stylesheet' }],
    ['link', { rel: 'icon', type: 'image/svg+xml', href: '/machine-learning/logo.svg' }]
  ],
  markdown: {
    math: true
  },
  locales: {
    root: {
      label: 'English',
      lang: 'en',
      themeConfig: {
        nav: [
          { text: 'About',    link: '/about/introduction' },
          { text: 'Guide',    link: '/guide/introduction' },
          { text: 'Learning', link: '/fr/learning/introduction' }
        ],
        sidebar: {
          '/about/': getAboutSidebar('en'),
          '/guide/': getGuideSidebar('en')
        }
      }
    },
    fr: {
      label: 'Français',
      lang: 'fr',
      themeConfig: {
        outline: { label: 'Sur cette page' },
        nav: [
          { text: 'À propos',      link: '/fr/about/introduction' },
          { text: 'Guide',         link: '/fr/guide/introduction' },
          { text: 'Apprentissage', link: '/fr/learning/introduction' }
        ],
        sidebar: {
          '/fr/about/':    getAboutSidebar('fr'),
          '/fr/guide/':    getGuideSidebar('fr'),
          '/fr/learning/': getLearningSidebar('fr')
        },
        docFooter: {
          prev: 'Page précédente',
          next: 'Page suivante'
        }
      }
    }
  },
  themeConfig: {
    logo: '/logo.svg',
    socialLinks: [
      { icon: 'github', link: 'https://gil/introduthub.com/tristan-greffe' },
      { icon: 'linkedin', link: 'https://www.linkedin.com/in/tristan-greffe' }
    ],
    footer: {
      copyright: 'MIT Licensed | Copyright © 2024 Tristan Greffe'
    }
  }
})

// ── About ──────────────────────────────────────────────────────────────────
function getAboutSidebar (lang) {
  if (lang === 'en') return [
    { text: 'GeoML',        link: '/about/introduction' },
    { text: 'Contributing', link: '/about/contributing' },
    { text: 'License',      link: '/about/license' }
  ]
  return [
    { text: 'GeoML',     link: '/fr/about/introduction' },
    { text: 'Contribuer', link: '/fr/about/contributing' },
    { text: 'Licence',    link: '/fr/about/license' }
  ]
}

// ── Guide ──────────────────────────────────────────────────────────────────
function getGuideSidebar (lang) {
  const p = lang === 'fr' ? '/fr' : ''
  const t = (fr, en) => lang === 'fr' ? fr : en

  return [
    { text: t('Guide', 'Guide'),                    link: `${p}/guide/introduction` },
    { text: t('Démarrage rapide', 'Getting started'), link: `${p}/guide/getting-started` },
    { text: t('Architecture', 'Architecture'),        link: `${p}/guide/architecture` },
    {
      text: t('Modèles', 'Models'),
      collapsed: true,
      items: [
        { text: t('Détection d\'arbres', 'Tree detection'), link: `${p}/guide/models/tree-detection` }
      ]
    },
    {
      text: 'Backend',
      collapsed: true,
      items: [
        { text: t('Architecture', 'Architecture'), link: `${p}/guide/backend/architecture` },
        { text: 'Endpoints',                       link: `${p}/guide/backend/endpoints` }
      ]
    },
    {
      text: 'Frontend',
      collapsed: true,
      items: [
        { text: t('Technologies', 'Technology'), link: `${p}/guide/frontend/technology` },
        { text: t('Carte & panneau', 'Map & panel'), link: `${p}/guide/frontend/map` }
      ]
    }
  ]
}

// ── Learning (FR full sidebar) ─────────────────────────────────────────────
function getLearningSidebar (lang) {
  const p = lang === 'fr' ? '/fr' : ''

  return [
    {
      text: lang === 'fr' ? 'Parcours Data Science & ML' : 'Data Science & ML Path',
      link: `${p}/learning/introduction`
    },
    {
      text: lang === 'fr' ? 'Bibliothèques' : 'Libraries',
      collapsed: true,
      items: [
        { text: 'NumPy', link: `${p}/learning/libraries/numpy/introduction` },
        {
          text: 'Pandas', collapsed: true,
          items: [
            { text: 'Introduction', link: `${p}/learning/libraries/pandas/introduction` },
            { text: 'Series', link: `${p}/learning/libraries/pandas/series` },
            { text: 'DataFrames', link: `${p}/learning/libraries/pandas/data-frames` },
            { text: lang === 'fr' ? 'Données manquantes' : 'Missing data', link: `${p}/learning/libraries/pandas/missing-data` },
            { text: 'Input & output', link: `${p}/learning/libraries/pandas/input-output` },
            { text: lang === 'fr' ? 'Mise en pratique' : 'Project', link: `${p}/learning/libraries/pandas/project` }
          ]
        },
        {
          text: 'Matplotlib', collapsed: true,
          items: [
            { text: 'Introduction', link: `${p}/learning/libraries/matplotlib/introduction` },
            { text: lang === 'fr' ? 'Programmation orientée objet' : 'Object-oriented', link: `${p}/learning/libraries/matplotlib/poo` },
            { text: lang === 'fr' ? 'Personnalisation' : 'Customization', link: `${p}/learning/libraries/matplotlib/customization` },
            { text: lang === 'fr' ? 'Mise en pratique' : 'Project', link: `${p}/learning/libraries/matplotlib/project` }
          ]
        },
        {
          text: 'Seaborn', collapsed: true,
          items: [
            { text: 'Introduction', link: `${p}/learning/libraries/seaborn/introduction` },
            { text: lang === 'fr' ? 'Dispersion' : 'Scatter plots', link: `${p}/learning/libraries/seaborn/scatter-plots` },
            { text: lang === 'fr' ? 'Distribution' : 'Distribution plots', link: `${p}/learning/libraries/seaborn/distribution-plots` },
            { text: lang === 'fr' ? 'Catégoriel' : 'Categorical plots', link: `${p}/learning/libraries/seaborn/categorical-plots` },
            { text: lang === 'fr' ? 'Comparaison' : 'Comparison plots', link: `${p}/learning/libraries/seaborn/comparison-plots` },
            { text: lang === 'fr' ? 'Matriciel' : 'Matrix plots', link: `${p}/learning/libraries/seaborn/matrix-plots` },
            { text: 'Seaborn Grids', link: `${p}/learning/libraries/seaborn/seaborn-grids` },
            { text: lang === 'fr' ? 'Mise en pratique' : 'Project', link: `${p}/learning/libraries/seaborn/project` }
          ]
        }
      ]
    },
    {
      text: 'Concepts',
      collapsed: true,
      items: [
        { text: lang === 'fr' ? 'Fondamentaux' : 'Fundamentals', link: `${p}/learning/concepts/fundamentals` },
        { text: lang === 'fr' ? 'Utilité' : 'Utility', link: `${p}/learning/concepts/utility` },
        { text: lang === 'fr' ? 'Types d\'apprentissage' : 'Learning types', link: `${p}/learning/concepts/type` },
        { text: lang === 'fr' ? 'Processus supervisé' : 'Supervised process', link: `${p}/learning/concepts/process` }
      ]
    },
    {
      text: lang === 'fr' ? 'Algorithmes supervisés' : 'Supervised algorithms',
      collapsed: true,
      items: [
        { text: 'Introduction', link: `${p}/learning/algorithms/introduction` },
        { text: lang === 'fr' ? 'Régression linéaire' : 'Linear regression', collapsed: true,
          items: [{ text: 'Introduction', link: `${p}/learning/algorithms/linear-regression/introduction` }] },
        { text: lang === 'fr' ? 'Régression logistique' : 'Logistic regression', collapsed: true,
          items: [{ text: 'Introduction', link: `${p}/learning/algorithms/logistic-regression/introduction` }] },
        { text: 'KNN', collapsed: true,
          items: [{ text: 'Introduction', link: `${p}/learning/algorithms/knn/introduction` }] },
        { text: 'SVM', collapsed: true,
          items: [{ text: 'Introduction', link: `${p}/learning/algorithms/svm/introduction` }] },
        { text: lang === 'fr' ? 'Arbre de décision' : 'Decision tree', collapsed: true,
          items: [{ text: 'Introduction', link: `${p}/learning/algorithms/decision-tree/introduction` }] },
        { text: 'Random Forest', collapsed: true,
          items: [{ text: 'Introduction', link: `${p}/learning/algorithms/random-forest/introduction` }] },
        { text: lang === 'fr' ? 'Boosting' : 'Boosting methods', collapsed: true,
          items: [{ text: 'Introduction', link: `${p}/learning/algorithms/boosting/introduction` }] }
      ]
    },
    {
      text: 'Deep Learning',
      collapsed: true,
      items: [
        { text: 'Introduction', link: `${p}/learning/deep-learning/introduction` },
        { text: lang === 'fr' ? 'Réseaux convolutifs (CNN)' : 'Convolutional networks (CNN)', link: `${p}/learning/deep-learning/cnn` },
        { text: lang === 'fr' ? 'Segmentation sémantique' : 'Semantic segmentation', link: `${p}/learning/deep-learning/segmentation` },
        { text: 'U-Net', link: `${p}/learning/deep-learning/unet` }
      ]
    },
    {
      text: lang === 'fr' ? 'Ressources' : 'Resources',
      link: `${p}/learning/resources/introduction`
    }
  ]
}
