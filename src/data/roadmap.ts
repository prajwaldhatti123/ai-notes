// Single source of truth for the learning path. The home page, the roadmap page,
// the practice page and the note navigation are all generated from this file.
//
// The path is organised in subject tracks (Math, ML, DL, then the LLM tracks).
// Math and ML run in parallel during weeks 1–4; every note carries the week it
// belongs to so the roadmap can show both tracks side by side.

export interface Note {
  slug: string;
  title: string;
  week: number;
  ready?: boolean;
}

export interface Track {
  id: string;
  number: number;
  title: string;
  short: string;
  weeks: string;
  goal: string;
  scope: string;
  sources: string[];
  project?: string;
  notes: Note[];
}

export const totalWeeks = 16;

export const tracks: Track[] = [
  {
    id: 'math',
    number: 1,
    title: 'Math for AI interviews',
    short: 'Math',
    weeks: 'Weeks 1–4, alongside ML',
    goal: 'Read any formula in these notes without fear, and do the small calculations interviewers ask for by hand.',
    scope:
      'Only the math that AI engineer interviews ask or that a later note needs: vectors, matrices, slopes, the chain rule, probability and entropy. No proofs, no integrals, no theory for its own sake. The last note lists what you may skip.',
    sources: [
      '3Blue1Brown, “Essence of linear algebra” and “Essence of calculus” (YouTube)',
      'Khan Academy: linear algebra, differential calculus, statistics and probability (for practice problems)',
      'Deisenroth, Faisal and Ong, Mathematics for Machine Learning (free PDF), chapters 2–6, selected sections',
      'Seeing Theory (Brown University), a visual introduction to probability',
    ],
    notes: [
      { slug: 'functions-exponents-logs', title: 'Functions, exponents and logarithms', week: 1, ready: true },
      { slug: 'vectors-dot-product', title: 'Vectors and the dot product', week: 1, ready: true },
      { slug: 'matrices-and-shapes', title: 'Matrices, matrix multiplication and shapes', week: 1, ready: true },
      { slug: 'norms-distance-cosine', title: 'Norms, distance and cosine similarity', week: 1, ready: true },
      { slug: 'derivatives', title: 'Derivatives: slope and rate of change', week: 2 },
      { slug: 'partial-derivatives-gradient', title: 'Partial derivatives and the gradient', week: 2 },
      { slug: 'chain-rule', title: 'The chain rule', week: 2 },
      { slug: 'descriptive-statistics', title: 'Mean, median, variance and standard deviation', week: 3 },
      { slug: 'probability-bayes', title: 'Probability, conditional probability and Bayes’ theorem', week: 3 },
      { slug: 'distributions-expectation', title: 'Distributions, expectation and the normal distribution', week: 3 },
      { slug: 'maximum-likelihood', title: 'Maximum likelihood: where loss functions come from', week: 3 },
      { slug: 'entropy-cross-entropy-kl', title: 'Entropy, cross-entropy and KL divergence', week: 4 },
      { slug: 'eigen-svd-intuition', title: 'Eigenvectors and SVD, only as much as PCA and LoRA need', week: 4 },
      { slug: 'math-you-can-skip', title: 'Math you can skip, and what to say if it comes up', week: 4 },
    ],
  },
  {
    id: 'ml',
    number: 2,
    title: 'Classical machine learning',
    short: 'ML',
    weeks: 'Weeks 1–4, alongside Math',
    goal: 'Explain how a model learns from data, train and evaluate one properly, and name the right algorithm for a problem.',
    scope:
      'The algorithms and habits interviews actually test: regression, classification, loss, gradient descent, overfitting, regularization, metrics, data splits, plus kNN, k-means, PCA and tree models at the depth they are asked. Each ML note is paired with the math note it needs.',
    sources: [
      'Andrew Ng, Machine Learning Specialization (Coursera), courses 1–2, watched at 1.5x',
      'StatQuest with Josh Starmer (YouTube), one video per algorithm',
      'Raschka, Machine Learning with PyTorch and Scikit-Learn, chapters 2–6 and 10',
      'James, Witten, Hastie and Tibshirani, An Introduction to Statistical Learning (free PDF), chapters 2–5',
      'Google, Machine Learning Crash Course (for quick checks)',
    ],
    project: 'Project 0: an ML library from scratch, plus a tabular case study',
    notes: [
      { slug: 'what-is-machine-learning', title: 'What machine learning is: data, model, loss, optimizer', week: 1, ready: true },
      { slug: 'linear-regression', title: 'Linear regression', week: 1, ready: true },
      { slug: 'feature-scaling-encoding', title: 'Feature scaling, normalization and encoding', week: 1, ready: true },
      { slug: 'loss-functions', title: 'Loss functions: MSE, MAE and log loss', week: 2 },
      { slug: 'gradient-descent', title: 'Gradient descent: batch, stochastic and mini-batch', week: 2 },
      { slug: 'overfitting-bias-variance', title: 'Overfitting, underfitting and the bias–variance trade-off', week: 2 },
      { slug: 'logistic-regression', title: 'Logistic regression and the sigmoid', week: 3 },
      { slug: 'classification-metrics', title: 'Evaluation metrics: accuracy, precision, recall, F1, ROC-AUC', week: 3 },
      { slug: 'data-splits-cross-validation', title: 'Train, validation, test and cross-validation', week: 3 },
      { slug: 'regularization', title: 'Regularization: L1, L2 and early stopping', week: 3 },
      { slug: 'knn-kmeans', title: 'kNN and k-means: learning from similarity', week: 4 },
      { slug: 'pca', title: 'PCA and dimensionality reduction', week: 4 },
      { slug: 'trees-forests-boosting', title: 'Decision trees, random forests and gradient boosting', week: 4 },
      { slug: 'svm-naive-bayes', title: 'SVM and Naive Bayes at interview depth', week: 4 },
      { slug: 'imbalance-leakage', title: 'Class imbalance, data leakage and other traps', week: 4 },
    ],
  },
  {
    id: 'dl',
    number: 3,
    title: 'Deep learning foundations',
    short: 'DL',
    weeks: 'Weeks 5–6',
    goal: 'Understand how any neural network learns, build one in NumPy, then write a PyTorch training loop from memory.',
    scope:
      'Neurons to networks, backpropagation, optimizers, softmax, PyTorch, the regularization tricks specific to deep nets, and a short bridge through CNNs and RNNs to attention. Computer vision and speech architectures are covered only as far as interviews ask.',
    sources: [
      '3Blue1Brown, “Neural Networks” series (chapters 1–4)',
      'Andrej Karpathy, “Zero to Hero”: the micrograd video',
      'Michael Nielsen, Neural Networks and Deep Learning (free online), chapters 1–3',
      'Raschka, Build a Large Language Model (From Scratch), Appendix A: Introduction to PyTorch',
    ],
    project: 'Project 0 continued: a neural network in NumPy, then the same network in PyTorch',
    notes: [
      { slug: 'what-is-a-neural-network', title: 'What is a neural network?', week: 5, ready: true },
      { slug: 'backpropagation', title: 'Backpropagation: how networks learn', week: 5 },
      { slug: 'softmax-cross-entropy', title: 'Logits, softmax and cross-entropy', week: 5 },
      { slug: 'numpy-neural-network', title: 'Build a neural network in NumPy, end to end', week: 5 },
      { slug: 'optimizers', title: 'Optimizers: SGD with momentum, Adam, AdamW and the learning rate', week: 6 },
      { slug: 'pytorch-essentials', title: 'PyTorch essentials: tensors, autograd, the training loop', week: 6 },
      { slug: 'normalization-dropout', title: 'Dropout, BatchNorm, LayerNorm and weight decay', week: 6 },
      { slug: 'cnn-rnn-to-attention', title: 'CNNs, RNNs and LSTMs: what they are and why attention replaced them', week: 6 },
    ],
  },
  {
    id: 'llm-internals',
    number: 4,
    title: 'LLM internals: build GPT from scratch',
    short: 'LLM internals',
    weeks: 'Weeks 7–9',
    goal: 'Explain and code every part of a GPT-style model: text in, next token out.',
    scope: 'The full GPT-2 architecture and training process as in the Vizuara course and the Raschka book, plus the encoder-decoder family for comparison.',
    sources: [
      'Vizuara, “Building LLMs from Scratch” (the full playlist, at 1.5–2x)',
      'Raschka, Build a Large Language Model (From Scratch), chapters 1–7',
      'Vaswani et al., “Attention Is All You Need” (2017)',
      'Jay Alammar, “The Illustrated Transformer” and “The Illustrated GPT-2”',
      'Karpathy, “Let’s build GPT: from scratch, in code, spelled out”',
    ],
    project: 'Project 1: GPT from scratch',
    notes: [
      { slug: 'what-is-an-llm', title: 'What is an LLM? Pretraining, fine-tuning and the big picture', week: 7 },
      { slug: 'tokenization-bpe', title: 'Tokenization and byte-pair encoding (BPE)', week: 7 },
      { slug: 'token-embeddings', title: 'Token embeddings: turning IDs into vectors', week: 7 },
      { slug: 'positional-encoding', title: 'Positional encoding: telling the model about word order', week: 7 },
      { slug: 'next-token-data', title: 'Preparing data: sliding windows and next-token prediction', week: 7 },
      { slug: 'self-attention-intuition', title: 'Self-attention, the simple version', week: 7 },
      { slug: 'scaled-dot-product-attention', title: 'Scaled dot-product attention: queries, keys and values', week: 8 },
      { slug: 'causal-masking', title: 'Causal masking and attention dropout', week: 8 },
      { slug: 'multi-head-attention', title: 'Multi-head attention', week: 8 },
      { slug: 'transformer-block-parts', title: 'LayerNorm, GELU, feed-forward layers and residual connections', week: 8 },
      { slug: 'gpt-architecture', title: 'The transformer block and the full GPT architecture', week: 8 },
      { slug: 'parameter-counting', title: 'Counting parameters and weight tying', week: 8 },
      { slug: 'pretraining-loop', title: 'Pretraining: the training loop, cross-entropy and perplexity', week: 9 },
      { slug: 'decoding-strategies', title: 'Decoding: greedy, temperature, top-k and top-p', week: 9 },
      { slug: 'loading-pretrained-weights', title: 'Loading pretrained GPT-2 weights', week: 9 },
      { slug: 'classification-finetuning', title: 'Fine-tuning for classification', week: 9 },
      { slug: 'instruction-finetuning', title: 'Instruction fine-tuning', week: 9 },
      { slug: 'encoder-vs-decoder', title: 'Encoder, decoder, encoder–decoder: BERT vs GPT vs T5', week: 9 },
    ],
  },
  {
    id: 'modern-llm-stack',
    number: 5,
    title: 'The modern LLM stack',
    short: 'Modern',
    weeks: 'Week 10',
    goal: 'Know what changed between GPT-2 and today’s models, and how models are adapted and shrunk cheaply.',
    scope: 'Architecture changes, RoPE, the KV cache, quantization, LoRA and QLoRA, preference tuning, and how to choose between prompting, RAG and fine-tuning.',
    sources: [
      'Hu et al., “LoRA: Low-Rank Adaptation of Large Language Models” (2021)',
      'Dettmers et al., “QLoRA” (2023)',
      'Su et al., “RoFormer: Rotary Position Embedding” (2021)',
      'Raschka, Build a Large Language Model (From Scratch), Appendix E: LoRA',
      'Hugging Face PEFT and Transformers documentation',
    ],
    project: 'Project 2: QLoRA fine-tune, quantize, run locally',
    notes: [
      { slug: 'modern-architecture-changes', title: 'From GPT-2 to modern LLMs: pre-norm, RMSNorm, SwiGLU, grouped-query attention', week: 10 },
      { slug: 'rope', title: 'Rotary position embeddings (RoPE)', week: 10 },
      { slug: 'kv-cache', title: 'The KV cache: why generation is fast', week: 10 },
      { slug: 'quantization', title: 'Quantization: 16-bit, 8-bit, 4-bit and GGUF', week: 10 },
      { slug: 'lora-qlora', title: 'LoRA, QLoRA and parameter-efficient fine-tuning', week: 10 },
      { slug: 'rlhf-dpo', title: 'Teaching preferences: RLHF and DPO', week: 10 },
      { slug: 'context-windows-reasoning', title: 'Context windows and reasoning models', week: 10 },
      { slug: 'prompt-vs-rag-vs-finetune', title: 'Prompting vs RAG vs fine-tuning: how to choose', week: 10 },
    ],
  },
  {
    id: 'rag',
    number: 6,
    title: 'Retrieval-augmented generation (RAG)',
    short: 'RAG',
    weeks: 'Weeks 11–12',
    goal: 'Design, build and measure a RAG system, and explain every trade-off in it.',
    scope: 'Embeddings, vector search, chunking, hybrid retrieval, reranking, the full pipeline, advanced variants, evaluation and debugging.',
    sources: [
      'Chip Huyen, AI Engineering (2025), the RAG and agents chapter',
      'Jay Alammar and Maarten Grootendorst, Hands-On Large Language Models',
      'Lewis et al., “Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks” (2020)',
      'Malkov and Yashunin, “HNSW” (2016)',
      'Anthropic, “Introducing Contextual Retrieval” (2024)',
    ],
    project: 'Project 3: production RAG with evals',
    notes: [
      { slug: 'embeddings-similarity', title: 'Text embeddings and semantic similarity', week: 11 },
      { slug: 'vector-databases', title: 'Vector databases and approximate nearest neighbour search (HNSW, IVF)', week: 11 },
      { slug: 'chunking', title: 'Chunking strategies', week: 11 },
      { slug: 'retrieval-methods', title: 'Retrieval: BM25, dense, hybrid search and rank fusion', week: 11 },
      { slug: 'reranking', title: 'Reranking with cross-encoders', week: 11 },
      { slug: 'rag-pipeline', title: 'The RAG pipeline end to end', week: 12 },
      { slug: 'advanced-rag', title: 'Advanced RAG: query rewriting, HyDE, multi-hop, GraphRAG, agentic RAG', week: 12 },
      { slug: 'rag-evaluation', title: 'Evaluating RAG: recall@k, MRR, nDCG, faithfulness', week: 12 },
      { slug: 'rag-failure-modes', title: 'RAG failure modes and how to debug them', week: 12 },
    ],
  },
  {
    id: 'agents',
    number: 7,
    title: 'Prompting, tools and agents',
    short: 'Agents',
    weeks: 'Weeks 13–14',
    goal: 'Build reliable LLM features: good context, structured output, tool use and agent loops.',
    scope: 'Prompt and context engineering, structured output, the agent loop, agent patterns, MCP, memory, multi-agent systems and security.',
    sources: [
      'Anthropic, “Building Effective Agents” (2024)',
      'Yao et al., “ReAct: Synergizing Reasoning and Acting in Language Models” (2022)',
      'Model Context Protocol specification and documentation',
      'Anthropic and OpenAI prompt engineering guides',
      'Chip Huyen, AI Engineering (2025), the prompt engineering chapter',
    ],
    project: 'Project 4: agent with your own MCP server',
    notes: [
      { slug: 'prompt-engineering', title: 'Prompt engineering that survives production', week: 13 },
      { slug: 'context-engineering', title: 'Context engineering: what goes in the window', week: 13 },
      { slug: 'structured-output-tools', title: 'Structured output and function (tool) calling', week: 13 },
      { slug: 'agent-loop-react', title: 'The agent loop and ReAct', week: 13 },
      { slug: 'agent-patterns', title: 'Workflows vs agents: routing, orchestrator–workers, evaluator–optimizer', week: 13 },
      { slug: 'mcp', title: 'Model Context Protocol (MCP)', week: 14 },
      { slug: 'agent-memory', title: 'Agent memory: short-term, long-term, compaction', week: 14 },
      { slug: 'multi-agent', title: 'Multi-agent systems: when they help and when they hurt', week: 14 },
      { slug: 'agent-security', title: 'Prompt injection and agent security', week: 14 },
    ],
  },
  {
    id: 'production',
    number: 8,
    title: 'Evals and production',
    short: 'Prod',
    weeks: 'Week 15',
    goal: 'Prove an LLM feature works, then run it cheaply, quickly and safely.',
    scope: 'Evaluation, LLM-as-judge, hallucination, guardrails, cost, latency, serving and observability.',
    sources: [
      'Chip Huyen, AI Engineering (2025), the evaluation and inference optimization chapters',
      'Hamel Husain, “Your AI Product Needs Evals”',
      'vLLM documentation (continuous batching, PagedAttention)',
    ],
    project: 'Project 4 continued: evals, guardrails, cost and latency report',
    notes: [
      { slug: 'evals-fundamentals', title: 'Evals: golden sets, metrics and regression testing', week: 15 },
      { slug: 'llm-as-judge', title: 'LLM-as-judge: how to trust a model grading a model', week: 15 },
      { slug: 'hallucination', title: 'Hallucination: causes, detection, mitigation', week: 15 },
      { slug: 'guardrails', title: 'Guardrails and safety layers', week: 15 },
      { slug: 'cost-latency', title: 'Cost and latency: caching, batching, streaming, model routing', week: 15 },
      { slug: 'serving', title: 'Serving LLMs: time to first token, throughput, continuous batching', week: 15 },
      { slug: 'observability', title: 'Observability and tracing', week: 15 },
    ],
  },
  {
    id: 'interview',
    number: 9,
    title: 'LLM system design and interview drill',
    short: 'Interview',
    weeks: 'Week 16, then every Sunday while applying',
    goal: 'Turn everything into spoken, structured answers under time pressure.',
    scope: 'A framework for design rounds, three worked designs, the ML coding round, question banks and project storytelling.',
    sources: [
      'Our own notes, tracks 1–8',
      'Alex Xu, System Design Interview (for the classic distributed-systems parts)',
      'Chip Huyen, AI Engineering (2025), the architecture chapter',
    ],
    project: 'Polish all projects: READMEs, demos, resume bullets',
    notes: [
      { slug: 'system-design-framework', title: 'A framework for LLM system design rounds', week: 16 },
      { slug: 'design-support-chatbot', title: 'Design: a customer support assistant', week: 16 },
      { slug: 'design-enterprise-search', title: 'Design: enterprise document search at scale', week: 16 },
      { slug: 'design-code-assistant', title: 'Design: a coding assistant', week: 16 },
      { slug: 'ml-coding-round', title: 'The ML coding round: attention, BPE and sampling from memory', week: 16 },
      { slug: 'question-bank-fundamentals', title: 'Question bank: math, ML and DL fundamentals', week: 16 },
      { slug: 'question-bank-applied', title: 'Question bank: applied AI engineering', week: 16 },
      { slug: 'project-storytelling', title: 'Talking about your projects', week: 16 },
    ],
  },
];

export const noteHref = (track: Track, note: Note) => `/notes/${track.id}/${note.slug}/`;

export const totalNotes = tracks.reduce((n, t) => n + t.notes.length, 0);

/** Every note of a given week, grouped by track, for the week-by-week schedule. */
export const notesForWeek = (week: number) =>
  tracks
    .map((track) => ({ track, notes: track.notes.filter((n) => n.week === week) }))
    .filter((g) => g.notes.length > 0);
