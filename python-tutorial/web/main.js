// Main application entry point

import { pyodide } from './core/pyodide-manager.js';
import { moduleLoader } from './core/module-loader.js';
import { progress } from './core/progress.js';
import { loadExercise } from './core/exercise-loader.js';
import { modules } from './config/modules.js';

// State
let currentView = 'home';
let currentModule = null;
let currentExercise = null;
let editor = null;
let scratchpadEditor = null;
let exerciseData = null;

// DOM Elements
const elements = {
  viewHome: document.getElementById('view-home'),
  viewModule: document.getElementById('view-module'),
  viewExercise: document.getElementById('view-exercise'),
  moduleGrid: document.getElementById('module-grid'),
  exerciseList: document.getElementById('exercise-list'),
  loadingOverlay: document.getElementById('loading-overlay'),
  loadingMessage: document.getElementById('loading-message'),
  loadingProgress: document.querySelector('#loading-progress .progress-fill'),
  warningModal: document.getElementById('warning-modal'),
  warningMessage: document.getElementById('warning-message'),
  pyodideStatus: document.getElementById('pyodide-status'),
  navBreadcrumb: document.getElementById('nav-breadcrumb'),
  sidebar: document.getElementById('sidebar'),
  overallProgress: document.getElementById('overall-progress'),
};

// Initialize app
async function init() {
  console.log('Initializing Python Tutorial...');

  // Setup navigation
  setupNavigation();

  // Render initial view
  renderHome();

  // Initialize Pyodide in background
  initPyodide();
}

// Setup click handlers for navigation
function setupNavigation() {
  // Home link
  document.querySelector('.nav-brand').addEventListener('click', (e) => {
    e.preventDefault();
    navigateTo('home');
  });

  // Warning modal buttons
  document.getElementById('warning-cancel').addEventListener('click', () => {
    elements.warningModal.classList.add('hidden');
    window.warningResolve?.(false);
  });

  document.getElementById('warning-confirm').addEventListener('click', () => {
    elements.warningModal.classList.add('hidden');
    window.warningResolve?.(true);
  });

  // Handle browser back/forward
  window.addEventListener('popstate', (e) => {
    if (e.state) {
      if (e.state.view === 'home') {
        showView('home');
      } else if (e.state.view === 'module') {
        showModule(e.state.moduleId, false);
      } else if (e.state.view === 'exercise') {
        showExercise(e.state.moduleId, e.state.exerciseNum, false);
      }
    }
  });
}

// Initialize Pyodide runtime
async function initPyodide() {
  const statusDot = elements.pyodideStatus.querySelector('.status-dot');
  const statusText = elements.pyodideStatus.querySelector('.status-text');

  try {
    await pyodide.init();
    statusDot.classList.add('ready');
    statusText.textContent = 'Python ready';

    // Preload numpy in background if user is idle
    setTimeout(() => {
      if ('requestIdleCallback' in window) {
        requestIdleCallback(() => {
          moduleLoader.queuePreload('05_numpy');
        });
      }
    }, 2000);
  } catch (err) {
    statusDot.classList.add('error');
    statusText.textContent = 'Python failed to load';
    console.error('Pyodide init error:', err);
  }
}

// Navigation
function navigateTo(view, params = {}) {
  if (view === 'home') {
    showView('home');
    history.pushState({ view: 'home' }, '', '#');
  } else if (view === 'module') {
    showModule(params.moduleId);
    history.pushState({ view: 'module', moduleId: params.moduleId }, '', `#${params.moduleId}`);
  } else if (view === 'exercise') {
    showExercise(params.moduleId, params.exerciseNum);
    history.pushState(
      { view: 'exercise', moduleId: params.moduleId, exerciseNum: params.exerciseNum },
      '',
      `#${params.moduleId}/${params.exerciseNum}`
    );
  }
}

// Show view
function showView(view) {
  currentView = view;
  elements.viewHome.classList.toggle('hidden', view !== 'home');
  elements.viewModule.classList.toggle('hidden', view !== 'module');
  elements.viewExercise.classList.toggle('hidden', view !== 'exercise');

  if (view === 'home') {
    elements.navBreadcrumb.innerHTML = '';
    renderHome();
  }
}

