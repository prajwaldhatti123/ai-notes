// One-line, plain-words meanings for every technical word the notes use.
// A note may only use a word before the note that teaches it if the word is
// wrapped in <Term id="...">, which links here and shows this one line on hover.
// `note` is the note that teaches the word properly (track/slug); `week` is when.

export interface GlossaryEntry {
  id: string;
  term: string;
  plain: string;
  note?: string;
  week?: number;
}

export const glossary: GlossaryEntry[] = [
  // ---- the words the very first note introduces ----
  { id: 'model', term: 'model', plain: 'A recipe that turns inputs into a guess, with adjustable amounts (parameters) that training sets.', note: 'ml/what-is-machine-learning', week: 1 },
  { id: 'parameters', term: 'parameters (weights)', plain: 'The adjustable numbers inside a model. Training changes them; nothing else does.', note: 'ml/what-is-machine-learning', week: 1 },
  { id: 'hyperparameter', term: 'hyperparameter', plain: 'A setting you choose before training, such as how big the model is or how large each training step is. Training never changes it.', note: 'ml/what-is-machine-learning', week: 1 },
  { id: 'training', term: 'training', plain: 'Showing a model many examples and nudging its parameters until its guesses match the answers.', note: 'ml/what-is-machine-learning', week: 1 },
  { id: 'example', term: 'example (sample, row)', plain: 'One data point: one house, one email, one photo.', note: 'ml/what-is-machine-learning', week: 1 },
  { id: 'feature', term: 'feature', plain: 'One measured fact about an example, such as the size of a house. The inputs to the model.', note: 'ml/what-is-machine-learning', week: 1 },
  { id: 'label', term: 'label (target)', plain: 'The right answer for an example, such as the price a house really sold for.', note: 'ml/what-is-machine-learning', week: 1 },
  { id: 'prediction', term: 'prediction', plain: 'The model’s guess for one example.', note: 'ml/what-is-machine-learning', week: 1 },
  { id: 'loss', term: 'loss', plain: 'One number that says how wrong the model’s guesses are on some examples. Zero means perfect. Training tries to make it small.', note: 'ml/what-is-machine-learning', week: 1 },
  { id: 'mse', term: 'mean squared error (MSE)', plain: 'A loss for number guesses: take each error, square it, average them.', note: 'ml/what-is-machine-learning', week: 1 },
  { id: 'optimizer', term: 'optimizer', plain: 'The procedure that changes the parameters to lower the loss. Gradient descent is the usual one.', note: 'ml/what-is-machine-learning', week: 1 },
  { id: 'gradient-descent', term: 'gradient descent', plain: 'Lower the loss by nudging every parameter a little in the downhill direction, over and over.', note: 'ml/gradient-descent', week: 2 },
  { id: 'learning-rate', term: 'learning rate', plain: 'How big each nudge is in gradient descent. Too big and training bounces around; too small and it crawls.', note: 'ml/gradient-descent', week: 2 },
  { id: 'inference', term: 'inference', plain: 'Using a trained model to make guesses on new inputs.', note: 'ml/what-is-machine-learning', week: 1 },
  { id: 'generalization', term: 'generalization', plain: 'Doing well on examples the model never saw during training. The real goal.', note: 'ml/what-is-machine-learning', week: 1 },
  { id: 'overfitting', term: 'overfitting', plain: 'The model memorised its training examples, noise included, so it does well on them and badly on new ones.', note: 'ml/overfitting-bias-variance', week: 2 },
  { id: 'train-test-split', term: 'train / validation / test split', plain: 'Set some examples aside before training. Train on one part, make choices on the second, measure once on the third.', note: 'ml/data-splits-cross-validation', week: 3 },
  { id: 'supervised', term: 'supervised learning', plain: 'Learning from examples that come with the right answers.', note: 'ml/what-is-machine-learning', week: 1 },
  { id: 'regression', term: 'regression', plain: 'Guessing a number, such as a price.', note: 'ml/linear-regression', week: 1 },
  { id: 'classification', term: 'classification', plain: 'Guessing a category, such as spam or not spam.', note: 'ml/logistic-regression', week: 3 },
  { id: 'epoch', term: 'epoch', plain: 'One full pass through all the training examples.', note: 'ml/gradient-descent', week: 2 },
  { id: 'batch', term: 'batch', plain: 'A handful of examples processed together in one step, stacked as the rows of a matrix.', note: 'math/matrices-and-shapes', week: 1 },
  { id: 'baseline', term: 'baseline', plain: 'The dumbest guess that could work, such as “always predict the average”. A real model must beat it.', note: 'ml/what-is-machine-learning', week: 1 },

  // ---- language models, in plain words ----
  { id: 'language-model', term: 'language model (LLM)', plain: 'A model whose only job is to guess the next piece of text given the text so far. “Large” means billions of parameters.', note: 'llm-internals/what-is-an-llm', week: 7 },
  { id: 'token', term: 'token', plain: 'A piece of text, usually a word or part of a word. Language models read and write text one token at a time.', note: 'llm-internals/tokenization-bpe', week: 7 },
  { id: 'embedding', term: 'embedding', plain: 'A list of numbers (a vector) that stands for a word, a sentence or an image, arranged so that similar things get similar lists.', note: 'llm-internals/token-embeddings', week: 7 },
  { id: 'attention', term: 'attention', plain: 'The part of a language model that lets each word look at the other words and decide which ones matter for guessing the next one.', note: 'llm-internals/self-attention-intuition', week: 7 },
  { id: 'transformer', term: 'transformer', plain: 'The kind of neural network every modern language model is built from. Its main part is attention.', note: 'llm-internals/gpt-architecture', week: 8 },
  { id: 'context-window', term: 'context window', plain: 'How many tokens the model can look at at once.', note: 'modern-llm-stack/context-windows-reasoning', week: 10 },
  { id: 'perplexity', term: 'perplexity', plain: 'A way of reporting a language model’s loss as “how many choices it was hesitating between”. Lower is better.', note: 'llm-internals/pretraining-loop', week: 9 },
  { id: 'temperature', term: 'temperature', plain: 'A dial at generation time: low makes the model pick its top guess almost always; high makes it take more chances.', note: 'llm-internals/decoding-strategies', week: 9 },
  { id: 'logprob', term: 'log-probability (logprob)', plain: 'The logarithm of a probability. Model APIs report these instead of probabilities because they are easier to add and never underflow.', note: 'math/functions-exponents-logs', week: 1 },

  // ---- scores, probabilities and the losses built from them ----
  { id: 'probability', term: 'probability', plain: 'A number from 0 to 1 saying how likely something is. The probabilities of all the possible outcomes add up to 1.', note: 'math/probability-bayes', week: 3 },
  { id: 'logit', term: 'logit (raw score)', plain: 'A model’s raw score for one possible answer before it is turned into a probability. Can be any number, negative or huge.', note: 'dl/softmax-cross-entropy', week: 5 },
  { id: 'softmax', term: 'softmax', plain: 'The recipe that turns a list of raw scores into probabilities that add up to 1: raise e to each score, then divide by the total.', note: 'dl/softmax-cross-entropy', week: 5 },
  { id: 'sigmoid', term: 'sigmoid', plain: 'An S-shaped curve that squashes any number into the range 0 to 1, so it can be read as a probability.', note: 'ml/logistic-regression', week: 3 },
  { id: 'log-loss', term: 'log loss', plain: 'A loss for probability guesses: minus the logarithm of the probability the model gave to the right answer. Cheap when confident and right, huge when confident and wrong.', note: 'ml/loss-functions', week: 2 },
  { id: 'cross-entropy', term: 'cross-entropy', plain: 'The general name for log loss when there are several possible answers. The loss that trains every language model.', note: 'math/entropy-cross-entropy-kl', week: 4 },
  { id: 'likelihood', term: 'likelihood', plain: 'The probability a model gives to the data that actually happened. Training picks the parameters that make it as large as possible.', note: 'math/maximum-likelihood', week: 3 },
  { id: 'entropy', term: 'entropy', plain: 'A measure of how unpredictable something is: zero when the outcome is certain, largest when every outcome is equally likely.', note: 'math/entropy-cross-entropy-kl', week: 4 },
  { id: 'kl-divergence', term: 'KL divergence', plain: 'A number saying how different one probability distribution is from another. Zero means identical.', note: 'math/entropy-cross-entropy-kl', week: 4 },
  { id: 'distribution', term: 'distribution', plain: 'The full list of possible outcomes with the probability of each.', note: 'math/distributions-expectation', week: 3 },
  { id: 'calibration', term: 'calibration', plain: 'A model is calibrated when its “70% sure” guesses are right about 70% of the time.', note: 'ml/classification-metrics', week: 3 },

  // ---- calculus words ----
  { id: 'derivative', term: 'derivative (slope)', plain: 'How fast an output changes when you nudge the input a little. The slope of the graph at that point.', note: 'math/derivatives', week: 2 },
  { id: 'gradient', term: 'gradient', plain: 'The list of slopes, one per parameter, saying which way to nudge each one to raise the loss fastest. Training moves the opposite way.', note: 'math/partial-derivatives-gradient', week: 2 },
  { id: 'chain-rule', term: 'chain rule', plain: 'How to find the slope of a function made of several steps: multiply the slopes of the steps.', note: 'math/chain-rule', week: 2 },
  { id: 'backpropagation', term: 'backpropagation', plain: 'The chain rule applied layer by layer, from the loss backwards, to get the gradient of every parameter in a neural network.', note: 'dl/backpropagation', week: 5 },
  { id: 'convex', term: 'convex', plain: 'Bowl-shaped: one lowest point and no dips to get stuck in, so going downhill always reaches the bottom.', note: 'ml/gradient-descent', week: 2 },

  // ---- linear algebra words ----
  { id: 'vector', term: 'vector', plain: 'An ordered list of numbers. Also an arrow from the origin to that point.', note: 'math/vectors-dot-product', week: 1 },
  { id: 'dot-product', term: 'dot product', plain: 'Multiply two lists element by element and add up the results. One number that measures how much two vectors agree.', note: 'math/vectors-dot-product', week: 1 },
  { id: 'matrix', term: 'matrix', plain: 'A grid of numbers with rows and columns. A dataset is one: one row per example, one column per feature.', note: 'math/matrices-and-shapes', week: 1 },
  { id: 'tensor', term: 'tensor', plain: 'An array with any number of axes: a vector has one, a matrix two, a stack of images four.', note: 'math/matrices-and-shapes', week: 1 },
  { id: 'norm', term: 'norm', plain: 'The length of a vector.', note: 'math/norms-distance-cosine', week: 1 },
  { id: 'cosine-similarity', term: 'cosine similarity', plain: 'How similar two vectors are in direction, ignoring length: 1 means same direction, 0 means unrelated, −1 means opposite.', note: 'math/norms-distance-cosine', week: 1 },
  { id: 'normalization', term: 'normalization', plain: 'Rescaling numbers to a standard range, such as making a vector length 1 or putting a feature between 0 and 1.', note: 'ml/feature-scaling-encoding', week: 1 },
  { id: 'eigenvector', term: 'eigenvector', plain: 'A direction a matrix only stretches, without turning. The stretch factor is the eigenvalue.', note: 'math/eigen-svd-intuition', week: 4 },

  // ---- statistics words ----
  { id: 'mean', term: 'mean', plain: 'The average.', note: 'math/descriptive-statistics', week: 3 },
  { id: 'variance', term: 'variance', plain: 'How spread out numbers are: the average squared distance from the mean.', note: 'math/descriptive-statistics', week: 3 },
  { id: 'standard-deviation', term: 'standard deviation', plain: 'The square root of the variance, so it is in the same units as the data.', note: 'math/descriptive-statistics', week: 3 },
  { id: 'normal-distribution', term: 'normal distribution', plain: 'The bell curve: most values near the middle, few far away.', note: 'math/distributions-expectation', week: 3 },
  { id: 'bayes', term: 'Bayes’ theorem', plain: 'A rule for updating how likely something is after seeing new evidence.', note: 'math/probability-bayes', week: 3 },

  // ---- more ML words ----
  { id: 'regularization', term: 'regularization', plain: 'Anything that discourages a model from fitting the training data too closely, usually a penalty on large parameters.', note: 'ml/regularization', week: 3 },
  { id: 'bias-term', term: 'bias (intercept)', plain: 'The parameter a model adds regardless of the input: where the line crosses the axis. Not the same as “bias” in bias–variance.', note: 'ml/linear-regression', week: 1 },
  { id: 'bias-variance', term: 'bias–variance trade-off', plain: 'Simple models miss the pattern (bias); flexible models chase the noise (variance). You balance the two.', note: 'ml/overfitting-bias-variance', week: 2 },
  { id: 'feature-scaling', term: 'feature scaling', plain: 'Putting all features on a similar range so that no feature dominates just because its numbers are bigger.', note: 'ml/feature-scaling-encoding', week: 1 },
  { id: 'one-hot', term: 'one-hot encoding', plain: 'Turning a category into a list of 0s with a single 1 in the slot for that category.', note: 'ml/feature-scaling-encoding', week: 1 },
  { id: 'accuracy', term: 'accuracy', plain: 'The fraction of guesses that were right.', note: 'ml/classification-metrics', week: 3 },
  { id: 'metric', term: 'metric', plain: 'The number you actually care about and report, such as accuracy. Often different from the loss the optimizer minimises.', note: 'ml/what-is-machine-learning', week: 1 },
  { id: 'knn', term: 'k-nearest neighbours (kNN)', plain: 'Guess by looking at the k most similar examples and copying their answers.', note: 'ml/knn-kmeans', week: 4 },
  { id: 'k-means', term: 'k-means', plain: 'Split examples into k groups so that each example is close to the centre of its group.', note: 'ml/knn-kmeans', week: 4 },
  { id: 'pca', term: 'PCA', plain: 'Squash many features into a few new ones that keep as much of the spread as possible.', note: 'ml/pca', week: 4 },
  { id: 'data-leakage', term: 'data leakage', plain: 'Information from the test examples sneaking into training, which makes scores look better than they really are.', note: 'ml/imbalance-leakage', week: 4 },

  // ---- deep learning words ----
  { id: 'neural-network', term: 'neural network', plain: 'A model built from layers, each layer multiplying by a matrix of weights and then bending the result with a simple curve.', note: 'dl/what-is-a-neural-network', week: 5 },
  { id: 'neuron', term: 'neuron (unit)', plain: 'One small calculator inside a network: a weighted sum of its inputs, plus a bias, passed through a simple curve.', note: 'dl/what-is-a-neural-network', week: 5 },
  { id: 'layer', term: 'layer', plain: 'A group of neurons that all read the same inputs. A network is layers in a row.', note: 'dl/what-is-a-neural-network', week: 5 },
  { id: 'activation', term: 'activation function', plain: 'The simple curve applied after each weighted sum, such as ReLU (zero out negatives). Without it, stacked layers would collapse into one line.', note: 'dl/what-is-a-neural-network', week: 5 },
  { id: 'relu', term: 'ReLU', plain: 'The curve that keeps positive numbers and turns negatives into 0. The most common activation function.', note: 'dl/what-is-a-neural-network', week: 5 },
  { id: 'dropout', term: 'dropout', plain: 'Randomly switching off some neurons during training so the network cannot rely on any one of them.', note: 'dl/normalization-dropout', week: 6 },
  { id: 'batchnorm', term: 'BatchNorm / LayerNorm', plain: 'Rescaling the numbers inside a network so each layer sees inputs on a steady range.', note: 'dl/normalization-dropout', week: 6 },
  { id: 'adam', term: 'Adam', plain: 'A popular optimizer: gradient descent with a memory of past steps and a separate step size per parameter.', note: 'dl/optimizers', week: 6 },
  { id: 'gradient-clipping', term: 'gradient clipping', plain: 'If the gradient gets too long, shrink it before taking the step, so one bad batch cannot throw training off.', note: 'dl/optimizers', week: 6 },
  { id: 'kv-cache', term: 'KV cache', plain: 'Memory where a language model keeps the key and value vectors of earlier tokens so it does not recompute them for every new word.', note: 'modern-llm-stack/kv-cache', week: 10 },
  { id: 'lora', term: 'LoRA', plain: 'A cheap way to adapt a big model: freeze its weights and learn a small correction written as the product of two thin matrices.', note: 'modern-llm-stack/lora-qlora', week: 10 },
  { id: 'fine-tuning', term: 'fine-tuning', plain: 'Taking a model that is already trained and training it a little more on your own data.', note: 'llm-internals/classification-finetuning', week: 9 },
  { id: 'rag', term: 'RAG', plain: 'Retrieval-augmented generation: look up relevant documents first, then let the language model answer using them.', note: 'rag/rag-pipeline', week: 11 },
];

export const glossaryById = Object.fromEntries(glossary.map((g) => [g.id, g]));
