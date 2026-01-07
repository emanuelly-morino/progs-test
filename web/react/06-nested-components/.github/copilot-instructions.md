# Copilot instructions for this repo

This repository is a minimal React + TypeScript + Vite app. The guidance below helps an AI coding agent work productively and safely in this codebase.

Project snapshot
- Build system: Vite with `@vitejs/plugin-react` (see `vite.config.ts`).
- Scripts: `dev` (vite), `build` (`tsc -b && vite build`), `preview`, `lint` (see `package.json`).
- Entry: `src/main.tsx` -> `src/App.tsx`. Components live in `src/components/`.

Key conventions and patterns
- Components: filenames and component names must start with a capital letter. Example: `src/components/Post.jsx` is imported as `import Post from './components/Post';` in `App.tsx`.
- Exports: components use default exports (see `Post.jsx` and `App.tsx`). Prefer default exports for UI components unless a reason exists.
- File extensions: the project mixes `.tsx` and `.jsx`. When adding TypeScript components, use `.tsx` and import with the explicit extension when other files do so (e.g., `import App from './App.tsx'` in `main.tsx`).
- Type checking: build runs `tsc -b` before `vite build` — ensure `tsconfig.app.json` and `tsconfig.node.json` remain correct when changing TS project layout.

Build, run, lint, debug
- Start dev server with `npm run dev`. Vite provides HMR/Fast Refresh via `@vitejs/plugin-react`.
- Full build: `npm run build` (runs `tsc -b` then `vite build`).
- Preview production build: `npm run preview`.
- Lint: `npm run lint` uses the repository's ESLint configuration (see `eslint.config.js` if present).

Project-specific gotchas
- Mixing JS and TS: there is an instance of `src/components/Post.jsx` (JS) while most app files are TSX. When converting or adding files, ensure imports and tsconfig references are consistent.
- Explicit extension imports: `src/main.tsx` imports `./App.tsx` with extension — follow existing import styles to avoid resolver surprises.
- Type-aware linting is not strictly enforced by default; the README suggests enabling `tseslint.configs.recommendedTypeChecked` if you add type-checked ESLint rules. Changes to lint rules should include updates to `tsconfig.app.json` and `tsconfig.node.json` where necessary.

Where to look when making changes
- `package.json` — scripts and dependencies.
- `vite.config.ts` — plugin/react config for HMR.
- `src/main.tsx`, `src/App.tsx`, `src/components/*` — component patterns and imports.
- `README.md` — notes on ESLint/TypeScript configuration.
- `tsconfig.app.json` and `tsconfig.node.json` — build and type-check boundaries.

Examples
- Add a new TypeScript component:
```
// src/components/MyWidget.tsx
import React from 'react'

export default function MyWidget(){
  return <div>My widget</div>
}
```
Import in `App.tsx` as `import MyWidget from './components/MyWidget';` (match existing import style).

Agent behavior expectations
- Run local dev (`npm run dev`) before proposing UI changes to confirm HMR behavior.
- Do not change global build scripts without updating `tsconfig` and `README.md` accordingly.
- If converting files from `.jsx` to `.tsx`, update `tsconfig` and ensure type-check passes (`tsc -b`).

Limitations discovered
- No test runner configured — do not assume unit tests exist.
- No CI config found for this repository — exercise caution when altering build steps.

If anything here is unclear or missing, ask the maintainer for the intended TypeScript linting/typing policy and whether `.jsx` files should be migrated to `.tsx`.
