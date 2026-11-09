// Shared shape of the generated reference pages (scikit-learn, Python tools).
// NumPy has its own older file with the same fields, minus `taught` and `image`.

export interface RefGroup { id: string; title: string; intro: string }

export interface RefEntry {
  group: string;
  /** Anchor id on the reference page; CodeBlock links code to it. */
  id: string;
  name: string;
  plain: string;
  sig: string;
  code: string;
  output: string;
  pitfalls: string[];
  interview: string;
  doc: string;
  /** "track/slug" of the note that teaches the idea behind it, if any. */
  taught: string;
  /** Path of a picture the example draws (plotting entries). */
  image: string;
}
