// Weekly practice plan. Notes give the words; these drills make them stick.
// Every week has hand problems (paper, no computer), coding drills (NumPy or
// PyTorch, typed by hand) and a project milestone. Links are checked when added.

export interface Resource {
  title: string;
  href: string;
  note?: string;
}

export interface WeekPlan {
  week: number;
  theme: string;
  byHand: string[];
  code: string[];
  milestone: string;
  resources?: Resource[];
}

export const weeklyPractice: WeekPlan[] = [
  {
    week: 1,
    theme: 'Vectors, matrices and linear regression',
    byHand: [
      'Compute ten dot products of small vectors (2 to 4 numbers) and say for each whether the vectors point roughly the same way, opposite ways or at right angles.',
      'Multiply a 2×3 matrix by a 3×2 matrix, then by a 3×1 column. Write the shape of the result before you compute it, every time.',
      'Given ten random matrix shapes, decide which pairs can be multiplied and in which order; write the output shape.',
      'Compute cosine similarity between three pairs of vectors by hand. Change one number and predict whether the similarity rises or falls.',
      'Simplify ten expressions using exponent and logarithm rules: log(ab), log(a/b), log(a^n), e^(ln x), and log base change.',
      'Fit a line by eye to five points on paper, then compute the mean squared error of your line.',
    ],
    code: [
      'In NumPy, implement dot product, matrix multiplication and cosine similarity with plain loops, then assert they match np.dot, @ and the vector formula.',
      'Write a function that checks whether two arrays can be matrix-multiplied and returns the output shape, with tests.',
      'Load a small dataset (the diabetes or California housing set from scikit-learn). Compute mean, min and max of each column. Scale the columns to zero mean and unit variance by hand.',
      'Fit linear regression three ways: the closed-form normal equation in NumPy, scikit-learn’s LinearRegression, and a hand-written loop that tries random slopes and keeps the best. Compare the coefficients.',
      'Plot the loss of a one-feature linear regression as a function of the slope. Find the minimum by eye, then by code.',
    ],
    milestone: 'Project 0: create the repository, a package layout with tests, and a working LinearRegression class (normal equation) with a test against scikit-learn.',
    resources: [
      { title: '3Blue1Brown, Essence of linear algebra (chapters 1–4)', href: 'https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab' },
      { title: 'Khan Academy, Linear algebra: vectors and spaces (practice exercises)', href: 'https://www.khanacademy.org/math/linear-algebra', note: 'Do the exercises, not only the videos.' },
      { title: 'NumPy: the absolute basics for beginners', href: 'https://numpy.org/doc/stable/user/absolute_beginners.html' },
      { title: 'StatQuest, Linear regression, clearly explained', href: 'https://www.youtube.com/watch?v=7ArmBVF2dCs' },
    ],
  },
  {
    week: 2,
    theme: 'Derivatives, gradients and gradient descent',
    byHand: [
      'Differentiate twenty simple functions: polynomials, e^x, ln x, 1/x, and products and quotients of them.',
      'For f(x, y) = x²y + 3y, compute both partial derivatives and the gradient at (1, 2). Draw the arrow on a sketch.',
      'Apply the chain rule to ten nested functions, including sigmoid(3x + 1) and (2x + 1)⁵. Write every intermediate step.',
      'Compute the derivative of mean squared error with respect to the slope for a two-point dataset, by hand.',
      'Run three steps of gradient descent by hand on f(x) = (x − 3)² from x = 0 with learning rate 0.1, then with learning rate 1.1. Explain what happened in the second case.',
      'Sketch what overfitting and underfitting look like on a scatter plot, and label which has high bias and which has high variance.',
    ],
    code: [
      'Write a numerical derivative function using (f(x + h) − f(x − h)) / 2h and check your hand answers from the by-hand list.',
      'Implement gradient descent for one-feature linear regression in NumPy. Plot the loss per step for learning rates 0.001, 0.01, 0.1 and 1.0.',
      'Extend it to many features using matrix form. Compare with the normal equation from Week 1.',
      'Implement batch, stochastic and mini-batch gradient descent; plot all three loss curves on one chart.',
      'Fit polynomials of degree 1, 3 and 15 to 20 noisy points. Plot train and test error against degree.',
    ],
    milestone: 'Project 0: gradient-descent trainer with pluggable loss, learning-rate schedule and loss logging; MSE and MAE losses with tests on their gradients.',
    resources: [
      { title: '3Blue1Brown, Essence of calculus (chapters 1–4)', href: 'https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr' },
      { title: 'Khan Academy, Differential calculus (practice exercises)', href: 'https://www.khanacademy.org/math/differential-calculus' },
      { title: 'StatQuest, Gradient descent, step by step', href: 'https://www.youtube.com/watch?v=sDv4f4s2SB8' },
      { title: 'StatQuest, Bias and variance', href: 'https://www.youtube.com/watch?v=EuBBz3bI-aA' },
    ],
  },
  {
    week: 3,
    theme: 'Probability, logistic regression and evaluation',
    byHand: [
      'Compute mean, median, variance and standard deviation of three small lists. Add one outlier and recompute: which changed most?',
      'Solve five Bayes’ theorem problems, including the classic medical test with a 1% base rate and a 95% accurate test.',
      'Compute the expected value and variance of a die roll and of a biased coin.',
      'Evaluate sigmoid(z) for z = −4, −1, 0, 1, 4 by hand, and log loss for predictions 0.9, 0.5 and 0.1 when the true label is 1.',
      'Fill in a confusion matrix from a list of 20 predictions and labels, then compute accuracy, precision, recall and F1.',
      'Draw an ROC curve from five thresholds on a tiny dataset.',
      'Explain in writing why maximizing likelihood for a yes/no model gives the log-loss formula.',
    ],
    code: [
      'Simulate 10,000 coin flips and dice rolls; compare sample means and variances with the formulas.',
      'Implement logistic regression in NumPy with gradient descent on the breast-cancer dataset. Compare the accuracy with scikit-learn.',
      'Implement accuracy, precision, recall, F1 and ROC-AUC from scratch; check against scikit-learn.metrics.',
      'Write k-fold cross-validation from scratch and use it to pick the learning rate.',
      'Plot the normal distribution for three different means and standard deviations; shade one standard deviation.',
    ],
    milestone: 'Project 0: LogisticRegression class, a metrics module and a cross-validation helper, each tested against scikit-learn.',
    resources: [
      { title: 'Seeing Theory: visual probability and statistics', href: 'https://seeing-theory.brown.edu/' },
      { title: '3Blue1Brown, Bayes theorem, the geometry of changing beliefs', href: 'https://www.youtube.com/watch?v=HZGCoVF3YvM' },
      { title: 'Khan Academy, Statistics and probability (practice exercises)', href: 'https://www.khanacademy.org/math/statistics-probability' },
      { title: 'StatQuest, Logistic regression', href: 'https://www.youtube.com/watch?v=yIYKR4sgzI8' },
    ],
  },
  {
    week: 4,
    theme: 'Entropy, regularization, similarity models and trees',
    byHand: [
      'Compute the entropy of a fair coin, a 90/10 coin and a fair die in bits.',
      'Compute cross-entropy and KL divergence between p = (0.5, 0.5) and q = (0.9, 0.1), both ways round. Note which is smaller.',
      'Write the L1 and L2 regularized loss for a two-weight model and compute the gradient of each penalty. Say in words why L1 makes weights exactly zero.',
      'Classify three new points by hand with kNN (k = 3) on a ten-point dataset; then run two iterations of k-means with k = 2.',
      'Compute the information gain of one split in a tiny decision tree.',
      'Given a dataset with 99% negatives, explain why 99% accuracy can be useless, and name two metrics that would expose it.',
    ],
    code: [
      'Implement kNN and k-means in NumPy; check against scikit-learn on the iris dataset.',
      'Implement PCA with NumPy’s SVD; project the iris data to two dimensions and plot it coloured by class.',
      'Add L2 regularization to your logistic regression; plot weight sizes against the regularization strength.',
      'Train a decision tree, a random forest and gradient boosting with scikit-learn on one tabular dataset; compare cross-validated scores and training time.',
      'Create a deliberately leaky feature (one computed from the label) and watch the validation score become suspiciously perfect. Then remove it.',
    ],
    milestone: 'Project 0: kNN, k-means and PCA added to the library. Tabular case study started: a Kaggle dataset with a clean split, a baseline and a results table.',
    resources: [
      { title: 'Kaggle, House Prices: a tabular regression case study', href: 'https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques' },
      { title: 'Kaggle Learn: short hands-on courses', href: 'https://www.kaggle.com/learn' },
      { title: 'scikit-learn user guide', href: 'https://scikit-learn.org/stable/user_guide.html', note: 'Read the page for each algorithm you implement.' },
      { title: 'Deep-ML: machine-learning coding problems, LeetCode style', href: 'https://www.deep-ml.com/', note: 'Do the easy linear algebra and ML problems from this week on.' },
    ],
  },
  {
    week: 5,
    theme: 'Neurons, backpropagation and softmax',
    byHand: [
      'Run the walk neuron and the XOR network from the neural-network note by hand on new inputs.',
      'Count the parameters of three small networks drawn on paper.',
      'Backpropagate by hand through a two-layer network with one hidden neuron, writing every local derivative.',
      'Compute softmax of (2, 1, 0) and the cross-entropy against each possible true class.',
      'Derive the gradient of cross-entropy with softmax with respect to the logits, and check it equals prediction minus target.',
    ],
    code: [
      'Rewrite micrograd from Karpathy’s video from memory: a scalar Value class with backward().',
      'Implement a two-layer network in NumPy with manual backprop; train it on XOR and then on a two-moons dataset.',
      'Check every gradient with a numerical gradient check.',
      'Implement softmax safely (subtract the maximum) and show what happens without the subtraction for large logits.',
    ],
    milestone: 'Project 0: a NumPy MLP with configurable layers trained on MNIST digits to above 95% test accuracy, with a gradient check in the tests.',
    resources: [
      { title: '3Blue1Brown, Neural networks (chapters 1–4)', href: 'https://www.youtube.com/watch?v=aircAruvnKk' },
      { title: 'Karpathy, The spelled-out intro to neural networks and backpropagation: building micrograd', href: 'https://www.youtube.com/watch?v=VMj-3S1tku0' },
      { title: 'Nielsen, Neural Networks and Deep Learning, chapters 1–2', href: 'http://neuralnetworksanddeeplearning.com/chap1.html' },
    ],
  },
  {
    week: 6,
    theme: 'Optimizers, PyTorch and regularization',
    byHand: [
      'Run three steps of SGD with momentum and three of Adam by hand on f(x) = x², tracking every running average.',
      'Write the LayerNorm formula and apply it to the vector (1, 2, 3, 6).',
      'Explain dropout at train time and at test time, including the scaling, in writing.',
      'Draw a convolution of a 3×3 filter over a 5×5 image and give the output size; then do it with padding 1.',
    ],
    code: [
      'Reimplement your NumPy MLP in PyTorch with nn.Module, then train it with SGD, SGD+momentum, Adam and AdamW; plot the four loss curves.',
      'Add dropout and weight decay; compare train and test accuracy with and without them.',
      'Add LayerNorm and BatchNorm; measure the effect on training speed.',
      'Write a learning-rate finder: increase the learning rate each step and plot loss against learning rate.',
      'Train a tiny character-level RNN on a short text, generate text, and note where it fails. This is the motivation for attention.',
    ],
    milestone: 'Project 0 complete: NumPy and PyTorch MLPs with a README comparing optimizers and regularization on MNIST. Write the resume bullet.',
    resources: [
      { title: 'Raschka, Build a Large Language Model (From Scratch), Appendix A code', href: 'https://github.com/rasbt/LLMs-from-scratch/tree/main/appendix-A' },
      { title: 'Karpathy, Building makemore (character-level models)', href: 'https://www.youtube.com/watch?v=PaCmpygFfXo' },
    ],
  },
  {
    week: 7,
    theme: 'Tokens, embeddings and the attention idea',
    byHand: [
      'Run three merges of byte-pair encoding by hand on a short string.',
      'Given a 5-word vocabulary and 3-dimensional embeddings, look up a sentence and write the resulting matrix and its shape.',
      'Compute a simplified attention: three 2-dimensional vectors, dot products, softmax, weighted sum.',
    ],
    code: [
      'Implement BPE training and encoding from scratch; compare the token count with tiktoken on the same paragraph.',
      'Build the sliding-window dataset and data loader; print input and target pairs and check them by eye.',
      'Implement simplified self-attention (no trainable weights) in PyTorch with loops, then with matrix operations; assert equal.',
    ],
    milestone: 'Project 1: tokenizer and data pipeline done, with tests.',
  },
  {
    week: 8,
    theme: 'Full attention and the transformer block',
    byHand: [
      'Write the shapes of Q, K, V, the score matrix and the output for batch 2, 4 tokens, 8 dimensions, 2 heads.',
      'Explain why scores are divided by the square root of the key dimension, with a numerical example.',
      'Count the parameters of one GPT-2 small transformer block.',
    ],
    code: [
      'Implement causal multi-head attention from memory, then the full transformer block and the GPT model.',
      'Write a parameter-count test that reproduces 124M for the GPT-2 small configuration.',
      'Visualize an attention map for a short sentence.',
    ],
    milestone: 'Project 1: full model forward pass works; parameter count matches GPT-2 small.',
  },
  {
    week: 9,
    theme: 'Training, decoding and fine-tuning',
    byHand: [
      'Compute perplexity from a cross-entropy loss of 2.3, and explain what it means in words.',
      'Apply temperature 0.5 and 2.0 to the logits (2, 1, 0) and compute the new probabilities.',
      'Walk through top-k and top-p sampling on a five-token distribution.',
    ],
    code: [
      'Write the pretraining loop with warmup, cosine decay and gradient clipping; train on TinyStories on a free GPU.',
      'Implement greedy, temperature, top-k and top-p decoding.',
      'Load GPT-2 weights into your model and fine-tune it as a classifier and then on instructions.',
    ],
    milestone: 'Project 1 complete with a README and generated samples.',
  },
  {
    week: 10,
    theme: 'Modern architecture, LoRA and quantization',
    byHand: [
      'Count the parameters LoRA adds to a 768×768 layer at rank 8, and the percentage of the original.',
      'Convert four float values to 8-bit integers with a scale and zero point, then back; compute the error.',
      'Explain the KV cache with a diagram, and compute its memory for a given model and sequence length.',
    ],
    code: [
      'Implement LoRA from scratch on your Project 1 model and fine-tune only the adapters.',
      'Add a KV cache to your model and measure tokens per second before and after.',
      'Run the full QLoRA fine-tune, convert to GGUF, and run it on your CPU.',
    ],
    milestone: 'Project 2 complete with a before-and-after results table.',
  },
  {
    week: 11,
    theme: 'Embeddings, vector search and retrieval',
    byHand: [
      'Rank five short documents against a query by cosine similarity on tiny hand-made embeddings.',
      'Compute BM25 for one query term over three documents.',
      'Combine two rankings with reciprocal rank fusion by hand.',
    ],
    code: [
      'Embed a corpus, build a brute-force search, then an HNSW index; compare recall and speed.',
      'Implement BM25 and hybrid search with rank fusion.',
      'Add a cross-encoder reranker and measure recall@k before and after.',
    ],
    milestone: 'Project 3: corpus ingested, golden set written, baseline retrieval measured.',
  },
  {
    week: 12,
    theme: 'The RAG pipeline and its evaluation',
    byHand: [
      'Compute recall@3, MRR and nDCG for three queries by hand.',
      'Design a chunking strategy for a code base and for a legal contract, and justify the difference.',
    ],
    code: [
      'Assemble the full pipeline with citations and streaming.',
      'Build an LLM judge for faithfulness and validate it against 50 of your own labels.',
      'Run the ablation table: chunk size, hybrid on/off, reranker on/off.',
    ],
    milestone: 'Project 3 complete with a results table and a failure-mode section in the README.',
  },
  {
    week: 13,
    theme: 'Prompting, tools and the agent loop',
    byHand: [
      'Rewrite a vague prompt into a production prompt with role, constraints, format and examples.',
      'Draw the agent loop and label where failures can happen at each arrow.',
    ],
    code: [
      'Write the agent loop with no framework: model call, tool call, result, repeat, with a step budget.',
      'Add structured output with a schema and retries on validation failure.',
    ],
    milestone: 'Project 4: the bare agent completes five of your test tasks.',
  },
  {
    week: 14,
    theme: 'MCP, memory and security',
    byHand: [
      'Write three prompt-injection attacks against your own agent and a defence for each.',
      'Design a memory scheme for a week-long task: what is kept, summarized and dropped.',
    ],
    code: [
      'Build an MCP server exposing your tools and connect the agent to it.',
      'Add compaction and a simple long-term memory; run a long task.',
      'Run the injection attacks against the agent and fix what breaks.',
    ],
    milestone: 'Project 4: 30 test tasks with a measured success rate.',
  },
  {
    week: 15,
    theme: 'Evals, cost and serving',
    byHand: [
      'Design an eval set for a feature of your choice: what is measured, how labels are made, what regression means.',
      'Estimate monthly cost for a feature at a given traffic, token count and model price; then halve it on paper.',
    ],
    code: [
      'Add tracing to the agent so every run can be inspected step by step.',
      'Add prompt caching and model routing; report cost and latency before and after.',
      'Add guardrails: input checks, tool permission limits and output validation.',
    ],
    milestone: 'Project 4 complete with a cost, latency and success-rate report.',
  },
  {
    week: 16,
    theme: 'Interview drill',
    byHand: [
      'Answer one question-bank section per day out loud, timed, without notes.',
      'Do one full system-design run per day on paper: 45 minutes, one of the three worked designs or a new prompt.',
      'Write and rehearse the two-minute story for each project.',
    ],
    code: [
      'From memory, in under 20 minutes each: scaled dot-product attention, BPE merge step, top-p sampling, logistic regression with gradient descent, k-means.',
      'Solve ten Deep-ML problems under time pressure.',
    ],
    milestone: 'All project READMEs polished; resume bullets written with measured numbers.',
    resources: [{ title: 'Deep-ML: timed ML coding problems', href: 'https://www.deep-ml.com/' }],
  },
];
