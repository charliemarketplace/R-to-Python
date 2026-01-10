// ModuleLoader - handles loading modules and their packages

import { pyodide } from './pyodide-manager.js';
import { modules, loadTimeFlags } from '../config/modules.js';

class ModuleLoader {
  constructor() {
    this.currentModule = null;
    this.preloadQueue = [];
    this.preloading = false;
  }

  /**
   * Get module config with computed load time.
   */
  getModuleInfo(moduleId) {
    const module = modules[moduleId];
    if (!module) return null;

    const packagesLoaded = pyodide.hasPackages(module.packages);
    const flag = loadTimeFlags[module.loadTimeFlag];

    return {
      ...module,
      id: moduleId,
      packagesLoaded,
      actualLoadTime: packagesLoaded ? 0 : module.estimatedLoadMs,
      flag,
      showWarning: flag.showWarningBeforeNav && !packagesLoaded,
    };
  }

  /**
   * Get all modules info.
   */
  getAllModulesInfo() {
    return Object.keys(modules).map(id => this.getModuleInfo(id));
  }

  /**
   * Load a module's packages. Shows loading UI.
   */
  async loadModule(moduleId, { onProgress, onWarningConfirm } = {}) {
    const info = this.getModuleInfo(moduleId);
    if (!info) throw new Error(`Unknown module: ${moduleId}`);

    // Show warning for slow modules
    if (info.showWarning && onWarningConfirm) {
      const confirmed = await onWarningConfirm(info.warningMessage);
      if (!confirmed) return { cancelled: true };
    }

    // Load packages
    if (info.packages.length > 0 && !info.packagesLoaded) {
      await pyodide.ensurePackages(info.packages, onProgress);
    }

    // Load additional scripts (e.g., plotly.js)
    if (info.additionalScripts) {
      await this.loadScripts(info.additionalScripts);
    }

    this.currentModule = moduleId;

    // Queue preload for next module
    const nextModule = this.getNextModule(moduleId);
    if (nextModule) {
      this.queuePreload(nextModule);
    }

    return { cancelled: false, module: info };
  }

  /**
   * Preload packages in background during idle time.
   */
  queuePreload(moduleId) {
    if (!moduleId || this.preloadQueue.includes(moduleId)) return;

    this.preloadQueue.push(moduleId);
    this.processPreloadQueue();
  }

  async processPreloadQueue() {
    if (this.preloading || this.preloadQueue.length === 0) return;

    this.preloading = true;

    while (this.preloadQueue.length > 0) {
      const moduleId = this.preloadQueue.shift();
      const info = this.getModuleInfo(moduleId);

      if (info && !info.packagesLoaded && info.packages.length > 0) {
        // Use requestIdleCallback for non-blocking load
        await new Promise(resolve => {
          const load = async () => {
            try {
              await pyodide.ensurePackages(info.packages);
            } catch (e) {
              console.warn(`Preload failed for ${moduleId}:`, e);
            }
            resolve();
          };

          if ('requestIdleCallback' in window) {
            requestIdleCallback(load, { timeout: 5000 });
          } else {
            setTimeout(load, 100);
          }
        });
      }
    }

    this.preloading = false;
  }

  getNextModule(currentId) {
    const ids = Object.keys(modules);
    const idx = ids.indexOf(currentId);
    return idx >= 0 && idx < ids.length - 1 ? ids[idx + 1] : null;
  }

  getPrevModule(currentId) {
    const ids = Object.keys(modules);
    const idx = ids.indexOf(currentId);
    return idx > 0 ? ids[idx - 1] : null;
  }

  async loadScripts(urls) {
    const promises = urls.map(url => {
      if (document.querySelector(`script[src="${url}"]`)) {
        return Promise.resolve();
      }
      return new Promise((resolve, reject) => {
        const script = document.createElement('script');
        script.src = url;
        script.onload = resolve;
        script.onerror = reject;
        document.head.appendChild(script);
      });
    });
    await Promise.all(promises);
  }
}

export const moduleLoader = new ModuleLoader();