// Render home page
function renderHome() {

  // Render overall progress
  const stats = progress.getStats();
  elements.overallProgress.innerHTML = `
    <span>${stats.completedExercises} / ${stats.totalExercises} exercises</span>
    <div class="progress-bar">
      <div class="progress-fill" style="width: ${stats.percentComplete}%"></div>
    </div>
    <span>${stats.percentComplete}%</span>
  `;

  // Render module grid
  const modulesInfo = moduleLoader.getAllModulesInfo();
  elements.moduleGrid.innerHTML = modulesInfo.map((mod, idx) => {
    const moduleProgress = progress.getModuleProgress(mod.id);
    const loadFlag = mod.flag.label && !mod.packagesLoaded
      ? `<span class="load-flag" style="background: ${mod.flag.color}">${mod.flag.label}</span>`
      : mod.packagesLoaded && mod.packages.length > 0
        ? '<span class="loaded-flag">loaded</span>'
        : '';

    return `
      <div class="module-card" data-module="${mod.id}">
        <div class="module-number">${idx + 1}</div>
        <h2>${mod.title}</h2>
        <div class="module-info">
          ${mod.exercises} exercises ${loadFlag}
        </div>
        <div class="module-progress">
          <div class="progress-bar">
            <div class="progress-fill" style="width: ${moduleProgress}%"></div>
          </div>
        </div>
      </div>
    `;
  }).join('');

  // Add click handlers
  elements.moduleGrid.querySelectorAll('.module-card').forEach(card => {
    card.addEventListener('click', () => {
      const moduleId = card.dataset.module;
      navigateTo('module', { moduleId });
    });
  });
}

// Show module view
async function showModule(moduleId, pushState = true) {
  currentModule = moduleId;
  const moduleInfo = moduleLoader.getModuleInfo(moduleId);

  if (!moduleInfo) {
    console.error('Module not found:', moduleId);
    return;
  }

  // Check if we need to load packages
  if (moduleInfo.showWarning) {
    const confirmed = await showWarningModal(moduleInfo.warningMessage);
    if (!confirmed) return;
  }

  // Load packages if needed
  if (moduleInfo.packages.length > 0 && !moduleInfo.packagesLoaded) {
    showLoading('Loading Python packages...', moduleInfo.estimatedLoadMs);
    await moduleLoader.loadModule(moduleId, {
      onProgress: (p) => {
        if (p.message) {
          elements.loadingMessage.textContent = p.message;
        }
      }
    });
    hideLoading();
  }

  showView('module');

  // Update breadcrumb
  elements.navBreadcrumb.innerHTML = `${moduleInfo.title}`;

  // Update header
  document.getElementById('module-title').textContent = moduleInfo.title;
  document.getElementById('module-subtitle').textContent = `${moduleInfo.exercises} exercises`;

  // Render exercise list
  const moduleProgressData = progress.getModule(moduleId);
  const exerciseCards = [];

  for (let i = 1; i <= moduleInfo.exercises; i++) {
    const isCompleted = moduleProgressData.completed?.includes(i);
    const exercise = await loadExercise(moduleId, i);
    const title = exercise?.title || `Exercise ${i}`;

    exerciseCards.push(`
      <div class="exercise-card ${isCompleted ? 'completed' : ''}" data-exercise="${i}">
        <div class="exercise-num">${i}</div>
        <span class="exercise-title">${title}</span>
        ${isCompleted ? '<span class="exercise-check">&#10003;</span>' : ''}
      </div>
    `);
  }

  elements.exerciseList.innerHTML = exerciseCards.join('');

  // Add click handlers
  elements.exerciseList.querySelectorAll('.exercise-card').forEach(card => {
    card.addEventListener('click', () => {
      const exerciseNum = parseInt(card.dataset.exercise);
      navigateTo('exercise', { moduleId, exerciseNum });
    });
  });

  if (pushState) {
    history.pushState({ view: 'module', moduleId }, '', `#${moduleId}`);
  }
}

