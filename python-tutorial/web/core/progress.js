// Progress storage using localStorage

import { modules } from '../config/modules.js';

const STORAGE_KEY = 'python_tutorial_progress';

export const progress = {
  /**
   * Get all progress data.
   */
  getAll() {
    try {
      return JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}');
    } catch {
      return {};
    }
  },

  /**
   * Get progress for a specific module.
   */
  getModule(moduleId) {
    const all = this.getAll();
    return all[moduleId] || { completed: [], code: {} };
  },

  /**
   * Mark an exercise as complete.
   */
  completeExercise(moduleId, exerciseNum, userCode = null) {
    const all = this.getAll();

    if (!all[moduleId]) {
      all[moduleId] = { completed: [], code: {} };
    }

    if (!all[moduleId].completed.includes(exerciseNum)) {
      all[moduleId].completed.push(exerciseNum);
    }

    if (userCode) {
      all[moduleId].code = all[moduleId].code || {};
      all[moduleId].code[exerciseNum] = userCode;
    }

    all[moduleId].lastActivity = Date.now();

    localStorage.setItem(STORAGE_KEY, JSON.stringify(all));
  },

  /**
   * Save code snapshot (for resuming later).
   */
  saveCode(moduleId, exerciseNum, code) {
    const all = this.getAll();

    if (!all[moduleId]) {
      all[moduleId] = { completed: [], code: {} };
    }

    all[moduleId].code = all[moduleId].code || {};
    all[moduleId].code[exerciseNum] = code;

    localStorage.setItem(STORAGE_KEY, JSON.stringify(all));
  },

  /**
   * Get saved code for an exercise.
   */
  getCode(moduleId, exerciseNum) {
    const module = this.getModule(moduleId);
    return module.code?.[exerciseNum] || null;
  },

  /**
   * Check if an exercise is completed.
   */
  isCompleted(moduleId, exerciseNum) {
    const module = this.getModule(moduleId);
    return module.completed?.includes(exerciseNum) || false;
  },

  /**
   * Get overall completion stats.
   */
  getStats() {
    const all = this.getAll();
    let totalExercises = 0;
    let completedExercises = 0;
    let modulesStarted = 0;
    let modulesCompleted = 0;

    for (const [moduleId, moduleConfig] of Object.entries(modules)) {
      totalExercises += moduleConfig.exercises;
      const moduleProgress = all[moduleId];

      if (moduleProgress?.completed?.length > 0) {
        modulesStarted++;
        completedExercises += moduleProgress.completed.length;

        if (moduleProgress.completed.length >= moduleConfig.exercises) {
          modulesCompleted++;
        }
      }
    }

    return {
      totalExercises,
      completedExercises,
      modulesStarted,
      modulesCompleted,
      totalModules: Object.keys(modules).length,
      percentComplete: totalExercises > 0
        ? Math.round((completedExercises / totalExercises) * 100)
        : 0,
    };
  },

  /**
   * Get module completion percentage.
   */
  getModuleProgress(moduleId) {
    const moduleConfig = modules[moduleId];
    if (!moduleConfig) return 0;

    const moduleData = this.getModule(moduleId);
    const completed = moduleData.completed?.length || 0;
    return Math.round((completed / moduleConfig.exercises) * 100);
  },

  /**
   * Reset all progress.
   */
  reset() {
    localStorage.removeItem(STORAGE_KEY);
  },

  /**
   * Export progress as JSON string.
   */
  export() {
    return JSON.stringify(this.getAll(), null, 2);
  },

  /**
   * Import progress from JSON string.
   */
  import(jsonString) {
    try {
      const data = JSON.parse(jsonString);
      localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
      return true;
    } catch {
      return false;
    }
  },
};
