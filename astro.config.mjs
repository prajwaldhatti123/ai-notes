import { defineConfig } from 'astro/config';

export default defineConfig({
  // Compression drops the space when a line break sits right before an inline tag,
  // which glues words together in prose ("the<span>bias</span>").
  compressHTML: false,
});
