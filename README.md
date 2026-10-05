# AI Engineer Notes

Interview-ready notes for AI engineering: explained simply first, then precisely, then in words you can say out loud.

Built with [Astro](https://astro.build). Output is plain static HTML.

## Run locally

```bash
npm install
npm run dev      # http://localhost:4321
npm run build    # static site in dist/
```

## Where things are

| Path | What it holds |
|---|---|
| `src/data/roadmap.ts` | The learning path: phases, sources and the list of notes. Home, roadmap and note navigation are generated from it. |
| `src/pages/notes/<phase>/<slug>.astro` | One file per note. Set `ready: true` for it in `roadmap.ts` to link it. |
| `src/components/` | Building blocks: `Callout`, `QA`, `Figure`, `Math`. |
| `src/styles/global.css` | The design system. All colours, fonts and spacing are tokens at the top. |
| `/style-guide/` | Live reference for every block and the writing rules. |

## Deploy

Import the repository in Vercel. It detects Astro and needs no configuration.