// Show exercise view
async function showExercise(moduleId, exerciseNum, pushState = true) {
  currentModule = moduleId;
  currentExercise = exerciseNum;

  const moduleInfo = moduleLoader.getModuleInfo(moduleId);

  // Load packages if needed
  if (moduleInfo.packages.length > 0 && !moduleInfo.packagesLoaded) {
    showLoading('Loading Python packages...', moduleInfo.estimatedLoadMs);
    await moduleLoader.loadModule(moduleId);
    hideLoading();
  }

  // Load exercise data
  showLoading('Loading exercise...');
  exerciseData = await loadExercise(moduleId, exerciseNum);
  hideLoading();

  if (!exerciseData) {
    console.error('Exercise not found:', moduleId, exerciseNum);
    return;
  }

  showView('exercise');

  // Update breadcrumb
  elements.navBreadcrumb.innerHTML = `
    <a data-nav="module" data-module="${moduleId}">${moduleInfo.title}</a>
    <span class="separator">/</span>
    Exercise ${exerciseNum}
  `;

  elements.navBreadcrumb.querySelector('[data-nav="module"]').addEventListener('click', () => {
    navigateTo('module', { moduleId });
  });

  // Update exercise header
  document.getElementById('exercise-title').textContent =
    `Exercise ${exerciseNum}: ${exerciseData.title}`;

  // Navigation buttons
  const navHtml = [];
  if (exerciseNum > 1) {
    navHtml.push(`<button class="btn btn-nav" data-nav="prev">&larr; Previous</button>`);
  }
  if (exerciseNum < moduleInfo.exercises) {
    navHtml.push(`<button class="btn btn-nav" data-nav="next">Next &rarr;</button>`);
  }
  document.getElementById('exercise-nav').innerHTML = navHtml.join('');

  document.querySelectorAll('[data-nav="prev"]').forEach(btn => {
    btn.addEventListener('click', () => {
      navigateTo('exercise', { moduleId, exerciseNum: exerciseNum - 1 });
    });
  });

  document.querySelectorAll('[data-nav="next"]').forEach(btn => {
    btn.addEventListener('click', () => {
      navigateTo('exercise', { moduleId, exerciseNum: exerciseNum + 1 });
    });
  });

  // Render docstring
  document.querySelector('#docstring pre').textContent = exerciseData.docstring;

  // Render setup code
  const setupSection = document.getElementById('setup-code-section');
  if (exerciseData.setupCode) {
    document.getElementById('setup-code').textContent = exerciseData.setupCode;
    setupSection.classList.remove('hidden');
  } else {
    setupSection.classList.add('hidden');
  }

  // Render sidebar
  renderSidebar(moduleId, exerciseNum);

  // Initialize editor
  initEditor(exerciseData);

  // Initialize scratchpad (reset state for new exercise)
  const scratchpadSection = document.getElementById('scratchpad-section');
  const scratchpadBody = document.getElementById('scratchpad-body');
  scratchpadSection.classList.remove('open');
  scratchpadBody.classList.add('hidden');

  // Pre-populate scratchpad with setup code
  const scratchpadDefault = exerciseData.setupCode
    ? `# Setup code (same as exercise)\n${exerciseData.setupCode}\n\n# Try your code here\n`
    : '# Try your code here\n';
  window.currentScratchpadDefault = scratchpadDefault; // Store for lazy init

  // Reset scratchpad editor content
  if (scratchpadEditor) {
    scratchpadEditor.setValue(scratchpadDefault);
    // Refresh after a tick to handle hidden state
    setTimeout(() => scratchpadEditor.refresh(), 10);
  }
  document.getElementById('scratchpad-output').textContent = '';
  initScratchpad();

  // Hide output/result sections
  document.getElementById('output-section').classList.add('hidden');
  document.getElementById('result-section').classList.add('hidden');

  if (pushState) {
    history.pushState(
      { view: 'exercise', moduleId, exerciseNum },
      '',
      `#${moduleId}/${exerciseNum}`
    );
  }
}

