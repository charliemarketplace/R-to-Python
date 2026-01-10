// Module configuration for Python tutorial

export const modules = {
  '01_fundamentals': {
    title: 'Python Fundamentals',
    packages: [],
    loadTimeFlag: 'fast',
    estimatedLoadMs: 0,
    preloadAfter: null,
    exercises: 8,
  },

  '02_control_flow': {
    title: 'Control Flow & Loops',
    packages: [],
    loadTimeFlag: 'fast',
    estimatedLoadMs: 0,
    preloadAfter: '01_fundamentals',
    exercises: 10,
  },

  '03_functions': {
    title: 'Functions & Scope',
    packages: [],
    loadTimeFlag: 'fast',
    estimatedLoadMs: 0,
    preloadAfter: '02_control_flow',
    exercises: 8,
  },

  '04_data_structures': {
    title: 'Data Structures',
    packages: [],
    loadTimeFlag: 'fast',
    estimatedLoadMs: 0,
    preloadAfter: '03_functions',
    exercises: 10,
  },

  '05_numpy': {
    title: 'NumPy Essentials',
    packages: ['numpy'],
    loadTimeFlag: 'medium',
    estimatedLoadMs: 2500,
    preloadAfter: '04_data_structures',
    exercises: 10,
  },

  '06_pandas': {
    title: 'Pandas - Tidyverse Translation',
    packages: ['numpy', 'pandas'],
    loadTimeFlag: 'medium',
    estimatedLoadMs: 3000,
    preloadAfter: '05_numpy',
    exercises: 12,
  },

  '07_polars': {
    title: 'Polars - Modern Alternative',
    packages: ['polars'],
    loadTimeFlag: 'slow',
    estimatedLoadMs: 10000,
    preloadAfter: null,
    warningMessage: 'Polars is a large package (~15MB). First load may take 10-15 seconds.',
    exercises: 10,
  },

  '08_stats': {
    title: 'Statistical Modeling',
    packages: ['numpy', 'pandas', 'scipy', 'statsmodels'],
    loadTimeFlag: 'slow',
    estimatedLoadMs: 8000,
    preloadAfter: '06_pandas',
    warningMessage: 'Loading statistical libraries. This may take a moment.',
    exercises: 10,
  },

  '09_plotly': {
    title: 'Data Visualization',
    packages: ['numpy', 'pandas'],
    loadTimeFlag: 'medium',
    estimatedLoadMs: 1000,
    preloadAfter: '08_stats',
    exercises: 8,
    additionalScripts: ['https://cdn.plot.ly/plotly-2.27.0.min.js'],
  },

  '10_capstone': {
    title: 'Capstone Project',
    packages: ['numpy', 'pandas', 'scipy', 'statsmodels'],
    loadTimeFlag: 'fast',
    estimatedLoadMs: 500,
    preloadAfter: '09_plotly',
    exercises: 7,
  },
};

export const loadTimeFlags = {
  fast: {
    label: null,
    color: null,
    showLoader: false,
  },
  medium: {
    label: '~3s load',
    color: '#f59e0b',
    showLoader: true,
    loaderMessage: 'Loading Python packages...',
  },
  slow: {
    label: '~10s load',
    color: '#ef4444',
    showLoader: true,
    loaderMessage: null,
    showWarningBeforeNav: true,
  },
};
