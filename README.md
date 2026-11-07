# AI Engineer Notes

Interview-ready notes for AI engineering: explained simply first, then precisely, then in words you can say out loud, then practised.

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
| `src/data/roadmap.ts` | The learning path: subject tracks (Math, ML, DL, LLM internals, …), their sources and the list of notes with the week each belongs to. Home, roadmap, practice and note navigation are generated from it. |
| `src/data/practice.ts` | The weekly practice plan: hand problems, coding drills, project milestone and problem-set links per week. |
| `src/data/glossary.ts` | One plain sentence per technical word, with the note that teaches it. Rendered at `/glossary/`; the `Term` component links to it. |
| `src/data/numpy.ts` | The NumPy reference (`/numpy/`): every function the notes use, with a runnable example and its real output. **Generated** by `scripts/gen_numpy.py`; edit the script, not the file. `CodeBlock` turns every `np.*` call in a code block into a link here. |
| `src/pages/notes/<track>/<slug>.astro` | One file per note. Set `ready: true` for it in `roadmap.ts` to link it. Notes within a week carry an `order`, and the roadmap, the sidebar pager and the week table follow it. |
| `src/components/` | Building blocks: `Callout`, `QA`, `Figure`, `Math`, `CodeBlock`, `Source`, `Term`, `TrackNotes`, `Timeline`, plus the `Sidebar`. |
| `src/styles/global.css` | The design system. All colours, fonts and spacing are tokens at the top, with a dark set under `[data-theme='dark']`. |

## Writing rules

Notes are read in the order given on the roadmap, and a note may only use a word that an earlier note taught. If a
later word is unavoidable, wrap it: `<Term id="softmax">softmax</Term>` (ids live in `src/data/glossary.ts`). Every
section opens in plain words with small numbers before any symbol. Each note ends with a labelled, optional
“Where you will meet this again” preview rather than mixing later material into the body.

Regenerate the NumPy reference after editing the generator:

```bash
python3 scripts/gen_numpy.py src/data/numpy.ts
```

## Deploy

Import the repository in Vercel. It detects Astro and needs no configuration.