// Render sidebar with exercises in current module
function renderSidebar(activeModuleId, activeExerciseNum) {
  const moduleInfo = moduleLoader.getModuleInfo(activeModuleId);
  const moduleProgress = progress.getModule(activeModuleId);

  const exerciseItems = [];
  for (let i = 1; i <= moduleInfo.exercises; i++) {
    const isActive = i === activeExerciseNum;
    const isCompleted = moduleProgress.completed?.includes(i);
    exerciseItems.push(`
      <div class="sidebar-exercise ${isActive ? 'active' : ''} ${isCompleted ? 'completed' : ''}">
        <a data-exercise="${i}">
          <span class="ex-num">${i}</span>
          ${isCompleted ? '<span class="ex-check">&#10003;</span>' : ''}
        </a>
      </div>
    `);
  }

  elements.sidebar.innerHTML = `
    <div class="sidebar-back">
      <a data-nav="modules">&larr; All Modules</a>
    </div>
    <h3>${moduleInfo.title}</h3>
    <div class="sidebar-exercises">
      ${exerciseItems.join('')}
    </div>
  `;

  // Back to modules link
  elements.sidebar.querySelector('[data-nav="modules"]').addEventListener('click', () => {
    navigateTo('module', { moduleId: activeModuleId });
  });

  // Exercise links
  elements.sidebar.querySelectorAll('[data-exercise]').forEach(link => {
    link.addEventListener('click', () => {
      const exerciseNum = parseInt(link.dataset.exercise);
      navigateTo('exercise', { moduleId: activeModuleId, exerciseNum });
    });
  });
}

// Initialize CodeMirror editor
function initEditor(exercise) {
  const textarea = document.getElementById('user-code');

  // Destroy existing editor
  if (editor) {
    editor.toTextArea();
  }

  // Get saved code or use starter
  const savedCode = progress.getCode(currentModule, currentExercise);
  textarea.value = savedCode || exercise.starterCode;

  // Create new editor
  editor = CodeMirror.fromTextArea(textarea, {
    mode: 'python',
    theme: 'xq-light',
    lineNumbers: true,
    indentUnit: 4,
    tabSize: 4,
    indentWithTabs: false,
    lineWrapping: true,
    extraKeys: {
      'Tab': (cm) => cm.replaceSelection('    ', 'end'),
      'Ctrl-Enter': () => runCode(),
      'Cmd-Enter': () => runCode(),
    }
  });

  // Auto-save on change
  let saveTimeout;
  editor.on('change', () => {
    clearTimeout(saveTimeout);
    saveTimeout = setTimeout(() => {
      progress.saveCode(currentModule, currentExercise, editor.getValue());
      document.getElementById('auto-save-indicator').textContent = 'Saved';
      setTimeout(() => {
        document.getElementById('auto-save-indicator').textContent = '';
      }, 1500);
    }, 1000);
  });

  // Setup buttons
  document.getElementById('run-btn').onclick = runCode;
  document.getElementById('reset-btn').onclick = () => {
    editor.setValue(exercise.starterCode);
    document.getElementById('output-section').classList.add('hidden');
    document.getElementById('result-section').classList.add('hidden');
  };
}

// Run and grade code
async function runCode() {
  if (!exerciseData) return;

  const runBtn = document.getElementById('run-btn');
  const outputSection = document.getElementById('output-section');
  const outputContent = document.getElementById('output-content');
  const resultSection = document.getElementById('result-section');

  // Show loading state
  runBtn.disabled = true;
  runBtn.textContent = 'Running...';
  outputSection.classList.remove('hidden');
  outputContent.textContent = 'Executing code...';
  resultSection.classList.add('hidden');

  try {
    const userCode = editor.getValue();
    const result = await pyodide.grade(
      exerciseData.setupCode,
      userCode,
      exerciseData.postUserCode,
      exerciseData.gradingCode,
      exerciseData.hint
    );

    // Show output
    outputContent.textContent = result.stdout || 'No output';

    // Show result
    resultSection.classList.remove('hidden');
    if (result.passed) {
      resultSection.innerHTML = `
        <div class="result-pass">
          All ${result.passedCount} check(s) passed!
        </div>
      `;
      // Save completion
      progress.completeExercise(currentModule, currentExercise, userCode);
    } else {
      let html = `
        <div class="result-fail">
          ${result.passedCount} passed, ${result.failedCount} failed
        </div>
      `;
      if (result.hint) {
        html += `<div class="result-hint">Hint: ${result.hint}</div>`;
      }
      resultSection.innerHTML = html;
    }
  } catch (err) {
    outputContent.textContent = 'Error: ' + err.message;
    resultSection.classList.remove('hidden');
    resultSection.innerHTML = '<div class="result-fail">Execution failed</div>';
  } finally {
    runBtn.disabled = false;
    runBtn.textContent = 'Run & Check';
  }
}

