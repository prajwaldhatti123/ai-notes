# Notes

A library of study notes, one notebook per subject. The home page (`/`) is the shelf of notebooks; each notebook lives under its own path. The first is **AI Engineer** at `/ai/`: interview-ready notes explained simply first, then precisely, then in words you can say out loud, then practised.

Built with [Astro](https://astro.build). Output is plain static HTML.

## Run locally

```bash
npm install
npm run dev      # http://localhost:4321  (Astro 7 runs it in the background; `npx astro dev stop` stops it)
npm run build    # static site in dist/
```

## Where things are

| Path | What it holds |
|---|---|
| `src/data/notebooks.ts` | The shelf on the home page. One entry per notebook; an entry without `href` shows as “coming soon”. |
| `src/pages/index.astro` | The library home. Uses `Base` with `library`, which drops the notebook sidebar. |
| `src/pages/ai/` | The AI Engineer notebook: its home, roadmap, practice, projects, glossary, NumPy reference and `notes/<track>/<slug>.astro`. |
| `src/data/roadmap.ts` | The learning path: subject tracks (Math, ML, DL, LLM internals, …), their sources and the list of notes with the week each belongs to. Home, roadmap, practice and note navigation are generated from it. |
| `src/data/practice.ts` | The weekly practice plan: hand problems, coding drills, project milestone and problem-set links per week. |
| `src/data/glossary.ts` | One plain sentence per technical word, with the note that teaches it. Rendered at `/ai/glossary/`; the `Term` component links to it. |
| `src/data/numpy.ts` | The NumPy reference (`/ai/numpy/`): every function the notes use, with a runnable example and its real output. **Generated** by `scripts/gen_numpy.py`; edit the script, not the file. `CodeBlock` turns every `np.*` call in a code block into a link here. |
| `src/data/sklearn.ts`, `src/data/pytools.ts` | The scikit-learn (`/ai/sklearn/`) and Python-tools (`/ai/python/`) references: every library name and less common Python feature the code uses, with real output (and pictures for plots). **Generated** by `scripts/gen_reference.py`. |
| `src/pages/ai/notes/<track>/<slug>.astro` | One file per note. Set `ready: true` for it in `roadmap.ts` to link it. Notes within a week carry an `order`, and the roadmap, the sidebar pager and the week table follow it. |
| `src/components/` | Building blocks: `Callout`, `QA`, `Figure`, `Math`, `CodeBlock`, `NewInCode`, `Source`, `Term`, `TrackNotes`, `Timeline`, `RefEntries`, plus the `Sidebar`. |
| `src/styles/global.css` | The design system. All colours, fonts and spacing are tokens at the top, with a dark set under `[data-theme='dark']`. |

## Writing rules

Notes are read in the order given on the roadmap, and a note may only use a word that an earlier note taught. If a
later word is unavoidable, wrap it: `<Term id="softmax">softmax</Term>` (ids live in `src/data/glossary.ts`). Every
section opens in plain words with small numbers before any symbol. Each note ends with a labelled, optional
“Where you will meet this again” preview rather than mixing later material into the body.

Code follows the same rule. It assumes plain Python only. Anything else (a NumPy or scikit-learn function, a
plot, `zip`, `lambda`, a format spec) is introduced in a `NewInCode` box right above the first block that uses it:

```astro
<NewInCode items={[
  ['np.polyfit(x, y, degree)', 'Fits the best curve of the given degree to the points.', 'numpy/polyfit'],
]} />
```

The third element is `page/id` on the NumPy, scikit-learn, Python-tools or glossary page; a wrong id fails the
build. Write one step per line, no semicolons, no renamed imports, no function calls inside f-string braces, and
put the real output in comments.

Regenerate the references after editing a generator:

```bash
python3 scripts/gen_numpy.py src/data/numpy.ts
python scripts/gen_reference.py      # needs scikit-learn, pandas and matplotlib installed
```

## Adding a notebook

1. Put its pages under `src/pages/<id>/` (for example `src/pages/frontend/index.astro`).
2. Add or update its entry in `src/data/notebooks.ts` and give it `href: '/<id>/'`.

The shared design (fonts, colours, callouts, code blocks, dark mode) works in every notebook.

## Deploy

Import the repository in Vercel. It detects Astro and needs no configuration. `vercel.json` redirects the old
top-level AI paths (`/notes/…`, `/roadmap/`, …) to their new home under `/ai/`.
