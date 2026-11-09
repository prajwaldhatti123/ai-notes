// The shelf on the home page. One entry per notebook.
// A notebook with `href` is live; without one it shows as "coming soon".
// To add a notebook: put its pages under src/pages/<id>/ and add an entry here.

import { totalNotes, totalWeeks, tracks } from './roadmap';

export interface Notebook {
  id: string;
  title: string;
  blurb: string;
  /** Short facts shown at the bottom of the card. */
  meta: string;
  href?: string;
  /** Colour of the card's spine, as a CSS colour or variable. */
  spine: string;
}

const aiReady = tracks.flatMap((t) => t.notes).filter((n) => n.ready).length;

export const notebooks: Notebook[] = [
  {
    id: 'ai',
    title: 'AI Engineer',
    blurb:
      'Interview prep for AI engineer and Gen AI roles, from “what is a vector?” to designing LLM systems. Math, ML, deep learning and LLMs side by side, each idea explained plainly first.',
    meta: `${totalWeeks} weeks · ${aiReady} of ${totalNotes} notes written`,
    href: '/ai/',
    spine: 'var(--red)',
  },
  {
    id: 'frontend',
    title: 'Frontend',
    blurb: 'JavaScript, TypeScript and React for frontend interviews, with one small production-grade project a day.',
    meta: 'Coming soon',
    spine: 'var(--blue)',
  },
  {
    id: 'system-design',
    title: 'System Design',
    blurb: 'How to design large systems in an interview: the building blocks, the trade-offs and the classic questions.',
    meta: 'Coming soon',
    spine: 'var(--green)',
  },
];
