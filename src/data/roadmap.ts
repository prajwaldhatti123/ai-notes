// Single source of truth for the learning path. The home page, the roadmap page
// and the note navigation are all generated from this file.

export interface Note {
  slug: string;
  title: string;
  ready?: boolean;
}

export interface Phase {
  id: string;
  number: number;
  title: string;
  weeks: string;
  goal: string;
  sources: string[];
  project?: string;
  notes: Note[];
}

export const phases: Phase[] = [
  {
    id: 'foundations',
    number: 1,
    title: 'Deep learning foundations',
    weeks: 'Week 1',
    goal: 'Understand how any neural network learns, and be able to write a training loop in PyTorch from memory.',
    sources: [
      '3Blue1Brown, “Neural Networks” series (chapters 1–4)',
      'Andrej Karpathy, “Zero to Hero”: the micrograd video',
      'Raschka, Build a Large Language Model (From Scratch), Appendix A: Introduction to PyTorch',
    ],
    notes: [
      { slug: 'what-is-a-neural-network', title: 'What is a neural network?', ready: true },
      { slug: 'loss-functions', title: 'Loss functions: measuring how wrong we are' },
      { slug: 'backpropagation', title: 'Gradient descent and backpropagation' },
      { slug: 'optimizers', title: 'Optimizers: SGD, Adam, AdamW and the learning rate' },
      { slug: 'softmax-cross-entropy', title: 'Logits, softmax and cross-entropy' },
      { slug: 'pytorch-essentials', title: 'PyTorch essentials: tensors, autograd, the training loop' },
      { slug: 'overfitting', title: 'Overfitting, regularization and data splits' },
    ],
  },
  {
    id: 'llm-internals',
    number: 2,
    title: 'LLM internals: build GPT from scratch',
    weeks: 'Weeks 2–4',
    goal: 'Explain and code every part of a GPT-style model: text in, next token out.',
    sources: [
      'Vizuara, “Building LLMs from Scratch” (the full playlist, at 1.5–2x)',
      'Raschka, Build a Large Language Model (From Scratch), chapters 1–7',
      'Vaswani et al., “Attention Is All You Need” (2017)',
      'Jay Alammar, “The Illustrated Transformer” and “The Illustrated GPT-2”',
      'Karpathy, “Let’s build GPT: from scratch, in code, spelled out”',
    ],
    project: 'Project 1: GPT from scratch',
    notes: [
      { slug: 'what-is-an-llm', title: 'What is an LLM? Pretraining, fine-tuning and the big picture' },
      { slug: 'tokenization-bpe', title: 'Tokenization and byte-pair encoding (BPE)' },
      { slug: 'token-embeddings', title: 'Token embeddings: turning IDs into vectors' },
      { slug: 'positional-encoding', title: 'Positional encoding: telling the model about word order' },
      { slug: 'next-token-data', title: 'Preparing data: sliding windows and next-token prediction' },
      { slug: 'self-attention-intuition', title: 'Self-attention, the simple version' },
      { slug: 'scaled-dot-product-attention', title: 'Scaled dot-product attention: queries, keys and values' },
      { slug: 'causal-masking', title: 'Causal masking and attention dropout' },
      { slug: 'multi-head-attention', title: 'Multi-head attention' },
      { slug: 'transformer-block-parts', title: 'LayerNorm, GELU, feed-forward layers and residual connections' },
      { slug: 'gpt-architecture', title: 'The transformer block and the full GPT architecture' },
      { slug: 'parameter-counting', title: 'Counting parameters and weight tying' },
      { slug: 'pretraining-loop', title: 'Pretraining: the training loop, cross-entropy and perplexity' },
      { slug: 'decoding-strategies', title: 'Decoding: greedy, temperature, top-k and top-p' },
      { slug: 'loading-pretrained-weights', title: 'Loading pretrained GPT-2 weights' },
      { slug: 'classification-finetuning', title: 'Fine-tuning for classification' },
      { slug: 'instruction-finetuning', title: 'Instruction fine-tuning' },
      { slug: 'encoder-vs-decoder', title: 'Encoder, decoder, encoder–decoder: BERT vs GPT vs T5' },
    ],
  },
  {
    id: 'modern-llm-stack',
    number: 3,
    title: 'The modern LLM stack',
    weeks: 'Week 5',
    goal: 'Know what changed between GPT-2 and today’s models, and how models are adapted and shrunk cheaply.',
    sources: [
      'Hu et al., “LoRA: Low-Rank Adaptation of Large Language Models” (2021)',
      'Dettmers et al., “QLoRA” (2023)',
      'Su et al., “RoFormer: Rotary Position Embedding” (2021)',
      'Raschka, Build a Large Language Model (From Scratch), Appendix E: LoRA',
      'Hugging Face PEFT and Transformers documentation',
    ],
    project: 'Project 2: QLoRA fine-tune, quantize, run locally',
    notes: [
      { slug: 'modern-architecture-changes', title: 'From GPT-2 to modern LLMs: pre-norm, RMSNorm, SwiGLU, grouped-query attention' },
      { slug: 'rope', title: 'Rotary position embeddings (RoPE)' },
      { slug: 'kv-cache', title: 'The KV cache: why generation is fast' },
      { slug: 'quantization', title: 'Quantization: 16-bit, 8-bit, 4-bit and GGUF' },
      { slug: 'lora-qlora', title: 'LoRA, QLoRA and parameter-efficient fine-tuning' },
      { slug: 'rlhf-dpo', title: 'Teaching preferences: RLHF and DPO' },
      { slug: 'context-windows-reasoning', title: 'Context windows and reasoning models' },
      { slug: 'prompt-vs-rag-vs-finetune', title: 'Prompting vs RAG vs fine-tuning: how to choose' },
    ],
  },
  {
    id: 'rag',
    number: 4,
    title: 'Retrieval-augmented generation (RAG)',
    weeks: 'Weeks 6–7',
    goal: 'Design, build and measure a RAG system, and explain every trade-off in it.',
    sources: [
      'Chip Huyen, AI Engineering (2025), the RAG and agents chapter',
      'Jay Alammar and Maarten Grootendorst, Hands-On Large Language Models',
      'Lewis et al., “Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks” (2020)',
      'Malkov and Yashunin, “HNSW” (2016)',
      'Anthropic, “Introducing Contextual Retrieval” (2024)',
    ],
    project: 'Project 3: production RAG with evals',
    notes: [
      { slug: 'embeddings-similarity', title: 'Text embeddings and semantic similarity' },
      { slug: 'vector-databases', title: 'Vector databases and approximate nearest neighbour search (HNSW, IVF)' },
      { slug: 'chunking', title: 'Chunking strategies' },
      { slug: 'retrieval-methods', title: 'Retrieval: BM25, dense, hybrid search and rank fusion' },
      { slug: 'reranking', title: 'Reranking with cross-encoders' },
      { slug: 'rag-pipeline', title: 'The RAG pipeline end to end' },
      { slug: 'advanced-rag', title: 'Advanced RAG: query rewriting, HyDE, multi-hop, GraphRAG, agentic RAG' },
      { slug: 'rag-evaluation', title: 'Evaluating RAG: recall@k, MRR, nDCG, faithfulness' },
      { slug: 'rag-failure-modes', title: 'RAG failure modes and how to debug them' },
    ],
  },
  {
    id: 'agents',
    number: 5,
    title: 'Prompting, tools and agents',
    weeks: 'Weeks 8–9',
    goal: 'Build reliable LLM features: good context, structured output, tool use and agent loops.',
    sources: [
      'Anthropic, “Building Effective Agents” (2024)',
      'Yao et al., “ReAct: Synergizing Reasoning and Acting in Language Models” (2022)',
      'Model Context Protocol specification and documentation',
      'Anthropic and OpenAI prompt engineering guides',
      'Chip Huyen, AI Engineering (2025), the prompt engineering chapter',
    ],
    project: 'Project 4: agent with your own MCP server',
    notes: [
      { slug: 'prompt-engineering', title: 'Prompt engineering that survives production' },
      { slug: 'context-engineering', title: 'Context engineering: what goes in the window' },
      { slug: 'structured-output-tools', title: 'Structured output and function (tool) calling' },
      { slug: 'agent-loop-react', title: 'The agent loop and ReAct' },
      { slug: 'agent-patterns', title: 'Workflows vs agents: routing, orchestrator–workers, evaluator–optimizer' },
      { slug: 'mcp', title: 'Model Context Protocol (MCP)' },
      { slug: 'agent-memory', title: 'Agent memory: short-term, long-term, compaction' },
      { slug: 'multi-agent', title: 'Multi-agent systems: when they help and when they hurt' },
      { slug: 'agent-security', title: 'Prompt injection and agent security' },
    ],
  },
  {
    id: 'production',
    number: 6,
    title: 'Evals and production',
    weeks: 'Week 10',
    goal: 'Prove an LLM feature works, then run it cheaply, quickly and safely.',
    sources: [
      'Chip Huyen, AI Engineering (2025), the evaluation and inference optimization chapters',
      'Hamel Husain, “Your AI Product Needs Evals”',
      'vLLM documentation (continuous batching, PagedAttention)',
    ],
    project: 'Project 4 continued: evals, guardrails, cost and latency report',
    notes: [
      { slug: 'evals-fundamentals', title: 'Evals: golden sets, metrics and regression testing' },
      { slug: 'llm-as-judge', title: 'LLM-as-judge: how to trust a model grading a model' },
      { slug: 'hallucination', title: 'Hallucination: causes, detection, mitigation' },
      { slug: 'guardrails', title: 'Guardrails and safety layers' },
      { slug: 'cost-latency', title: 'Cost and latency: caching, batching, streaming, model routing' },
      { slug: 'serving', title: 'Serving LLMs: time to first token, throughput, continuous batching' },
      { slug: 'observability', title: 'Observability and tracing' },
    ],
  },
  {
    id: 'interview',
    number: 7,
    title: 'LLM system design and interview drill',
    weeks: 'Weeks 11–12',
    goal: 'Turn everything into spoken, structured answers under time pressure.',
    sources: [
      'Our own notes, phases 1–6',
      'Alex Xu, System Design Interview (for the classic distributed-systems parts)',
      'Chip Huyen, AI Engineering (2025), the architecture chapter',
    ],
    project: 'Polish all four projects: READMEs, demos, resume bullets',
    notes: [
      { slug: 'system-design-framework', title: 'A framework for LLM system design rounds' },
      { slug: 'design-support-chatbot', title: 'Design: a customer support assistant' },
      { slug: 'design-enterprise-search', title: 'Design: enterprise document search at scale' },
      { slug: 'design-code-assistant', title: 'Design: a coding assistant' },
      { slug: 'ml-coding-round', title: 'The ML coding round: attention, BPE and sampling from memory' },
      { slug: 'question-bank-fundamentals', title: 'Question bank: fundamentals' },
      { slug: 'question-bank-applied', title: 'Question bank: applied AI engineering' },
      { slug: 'project-storytelling', title: 'Talking about your projects' },
    ],
  },
];

export const noteHref = (phase: Phase, note: Note) => `/notes/${phase.id}/${note.slug}/`;

export const totalNotes = phases.reduce((n, p) => n + p.notes.length, 0);