// Scratchpad functionality
let scratchpadInitialized = false;

function initScratchpad() {
  if (scratchpadInitialized) return;
  scratchpadInitialized = true;

  const toggle = document.getElementById('scratchpad-toggle');
  const body = document.getElementById('scratchpad-body');
  const section = document.getElementById('scratchpad-section');
  const textarea = document.getElementById('scratchpad-code');

  // Toggle expand/collapse
  toggle.addEventListener('click', () => {
    const isOpen = section.classList.toggle('open');
    body.classList.toggle('hidden', !isOpen);

    // Initialize CodeMirror on first open
    if (isOpen && !scratchpadEditor) {
      scratchpadEditor = CodeMirror.fromTextArea(textarea, {
        mode: 'python',
        theme: 'xq-light',
        lineNumbers: true,
        indentUnit: 4,
        tabSize: 4,
        indentWithTabs: false,
        lineWrapping: true,
        extraKeys: {
          'Tab': (cm) => cm.replaceSelection('    ', 'end'),
          'Ctrl-Enter': () => runScratchpad(),
          'Cmd-Enter': () => runScratchpad(),
        }
      });
      scratchpadEditor.setValue(window.currentScratchpadDefault || '# Try your code here\n');
    }

    // Refresh when opening (content may have been set while hidden)
    if (isOpen && scratchpadEditor) {
      setTimeout(() => scratchpadEditor.refresh(), 10);
    }
  });

  // Run button
  document.getElementById('scratchpad-run').addEventListener('click', runScratchpad);

  // Reset button - restore to default (setup code)
  document.getElementById('scratchpad-clear').addEventListener('click', () => {
    if (scratchpadEditor) {
      scratchpadEditor.setValue(window.currentScratchpadDefault || '# Try your code here\n');
    }
    document.getElementById('scratchpad-output').textContent = '';
  });
}

async function runScratchpad() {
  if (!scratchpadEditor) return;

  const output = document.getElementById('scratchpad-output');
  const code = scratchpadEditor.getValue();

  output.textContent = 'Running...';

  try {
    const result = await pyodide.runCode(code);
    let text = '';
    if (result.stdout) text += result.stdout;
    if (result.stderr) text += (text ? '\n' : '') + result.stderr;
    if (result.error) text += (text ? '\n' : '') + 'Error: ' + result.error;
    if (result.result && result.result !== 'None' && result.result !== 'undefined') {
      text += (text ? '\n=> ' : '=> ') + result.result;
    }
    output.textContent = text || 'No output';
  } catch (err) {
    output.textContent = 'Error: ' + err.message;
  }
}

// Loading overlay
function showLoading(message, estimatedMs = 0) {
  elements.loadingMessage.textContent = message;
  elements.loadingProgress.style.width = '0%';
  elements.loadingOverlay.classList.remove('hidden');

  if (estimatedMs > 0) {
    const start = Date.now();
    const interval = setInterval(() => {
      const elapsed = Date.now() - start;
      const percent = Math.min(95, (elapsed / estimatedMs) * 100);
      elements.loadingProgress.style.width = `${percent}%`;

      if (elements.loadingOverlay.classList.contains('hidden')) {
        clearInterval(interval);
      }
    }, 100);
  }
}

function hideLoading() {
  elements.loadingProgress.style.width = '100%';
  setTimeout(() => {
    elements.loadingOverlay.classList.add('hidden');
  }, 200);
}

// Warning modal
function showWarningModal(message) {
  return new Promise(resolve => {
    window.warningResolve = resolve;
    elements.warningMessage.textContent = message;
    elements.warningModal.classList.remove('hidden');
  });
}

// Handle initial URL hash
function handleInitialRoute() {
  const hash = window.location.hash.slice(1);
  if (!hash) return;

  const parts = hash.split('/');
  if (parts.length === 1) {
    // Module view
    showModule(parts[0], false);
  } else if (parts.length === 2) {
    // Exercise view
    showExercise(parts[0], parseInt(parts[1]), false);
  }
}

// Start app
init().then(() => {
  handleInitialRoute();
});
