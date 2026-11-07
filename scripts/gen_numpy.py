# Generates src/data/numpy.ts. Every example is executed here, so the printed
# output in the reference is real output from NumPy, not typed by hand.
import io, json, contextlib, sys, traceback
import numpy as np

D = "https://numpy.org/doc/stable/reference/generated/"
R = "https://numpy.org/doc/stable/reference/random/generated/"
U = "https://numpy.org/doc/stable/user/"

groups = [
  {"id": "start", "title": "Arrays: making them", "intro": "NumPy is the library every piece of ML code in these notes uses. Its one data type is the array: a grid of numbers of one type, stored tightly in memory, with every math operation written once for the whole grid instead of in a loop. These are the ways to make one."},
  {"id": "shape", "title": "Shape: asking and changing", "intro": "Most NumPy bugs are shape bugs. These are the tools for asking what shape an array has and changing it without changing the numbers."},
  {"id": "index", "title": "Picking elements: indexing, slicing, masks", "intro": "How to pull out one number, a row, a column, or every element that passes a test."},
  {"id": "elementwise", "title": "Math on every element", "intro": "These functions apply to every number in the array at once and return an array of the same shape. The maths notes use them on whole datasets in one line."},
  {"id": "reduce", "title": "Reductions: one number from many", "intro": "A reduction collapses an array to fewer numbers: a sum, a mean, the position of the largest. The axis argument says which direction to collapse, and it is the single most asked-about NumPy idea in interviews."},
  {"id": "linalg", "title": "Linear algebra: dot, matmul, norm, solve", "intro": "The functions behind the vector and matrix notes. Each one is a formula from those notes with the loop removed."},
  {"id": "random", "title": "Random numbers", "intro": "Fake data, shuffled splits and starting weights all need random numbers. Modern NumPy puts them behind a generator object made once with a seed, so results repeat exactly."},
  {"id": "compare", "title": "Checking and printing", "intro": "Floating-point numbers are rarely exactly equal. These are the honest ways to compare them, and a way to keep printed output short."},
]

E = []
def e(group, id, name, plain, sig, code, pitfalls, interview, doc, aliases=None, when=None):
    E.append(dict(group=group, id=id, name=name, plain=plain, sig=sig, code=code, pitfalls=pitfalls, interview=interview, doc=doc, aliases=aliases or [], when=when or ""))

# ---------------- start ----------------
e("start", "import", "import numpy as np", "Loads the library under the short name np. Every example on this page assumes this line has run.",
  "import numpy as np",
  "import numpy as np\nprint(np.__version__)",
  ["Nobody writes numpy.array; the np alias is universal, and interviewers write it too."],
  "“np is the conventional alias for NumPy; its core object is the ndarray, a fixed-type n-dimensional array with vectorised operations.”",
  U + "absolute_beginners.html")
e("start", "array", "np.array", "Turns a Python list (or list of lists) into an array. A list of numbers gives a 1-D array; a list of equal-length lists gives a 2-D array, one inner list per row.",
  "np.array(object, dtype=None)",
  "import numpy as np\nv = np.array([1, 2, 3])\nM = np.array([[1, 2, 3],\n              [4, 5, 6]])\nprint(v, v.shape, v.dtype)\nprint(M)\nprint(M.shape)\nprint(np.array([1, 2, 3], dtype=float))",
  ["Mixing an int and a float in the list makes the whole array float; mixing in a string makes everything a string.",
   "np.array([1, 2, 3]) is an array of shape (3,), not (3, 1) and not (1, 3). The matrices note explains why that matters."],
  "“np.array copies a Python sequence into a contiguous, single-dtype ndarray; nested lists become extra dimensions.”",
  D + "numpy.array.html")
e("start", "arange", "np.arange", "Numbers from a start up to but not including a stop, in steps. Like Python's range, but it returns an array and allows fractional steps.",
  "np.arange(start, stop, step)",
  "import numpy as np\nprint(np.arange(5))\nprint(np.arange(2, 10, 2))\nprint(np.arange(0, 1, 0.25))",
  ["The stop value is never included.", "With fractional steps the number of elements can be off by one because of rounding; use np.linspace when you care about the count."],
  "“arange gives evenly spaced values by step; linspace by count.”",
  D + "numpy.arange.html")
e("start", "linspace", "np.linspace", "Exactly num numbers spread evenly from start to stop, both included. The right tool for the x-axis of a plot.",
  "np.linspace(start, stop, num=50)",
  "import numpy as np\nprint(np.linspace(0, 1, 5))\nprint(np.linspace(-2, 2, 9))",
  ["Unlike arange, the stop value is included."],
  "“linspace returns num evenly spaced samples over a closed interval; it is what you use for smooth curves.”",
  D + "numpy.linspace.html")
e("start", "zeros", "np.zeros", "An array of the given shape filled with 0.0. The usual way to make a place to accumulate results into.",
  "np.zeros(shape, dtype=float)",
  "import numpy as np\nprint(np.zeros(3))\nprint(np.zeros((2, 3)))\nprint(np.zeros(3, dtype=int))",
  ["The shape of a 2-D array is passed as one tuple, np.zeros((2, 3)), not np.zeros(2, 3)."],
  "“np.zeros allocates and zero-fills; starting a weight matrix at all zeros is a classic bug in neural nets because every neuron then learns the same thing.”",
  D + "numpy.zeros.html")
e("start", "ones", "np.ones", "An array of the given shape filled with 1.0. Often used to add a column of ones so that the bias term can live inside the weight vector.",
  "np.ones(shape, dtype=float)",
  "import numpy as np\nX = np.array([[1.0], [1.5], [2.0]])\nX1 = np.column_stack([np.ones(3), X])   # bias column first\nprint(X1)",
  ["Same tuple rule as np.zeros."],
  "“A ones column appended to X lets the intercept be learned as an ordinary weight.”",
  D + "numpy.ones.html")
e("start", "full", "np.full", "An array of the given shape filled with any value you choose.",
  "np.full(shape, fill_value)",
  "import numpy as np\nprint(np.full((2, 2), 7))\nprint(np.full(3, np.nan))",
  ["np.full(3, 7) is integer; np.full(3, 7.0) is float."],
  "“np.full is the general constant-fill constructor; zeros and ones are special cases.”",
  D + "numpy.full.html")
e("start", "like", "np.zeros_like, np.ones_like, np.full_like", "The same as zeros, ones and full, but copying the shape and type from an existing array instead of spelling them out.",
  "np.zeros_like(a)  np.ones_like(a)  np.full_like(a, value)",
  "import numpy as np\ny = np.array([200.0, 300.0, 380.0])\nprint(np.zeros_like(y))\nprint(np.ones_like(y))\nprint(np.full_like(y, y.mean()))   # a 'predict the average' baseline",
  ["full_like keeps the dtype of the template, so np.full_like(np.array([1, 2]), 2.5) silently gives [2, 2]."],
  "“The _like constructors build an array shaped like another; handy for gradients, which must match the shape of their parameter.”",
  D + "numpy.zeros_like.html")
e("start", "eye", "np.eye", "The identity matrix: ones on the diagonal, zeros elsewhere. Multiplying by it changes nothing.",
  "np.eye(n)",
  "import numpy as np\nI = np.eye(3)\nA = np.array([[2.0, 1.0, 0.0], [0.0, 1.0, 3.0], [4.0, 0.0, 1.0]])\nprint(I)\nprint(np.allclose(A @ I, A))",
  ["np.eye(3) is float, which is what you want for linear algebra."],
  "“np.eye(n) is the n×n identity; A @ I == A, and it is the starting point for ridge regression's (XᵀX + λI).”",
  D + "numpy.eye.html")
e("start", "diag", "np.diag", "Two jobs: given a 1-D array it builds a square matrix with those numbers on the diagonal; given a 2-D array it pulls the diagonal out.",
  "np.diag(v)  or  np.diag(M)",
  "import numpy as np\nprint(np.diag([1, 2, 3]))\nM = np.arange(9).reshape(3, 3)\nprint(M)\nprint(np.diag(M))",
  ["Remember it goes both ways; which way depends only on whether you pass 1-D or 2-D."],
  "“np.diag either constructs a diagonal matrix or extracts a diagonal; the trace is np.diag(M).sum().”",
  D + "numpy.diag.html")

# ---------------- shape ----------------
e("shape", "shape", ".shape, .ndim, .size, .dtype", "Four attributes to read, not call. shape is a tuple with one entry per axis (rows, columns, ...). ndim is how many axes. size is the total count of numbers. dtype is the number type.",
  "a.shape  a.ndim  a.size  a.dtype",
  "import numpy as np\nX = np.array([[1.0, 1.5, 2.0], [3.0, 4.0, 5.0]])\nprint(X.shape)\nprint(X.ndim, X.size, X.dtype)\nv = np.array([1, 2, 3])\nprint(v.shape, v.ndim)",
  ["shape is a tuple: (3,) with the comma is a 1-D array of three numbers; (3, 1) is a column; (1, 3) is a row.",
   "They are attributes, so X.shape, not X.shape()."],
  "“shape is the tuple of axis lengths; a 1-D array of length n has shape (n,), which broadcasts differently from (n, 1).”",
  D + "numpy.ndarray.shape.html")
e("shape", "reshape", ".reshape", "Rearranges the same numbers into a new shape, reading them row by row. One dimension may be -1, meaning 'work this one out'.",
  "a.reshape(new_shape)",
  "import numpy as np\na = np.arange(6)\nprint(a.reshape(2, 3))\nprint(a.reshape(3, -1))        # -1: NumPy computes 2\nprint(a.reshape(-1, 1).shape)  # a column vector",
  ["The number of elements must not change: 6 numbers cannot become (4, 2).",
   "reshape does not transpose. (2, 3) reshaped to (3, 2) is not the transpose; it re-reads the numbers row by row."],
  "“reshape reinterprets the same memory in a new shape, row-major; -1 infers one dimension. It is not a transpose.”",
  D + "numpy.ndarray.reshape.html")
e("shape", "T", ".T (transpose)", "Flips a matrix over its diagonal: rows become columns. Shape (m, n) becomes (n, m).",
  "M.T",
  "import numpy as np\nX = np.array([[1, 2, 3],\n              [4, 5, 6]])\nprint(X.T)\nprint(X.shape, '->', X.T.shape)\nv = np.array([1, 2, 3])\nprint(v.T.shape)   # unchanged: 1-D arrays have nothing to flip",
  ["Transposing a 1-D array does nothing. To get a column, use v.reshape(-1, 1) or v[:, None]."],
  "“.T swaps the two axes of a matrix; XᵀX is X.T @ X, the Gram matrix that appears in least squares.”",
  D + "numpy.ndarray.T.html")
e("shape", "newaxis", "v[:, None] and np.newaxis", "Adds a new axis of length 1. v[:, None] turns a 1-D array of length n into an (n, 1) column; v[None, :] into a (1, n) row. Needed to make broadcasting do what you mean.",
  "v[:, None]  v[None, :]  v[:, np.newaxis]",
  "import numpy as np\nv = np.array([1, 2, 3])\nprint(v[:, None].shape, v[None, :].shape)\nprint(v[:, None] * v[None, :])   # every product v_i * v_j: an outer product",
  ["None and np.newaxis are the same thing; None is shorter and what most code uses.",
   "Scikit-learn wants features as (n_samples, n_features), so a single feature must be x[:, None], not x."],
  "“Indexing with None inserts a unit axis; it is how you turn a vector into a column so broadcasting pairs the right elements.”",
  D + "numpy.newaxis.html")
e("shape", "stack", "np.stack, np.vstack, np.column_stack, np.concatenate", "Ways to glue arrays together. concatenate joins along an existing axis. vstack stacks rows on top of each other. column_stack puts 1-D arrays side by side as columns. stack creates a new axis.",
  "np.concatenate([a, b], axis=0)  np.vstack([a, b])  np.column_stack([a, b])  np.stack([a, b])",
  "import numpy as np\na = np.array([1, 2, 3]); b = np.array([4, 5, 6])\nprint(np.concatenate([a, b]))\nprint(np.vstack([a, b]))\nprint(np.column_stack([a, b]))\nprint(np.stack([a, b]).shape, np.stack([a, b], axis=1).shape)",
  ["concatenate needs the arrays to already have the axis you join on; to turn two 1-D arrays into two rows, use vstack or stack.",
   "All of them take one list of arrays, not several arguments: np.vstack([a, b]), not np.vstack(a, b)."],
  "“concatenate joins along an existing axis; stack adds one. column_stack is the quick way to build a feature matrix from separate feature vectors.”",
  D + "numpy.concatenate.html")
e("shape", "ravel", ".ravel and .flatten", "Both return the array as one long 1-D array. ravel avoids copying when it can; flatten always copies.",
  "a.ravel()  a.flatten()",
  "import numpy as np\nM = np.array([[1, 2], [3, 4]])\nprint(M.ravel())\nprint(M.flatten())",
  ["Because ravel may share memory, changing the result can change the original. Use flatten when you intend to modify."],
  "“ravel returns a flattened view when possible; flatten always returns a copy.”",
  D + "numpy.ravel.html")
e("shape", "astype", ".astype", "Returns a copy with a different number type: ints to floats, floats to ints (which truncates), booleans to 0 and 1.",
  "a.astype(dtype)",
  "import numpy as np\nmask = np.array([True, False, True])\nprint(mask.astype(int))\nprint(np.array([1, 2, 3]).astype(float))\nprint(np.array([2.9, -2.9]).astype(int))   # truncates toward zero",
  ["float to int truncates, it does not round. Use np.round first if you want rounding.",
   "Integer arrays silently truncate division results in some operations; convert to float early."],
  "“astype casts to a new dtype and returns a copy; booleans cast to 0/1, which is how a mask becomes a count via .sum().”",
  D + "numpy.ndarray.astype.html")

# ---------------- index ----------------
e("index", "slicing", "Indexing and slicing", "a[i] is one element, a[i, j] one element of a matrix, a[i] of a matrix is row i, a[:, j] is column j, a[1:3] is elements 1 and 2. Negative numbers count from the end.",
  "a[i]  M[i, j]  M[i]  M[:, j]  a[start:stop:step]",
  "import numpy as np\nM = np.array([[10, 11, 12],\n              [20, 21, 22],\n              [30, 31, 32]])\nprint(M[0, 2])\nprint(M[1])        # row 1\nprint(M[:, 0])     # column 0\nprint(M[-1])       # last row\nprint(M[0:2, 1:])  # rows 0-1, columns 1 onward\nx = np.arange(10)\nprint(x[::2], x[::-1])",
  ["Slices are views: changing M[0] changes M. Add .copy() if you need independence.",
   "M[1] is a 1-D array of shape (3,), the row with its axis dropped; M[1:2] keeps shape (1, 3)."],
  "“NumPy slicing returns views, not copies; a single-index pull drops that axis while a slice keeps it.”",
  U + "basics.indexing.html")
e("index", "mask", "Boolean masks", "Compare an array to something and you get an array of True/False. Use that as an index to keep only the elements where it is True. Summing a mask counts the Trues.",
  "a[a > 0]  (a > 0).sum()  (a > 0).mean()",
  "import numpy as np\ny_true = np.array([1, 0, 1, 1, 0])\ny_pred = np.array([1, 0, 0, 1, 1])\nprint(y_true == y_pred)\nprint((y_true == y_pred).mean())      # accuracy\nx = np.array([-2.0, 0.5, 3.0, -1.0])\nprint(x[x > 0])\nprint(np.maximum(x, 0))               # ReLU: keep positives, zero the rest",
  ["Combine conditions with & and |, each in brackets: (x > 0) & (x < 2). The words and / or raise an error on arrays."],
  "“A boolean mask is an array of the same shape; indexing with it selects True positions, and its mean is the fraction satisfying the condition, which is exactly accuracy.”",
  U + "basics.indexing.html#boolean-array-indexing")
e("index", "fancy", "Index with an array of positions", "Pass a list or array of integer positions and you get those elements, in that order. This is how a shuffled split picks rows.",
  "a[idx]  M[idx]  M[rows, cols]",
  "import numpy as np\nX = np.arange(10, 15)\nidx = np.array([3, 0, 4])\nprint(X[idx])\nrng = np.random.default_rng(0)\nperm = rng.permutation(5)\nprint(perm, X[perm])\nM = np.arange(9).reshape(3, 3)\nprint(M[[0, 2]])            # rows 0 and 2\nprint(M[[0, 1, 2], [2, 1, 0]])   # elements (0,2), (1,1), (2,0)",
  ["This returns a copy, unlike slicing.", "M[[0, 1], [1, 2]] picks the pairs (0,1) and (1,2), not a 2×2 block; for a block use M[[0, 1]][:, [1, 2]] or np.ix_."],
  "“Integer-array indexing gathers arbitrary positions and returns a copy; combined with a permutation it implements a shuffled train/test split.”",
  U + "basics.indexing.html#integer-array-indexing")
e("index", "where", "np.where", "Two uses. np.where(condition, a, b) picks from a where the condition is True and from b elsewhere. np.where(condition) alone returns the positions where it is True.",
  "np.where(cond, a, b)  np.where(cond)",
  "import numpy as np\nx = np.array([-2.0, 0.5, 3.0, -1.0])\nprint(np.where(x > 0, x, 0.0))        # ReLU again\nprint(np.where(x > 0))                # positions\nprint(np.where(x > 0)[0])",
  ["The one-argument form returns a tuple with one array per axis, so you usually want [0] at the end."],
  "“np.where is a vectorised if/else; it is how piecewise functions like ReLU or the Huber loss are written without loops.”",
  D + "numpy.where.html")
e("index", "unravel-index", "np.unravel_index", "Turns a position in a flattened array back into (row, column). Used with argmin or argmax on a 2-D grid.",
  "np.unravel_index(flat_index, shape)",
  "import numpy as np\ngrid = np.array([[5.0, 2.0], [9.0, 1.0]])\nflat = grid.argmin()\nrow, col = np.unravel_index(flat, grid.shape)\nprint(flat, int(row), int(col))",
  ["argmax/argmin on a matrix return a flat position unless you give an axis; this is the fix."],
  "“argmin flattens by default; unravel_index converts the flat index back to coordinates.”",
  D + "numpy.unravel_index.html")

# ---------------- elementwise ----------------
e("elementwise", "arith", "Element-wise arithmetic and broadcasting", "+, -, *, / and ** work number by number on arrays of the same shape. If the shapes differ, NumPy stretches the smaller one along axes of length 1 (broadcasting). A number against an array is the simplest case.",
  "a + b  a * b  a ** 2  a - a.mean(axis=0)",
  "import numpy as np\nx = np.array([1.0, 1.5, 2.0]); y = np.array([200.0, 300.0, 380.0])\nprint(180 * x + 23.33)                # a line, for every house at once\nprint(((180 * x + 23.33 - y) ** 2).mean())   # mean squared error\nX = np.array([[1.0, 100.0], [2.0, 300.0], [3.0, 500.0]])\nprint(X - X.mean(axis=0))              # (3,2) minus (2,): centre each column",
  ["* is element-wise, not matrix multiplication. Use @ for matrices.",
   "Shapes (3,) and (3, 1) broadcast to (3, 3), which is almost never what you wanted; check shapes when a result is suddenly square."],
  "“Broadcasting aligns trailing axes and stretches length-1 axes; a (n, d) matrix minus a (d,) vector subtracts per column, which is how standardisation is written in one line.”",
  U + "basics.broadcasting.html")
e("elementwise", "exp", "np.exp", "e raised to each element. Turns any number into a positive one, and small differences into big ratios. The building block of the sigmoid and softmax functions.",
  "np.exp(x)",
  "import numpy as np\nprint(np.exp(0), np.exp(1))\nz = np.array([2.0, 1.0, 0.0])\nprint(np.exp(z))\nprint(np.exp(z) / np.exp(z).sum())    # scores to percentages (softmax)\nprint(np.exp(1000))                   # overflow -> inf, with a warning",
  ["np.exp(710) is already inf in 64-bit floats. Subtract the maximum first: np.exp(z - z.max()).",
   "np.exp of an integer array returns floats, which is fine."],
  "“np.exp is the element-wise exponential; because it overflows past about 709, softmax is always computed as exp(z − max z).”",
  D + "numpy.exp.html")
e("elementwise", "log", "np.log", "The natural logarithm (base e) of each element. np.log(np.exp(x)) is x. It turns products into sums and squashes huge ranges, which is why losses are written with it.",
  "np.log(x)  np.log2(x)  np.log10(x)  np.log1p(x)",
  "import numpy as np\nprint(np.log(1), np.log(np.e))\np = np.array([0.9, 0.8, 0.95])\nprint(np.log(p).sum(), np.log(p.prod()))   # sum of logs == log of product\nprint(-np.log(np.array([0.99, 0.5, 0.01])))  # log loss: cheap when sure and right\nprint(np.log(0))                            # -inf, with a warning\nprint(np.log2(1024), np.log10(1000))",
  ["np.log is the natural log, not base 10. Use np.log10 or np.log2 explicitly when you mean them.",
   "np.log(0) is -inf and np.log of a negative is nan. Clip probabilities to [1e-12, 1] before taking logs in a loss."],
  "“np.log is the natural log; the log loss −log p needs clipping away from zero because log 0 is −inf.”",
  D + "numpy.log.html")
e("elementwise", "sqrt", "np.sqrt", "Square root of each element. Appears in the length of a vector, the standard deviation and RMSE.",
  "np.sqrt(x)",
  "import numpy as np\nv = np.array([3.0, 4.0])\nprint(np.sqrt((v ** 2).sum()))     # length of the vector\nerrors = np.array([-2.0, 1.0, 3.0])\nprint(np.sqrt((errors ** 2).mean()))   # RMSE\nprint(np.sqrt(-1))                 # nan, with a warning",
  ["Square root of a negative is nan, not an error."],
  "“np.sqrt is element-wise; the L2 norm and RMSE are both np.sqrt of a mean or sum of squares.”",
  D + "numpy.sqrt.html")
e("elementwise", "abs", "np.abs", "Absolute value of each element. Used in the L1 norm and in mean absolute error.",
  "np.abs(x)",
  "import numpy as np\nerrors = np.array([-2.0, 1.0, 3.0])\nprint(np.abs(errors))\nprint(np.abs(errors).mean())   # mean absolute error\nprint(np.abs(errors).sum())    # L1 norm",
  [],
  "“np.abs gives element-wise magnitude; MAE and the L1 norm are its mean and sum.”",
  D + "numpy.absolute.html")
e("elementwise", "round", "np.round", "Rounds each element to a number of decimals. Mostly for printing.",
  "np.round(x, decimals=0)",
  "import numpy as np\nx = np.array([0.6652, 0.2447, 0.0900])\nprint(np.round(x, 2))\nprint(np.round(2.5), np.round(3.5))   # rounds halves to the even neighbour",
  ["Halves round to the nearest even number (2.5 → 2, 3.5 → 4), the banker's rule, unlike school rounding."],
  "“np.round uses round-half-to-even; use it for display, not for turning probabilities into classes (use a threshold).”",
  D + "numpy.round.html")
e("elementwise", "maximum", "np.maximum and np.minimum", "Compares two arrays (or an array and a number) element by element and keeps the larger (or smaller) of each pair. np.maximum(x, 0) is ReLU.",
  "np.maximum(a, b)  np.minimum(a, b)",
  "import numpy as np\nx = np.array([-2.0, 0.5, 3.0, -1.0])\nprint(np.maximum(x, 0))\nprint(np.minimum(x, 1))\nprint(np.maximum(np.array([1, 5, 2]), np.array([3, 2, 2])))",
  ["np.maximum (two inputs, element-wise) is different from np.max (one input, reduces to its largest element)."],
  "“np.maximum is the element-wise max of two arrays; ReLU is np.maximum(z, 0). np.max is a reduction.”",
  D + "numpy.maximum.html")
e("elementwise", "clip", "np.clip", "Pushes every element into a range: anything below the minimum becomes the minimum, anything above the maximum becomes the maximum. Used to keep probabilities away from exact 0 and 1 before a log.",
  "np.clip(x, lo, hi)",
  "import numpy as np\np = np.array([0.0, 0.3, 1.0])\neps = 1e-12\nprint(np.clip(p, eps, 1 - eps))\nprint(-np.log(np.clip(p, eps, 1 - eps)))",
  ["Clipping gradients is the same idea applied to gradient values; clipping by norm is different and uses np.linalg.norm."],
  "“np.clip bounds values element-wise; it is the standard guard before log in a cross-entropy implementation.”",
  D + "numpy.clip.html")
e("elementwise", "trig", "np.sin, np.cos, np.arccos, np.degrees", "Trigonometry on each element, in radians. In these notes they appear only to turn a cosine similarity into an angle and to draw curves.",
  "np.cos(x)  np.sin(x)  np.arccos(c)  np.degrees(radians)",
  "import numpy as np\ncos_sim = 0.5\nprint(np.degrees(np.arccos(cos_sim)))   # the angle whose cosine is 0.5\nprint(np.cos(0), np.cos(np.pi))",
  ["Everything is in radians. np.degrees converts for humans.",
   "np.arccos of a value slightly outside [-1, 1] from rounding gives nan; clip first."],
  "“arccos of the cosine similarity gives the angle between two vectors; clip to [−1, 1] first to avoid nan from rounding.”",
  D + "numpy.arccos.html")
e("elementwise", "constants", "np.e, np.pi, np.inf, np.nan", "Four built-in values: e ≈ 2.718, π ≈ 3.14159, infinity, and 'not a number', the value NumPy uses for undefined results and missing data.",
  "np.e  np.pi  np.inf  np.nan",
  "import numpy as np\nprint(np.e, np.pi)\nprint(np.inf > 1e308, -np.inf < 0)\nprint(np.nan == np.nan)          # False! nan is not equal to anything\nx = np.array([1.0, np.nan, 3.0])\nprint(np.isnan(x), np.nanmean(x))",
  ["nan is not equal to itself, so use np.isnan to find it. Any arithmetic with nan gives nan, and x.mean() with one nan is nan; np.nanmean ignores them.",
   "np.inf - np.inf is nan."],
  "“nan propagates through arithmetic and fails equality tests; detect with np.isnan and use the nan-aware reductions.”",
  D + "numpy.nan.html")

# ---------------- reduce ----------------
e("reduce", "sum", "np.sum and .sum()", "Adds up the elements. With no axis, all of them, giving one number. axis=0 adds down the columns (collapsing rows); axis=1 adds across each row. Also written as a.sum().",
  "np.sum(a, axis=None, keepdims=False)  a.sum(axis=...)",
  "import numpy as np\nM = np.array([[1, 2, 3],\n              [4, 5, 6]])\nprint(M.sum())\nprint(M.sum(axis=0))      # column totals, shape (3,)\nprint(M.sum(axis=1))      # row totals, shape (2,)\nprint(M.sum(axis=1, keepdims=True).shape)",
  ["axis is the axis that disappears. axis=0 on a (2, 3) array gives shape (3,): the rows were collapsed.",
   "keepdims=True keeps the collapsed axis with length 1, so the result still broadcasts against the original. Softmax needs this."],
  "“axis names the dimension that is reduced away; axis=0 aggregates over rows to give per-column results. keepdims keeps the result broadcastable.”",
  D + "numpy.sum.html")
e("reduce", "mean", "np.mean and .mean()", "The average. Same axis rules as sum. The mean of a boolean array is the fraction that is True.",
  "np.mean(a, axis=None)  a.mean(axis=...)",
  "import numpy as np\nX = np.array([[1.0, 100.0], [2.0, 300.0], [3.0, 500.0]])\nprint(X.mean())\nprint(X.mean(axis=0))     # per-feature means, the thing a scaler learns\nerrors = np.array([-20.0, -30.0, -20.0])\nprint((errors ** 2).mean())   # mean squared error\nprint((np.array([1, 0, 1]) == np.array([1, 1, 1])).mean())   # accuracy",
  ["Mean over axis=0 of an (n, d) matrix gives d numbers: one per column, averaged over the rows. Get this backwards and your scaler standardises examples instead of features."],
  "“X.mean(axis=0) is the per-feature mean over examples; MSE is the mean of squared errors; the mean of a boolean mask is a proportion.”",
  D + "numpy.mean.html")
e("reduce", "median", "np.median and np.percentile", "The median is the middle value after sorting; it ignores outliers that drag the mean. np.percentile gives any cut point, such as the 25th and 75th percentiles used by the robust scaler.",
  "np.median(a)  np.percentile(a, q)",
  "import numpy as np\nincome = np.array([30, 35, 40, 45, 50, 1000])\nprint(income.mean(), np.median(income))\nprint(np.percentile(income, [25, 50, 75]))",
  ["With an even count the median is the average of the two middle values."],
  "“The median is robust to outliers where the mean is not; the IQR from np.percentile(x, [25, 75]) drives robust scaling.”",
  D + "numpy.median.html")
e("reduce", "std", "np.std, np.var and .std()", "Spread. Variance is the mean squared distance from the mean; standard deviation is its square root, in the original units. Both take axis.",
  "a.std(axis=None, ddof=0)  a.var(...)",
  "import numpy as np\nx = np.array([2.0, 4.0, 4.0, 4.0, 5.0, 5.0, 7.0, 9.0])\nprint(x.var(), x.std())\nprint(x.std(ddof=1))     # the 'sample' version divides by n-1\nX = np.array([[1.0, 100.0], [2.0, 300.0], [3.0, 500.0]])\nprint((X - X.mean(axis=0)) / X.std(axis=0))   # standardisation",
  ["NumPy divides by n by default (ddof=0); pandas divides by n−1 by default. The two disagree on small data.",
   "A constant column has std 0, and dividing by it gives nan. Scalers guard against this."],
  "“np.std defaults to the population formula (ddof=0) while pandas uses the sample formula; standardisation is (X − mean) / std per feature.”",
  D + "numpy.std.html")
e("reduce", "max", "np.max, np.min, .max(), .min()", "The largest or smallest element, overall or along an axis.",
  "a.max(axis=None)  a.min(axis=None)",
  "import numpy as np\nz = np.array([[2.0, 1.0, 0.0], [5.0, 1.0, -3.0]])\nprint(z.max(), z.min())\nprint(z.max(axis=1))\nprint(z.max(axis=1, keepdims=True))\nx = np.array([1.0, 50.0, 100.0])\nprint((x - x.min()) / (x.max() - x.min()))   # min-max scaling to [0, 1]",
  ["np.max reduces one array; np.maximum compares two. They are different functions."],
  "“max/min along axis=1 with keepdims=True is the per-row maximum used to stabilise softmax.”",
  D + "numpy.max.html")
e("reduce", "argmax", "np.argmax, np.argmin, .argmax()", "The position of the largest (or smallest) element, not its value. On a matrix of class scores, argmax(axis=1) gives each row's predicted class.",
  "a.argmax(axis=None)  a.argmin(axis=None)",
  "import numpy as np\nscores = np.array([[0.1, 0.7, 0.2],\n                   [0.8, 0.1, 0.1]])\nprint(scores.argmax(axis=1))     # predicted class per row\nprint(scores.argmax())           # flat position when no axis is given\nlosses = np.array([74.1, 22.2, 41.7])\nprint(losses.argmin(), losses.min())",
  ["With no axis it returns one flat position, even on a matrix; use np.unravel_index or give an axis.",
   "Ties go to the first occurrence."],
  "“argmax returns the index of the maximum along an axis; argmax over the class axis converts probabilities to predicted labels.”",
  D + "numpy.argmax.html")
e("reduce", "sort", "np.sort and np.argsort", "np.sort returns the elements in increasing order. np.argsort returns the positions that would sort them, which is what you need to reorder a second array the same way (for example, to rank neighbours by distance).",
  "np.sort(a)  np.argsort(a)  np.argsort(a)[::-1]",
  "import numpy as np\ndist = np.array([2.5, 0.4, 1.7])\nlabels = np.array(['cat', 'dog', 'cat'])\nprint(np.sort(dist))\norder = np.argsort(dist)\nprint(order)\nprint(labels[order])          # labels of the nearest first\nprint(np.argsort(dist)[::-1][:2])   # positions of the two largest",
  ["There is no 'descending' flag; reverse with [::-1].", "np.sort returns a copy; a.sort() sorts in place and returns None."],
  "“argsort gives the permutation that sorts; indexing another array with it is how k-nearest-neighbours picks the k closest labels.”",
  D + "numpy.argsort.html")
e("reduce", "prod", "np.prod", "Multiplies all the elements together. Products of many probabilities underflow to zero, which is the reason losses use sums of logs instead.",
  "np.prod(a, axis=None)",
  "import numpy as np\np = np.array([0.9, 0.8, 0.95])\nprint(np.prod(p))\nprint(np.prod(np.full(1000, 0.001)))      # underflows to exactly 0\nprint(np.log(np.full(1000, 0.001)).sum())   # fine in log space",
  ["Products of many numbers below 1 underflow to 0; work in logs."],
  "“np.prod demonstrates underflow: a thousand probabilities of 0.001 multiply to 0, so likelihoods are summed in log space.”",
  D + "numpy.prod.html")

# ---------------- linalg ----------------
e("linalg", "dot", "np.dot", "The dot product of two vectors: multiply matching elements and add. Also written v @ w. For 2-D inputs it does matrix multiplication, but @ is clearer for that.",
  "np.dot(a, b)  a @ b",
  "import numpy as np\nw = np.array([180.0, 1.0]); x = np.array([1.5, 23.33])\nprint(np.dot(w, x), w @ x, (w * x).sum())   # three spellings of one thing\nu = np.array([1.0, 0.0]); v = np.array([0.0, 1.0])\nprint(u @ v)        # perpendicular -> 0",
  ["np.dot(a, b) with two 1-D arrays is a number. With 2-D arrays it multiplies matrices; prefer @ there so the reader knows what you meant."],
  "“The dot product is Σ wᵢxᵢ, written w @ x; a linear model's prediction is a dot product of weights and features plus a bias.”",
  D + "numpy.dot.html")
e("linalg", "matmul", "@ and np.matmul", "Matrix multiplication. The inner dimensions must match: (m, n) @ (n, p) gives (m, p). Each output entry is a dot product of a row of the left matrix with a column of the right one.",
  "A @ B  np.matmul(A, B)",
  "import numpy as np\nX = np.array([[1.0, 1.0], [1.0, 1.5], [1.0, 2.0]])   # 3 houses, bias column + size\nw = np.array([23.33, 180.0])\nprint(X @ w)                 # (3,2) @ (2,) -> (3,): all predictions at once\nA = np.array([[1, 2], [3, 4]]); B = np.array([[0, 1], [1, 0]])\nprint(A @ B)\nprint(B @ A)                 # order matters\nprint(A * B)                 # NOT matrix multiplication",
  ["* is element-wise. @ is matrix multiplication. Mixing them up is the most common NumPy bug in ML code.",
   "Shape error 'shapes (3,2) and (3,2) not aligned' means the inner dimensions differ; transpose one side.",
   "A @ B is not B @ A in general."],
  "“@ performs matrix multiplication with the (m,n)(n,p)→(m,p) rule; a layer of a neural net is X @ W + b, one dot product per output per example.”",
  D + "numpy.matmul.html")
e("linalg", "linalg-norm", "np.linalg.norm", "The length of a vector. By default the ordinary Euclidean length (square root of the sum of squares, the L2 norm). ord=1 gives the L1 norm (sum of absolute values). With axis it gives the length of every row or column.",
  "np.linalg.norm(v)  np.linalg.norm(v, ord=1)  np.linalg.norm(M, axis=1)",
  "import numpy as np\nv = np.array([3.0, 4.0])\nprint(np.linalg.norm(v))\nprint(np.linalg.norm(v, ord=1), np.linalg.norm(v, ord=np.inf))\na = np.array([1.0, 2.0]); b = np.array([4.0, 6.0])\nprint(np.linalg.norm(a - b))              # distance between two points\nprint(a @ b / (np.linalg.norm(a) * np.linalg.norm(b)))   # cosine similarity\nE = np.array([[3.0, 4.0], [1.0, 0.0]])\nprint(np.linalg.norm(E, axis=1))          # length of each row\nprint(E / np.linalg.norm(E, axis=1, keepdims=True))   # unit rows",
  ["On a matrix with no axis it returns the Frobenius norm (all entries squared, summed, rooted), not a per-row result.",
   "Distance is the norm of the difference; cosine similarity is the dot product divided by both norms."],
  "“np.linalg.norm defaults to L2; Euclidean distance is norm(a − b), cosine similarity is a·b / (‖a‖‖b‖), and normalising rows uses axis=1 with keepdims.”",
  D + "numpy.linalg.norm.html")
e("linalg", "linalg-inv", "np.linalg.inv", "The inverse of a square matrix: the matrix that undoes it, so that A @ inv(A) is the identity. Appears in the closed-form least-squares formula. In real code you rarely call it; solve or lstsq are more accurate.",
  "np.linalg.inv(A)",
  "import numpy as np\nA = np.array([[2.0, 1.0], [1.0, 3.0]])\nAi = np.linalg.inv(A)\nprint(Ai)\nprint(np.allclose(A @ Ai, np.eye(2)))\ntry:\n    np.linalg.inv(np.array([[1.0, 2.0], [2.0, 4.0]]))   # rows are multiples: no inverse\nexcept np.linalg.LinAlgError as err:\n    print('LinAlgError:', err)",
  ["A matrix whose rows (or columns) are multiples of each other has no inverse; inv raises LinAlgError. In regression this means two features carry the same information.",
   "inv(XᵀX) @ Xᵀ @ y works on paper; np.linalg.lstsq is the numerically safe way to get the same answer."],
  "“inv exists only for full-rank square matrices; for least squares prefer solve or lstsq over forming the inverse explicitly.”",
  D + "numpy.linalg.inv.html")
e("linalg", "linalg-solve", "np.linalg.solve", "Solves A x = b for x without computing an inverse. Faster and more accurate than inv(A) @ b.",
  "np.linalg.solve(A, b)",
  "import numpy as np\nA = np.array([[2.0, 1.0], [1.0, 3.0]]); b = np.array([3.0, 5.0])\nx = np.linalg.solve(A, b)\nprint(x)\nprint(np.allclose(A @ x, b))",
  ["A must be square and invertible; for tall matrices (more equations than unknowns) use lstsq."],
  "“solve(A, b) is the right way to compute A⁻¹b; the normal equations of linear regression are solve(XᵀX, Xᵀy).”",
  D + "numpy.linalg.solve.html")
e("linalg", "linalg-lstsq", "np.linalg.lstsq", "Least squares: finds the weights that make X @ w as close as possible to y. This is linear regression in one call, and it works even when the exact solution does not exist.",
  "w, residuals, rank, sv = np.linalg.lstsq(X, y, rcond=None)",
  "import numpy as np\nx = np.array([1.0, 1.5, 2.0]); y = np.array([200.0, 300.0, 380.0])\nX = np.column_stack([np.ones(3), x])          # bias column, then size\nw, res, rank, sv = np.linalg.lstsq(X, y, rcond=None)\nprint(np.round(w, 2))         # [b, w] = [23.33, 180]\nprint(res / 3)                # sum of squared residuals / n = MSE",
  ["It returns four things; the weights are the first. Pass rcond=None to silence the deprecation warning.",
   "Remember the column of ones, or you are fitting a line through the origin."],
  "“lstsq solves min‖Xw − y‖² via SVD, which is numerically stable even when XᵀX is nearly singular.”",
  D + "numpy.linalg.lstsq.html")
e("linalg", "linalg-rank", "np.linalg.matrix_rank", "How many independent rows (or columns) a matrix has. A feature matrix with rank less than its number of columns has a redundant feature, and XᵀX cannot be inverted.",
  "np.linalg.matrix_rank(M)",
  "import numpy as np\nX = np.array([[1.0, 2.0], [2.0, 4.0], [3.0, 6.0]])   # column 2 = 2 x column 1\nprint(np.linalg.matrix_rank(X))\nX2 = np.array([[1.0, 2.0], [2.0, 5.0], [3.0, 6.0]])\nprint(np.linalg.matrix_rank(X2))",
  ["Rank is computed numerically; a column that is almost a multiple of another still counts as independent but makes the fit unstable."],
  "“Rank below the number of features means perfect multicollinearity: the least-squares solution is not unique and inv(XᵀX) fails.”",
  D + "numpy.linalg.matrix_rank.html")
e("linalg", "linalg-error", "np.linalg.LinAlgError", "The error NumPy raises when a linear-algebra operation is impossible, most often inverting a singular matrix. Catch it when fitting on data that may have duplicate features.",
  "try: ... except np.linalg.LinAlgError:",
  "import numpy as np\nS = np.array([[1.0, 2.0], [2.0, 4.0]])\ntry:\n    np.linalg.inv(S)\nexcept np.linalg.LinAlgError as err:\n    print('cannot invert:', err)",
  [],
  "“LinAlgError on inv signals a singular matrix; in regression that is a sign of collinear features, fixed by dropping one or adding a ridge penalty.”",
  D + "numpy.linalg.LinAlgError.html")
e("linalg", "linalg-eig-svd", "np.linalg.eig, np.linalg.eigh, np.linalg.svd", "Eigen-decomposition and the singular value decomposition. You will meet them in week 4 for PCA: the eigenvectors of the covariance matrix are the directions of most spread. eigh is for symmetric matrices (like covariance) and returns sorted real results.",
  "vals, vecs = np.linalg.eigh(C)  U, s, Vt = np.linalg.svd(X)",
  "import numpy as np\nX = np.array([[2.0, 0.0], [0.0, 1.0], [-2.0, 0.0], [0.0, -1.0]])\nC = X.T @ X / len(X)           # covariance (data already centred)\nvals, vecs = np.linalg.eigh(C)\nprint(vals)                    # variances along each direction, ascending\nprint(vecs)                    # the directions, as columns\nU, s, Vt = np.linalg.svd(X, full_matrices=False)\nprint(s ** 2 / len(X))         # same variances from the SVD",
  ["eigh returns eigenvalues in ascending order; PCA wants the largest first, so reverse.",
   "Use eigh, not eig, on symmetric matrices: it is faster and never returns tiny imaginary parts."],
  "“PCA is the eigendecomposition of the covariance matrix, equivalently the SVD of the centred data; eigh is the right call for symmetric matrices.”",
  D + "numpy.linalg.eigh.html")

# ---------------- random ----------------
e("random", "default-rng", "np.random.default_rng", "Makes a random-number generator. Give it a seed (any integer) and every run produces the same 'random' numbers, which is what makes experiments repeatable. All the rng.* calls below come from this object.",
  "rng = np.random.default_rng(seed)",
  "import numpy as np\nrng = np.random.default_rng(0)\nprint(rng.random(3))\nrng2 = np.random.default_rng(0)\nprint(rng2.random(3))      # identical: same seed, same numbers\nprint(np.random.default_rng(1).random(3))   # different seed",
  ["The old style, np.random.seed(0) and np.random.randn(...), still works but is discouraged; new code uses a Generator.",
   "Make one generator and pass it around; making a new one with the same seed inside a loop gives the same numbers every iteration."],
  "“default_rng returns a Generator with its own state; seeding it makes shuffles, splits and initialisations reproducible.”",
  R + "numpy.random.default_rng.html")
e("random", "rng-normal", "rng.normal", "Random numbers from a bell curve with the given mean and standard deviation. Used for noise in fake data and for starting weights.",
  "rng.normal(loc=0.0, scale=1.0, size=None)",
  "import numpy as np\nrng = np.random.default_rng(0)\nnoise = rng.normal(0, 1, size=5)\nprint(np.round(noise, 3))\nW = rng.normal(0, 0.01, size=(2, 3))    # small starting weights\nprint(W.shape)\nbig = rng.normal(10, 2, size=100_000)\nprint(round(big.mean(), 2), round(big.std(), 2))",
  ["The second argument is the standard deviation, not the variance.", "rng.standard_normal(size) is the shortcut for mean 0, std 1."],
  "“rng.normal(mean, std, size) samples a Gaussian; weight initialisation draws from a normal with a small, layer-dependent std.”",
  R + "numpy.random.Generator.normal.html")
e("random", "rng-uniform", "rng.uniform", "Random numbers spread evenly between low and high. rng.random() is the same on [0, 1).",
  "rng.uniform(low=0.0, high=1.0, size=None)",
  "import numpy as np\nrng = np.random.default_rng(0)\nx = rng.uniform(0, 10, size=5)\nprint(np.round(x, 2))\nprint(rng.uniform(-1, 1, size=(2, 2)).shape)",
  ["high is excluded, like a range."],
  "“rng.uniform samples evenly on [low, high); it is the usual source of synthetic x values.”",
  R + "numpy.random.Generator.uniform.html")
e("random", "rng-integers", "rng.integers", "Random whole numbers from low up to (not including) high. For random labels or random indices.",
  "rng.integers(low, high=None, size=None)",
  "import numpy as np\nrng = np.random.default_rng(0)\nprint(rng.integers(0, 2, size=10))     # ten coin flips as 0/1\nprint(rng.integers(0, 100, size=3))",
  ["high is excluded; rng.integers(0, 2) gives 0 or 1, never 2."],
  "“rng.integers draws integers on [low, high); use it for random labels or index sampling.”",
  R + "numpy.random.Generator.integers.html")
e("random", "rng-permutation", "rng.permutation and rng.shuffle", "permutation returns the numbers 0..n−1 in random order (or a shuffled copy of an array). shuffle reorders an array in place. Either one is the heart of a train/test split.",
  "rng.permutation(n)  rng.shuffle(a)",
  "import numpy as np\nrng = np.random.default_rng(0)\nidx = rng.permutation(10)\nprint(idx)\ntrain, test = idx[:8], idx[8:]\nprint(train, test)               # 80/20 split of row positions\na = np.arange(5); rng.shuffle(a); print(a)",
  ["Shuffle the index, then apply the same index to X and y; shuffling X and y separately breaks their pairing."],
  "“A permutation of row indices, applied to both X and y, is the simplest correct random split.”",
  R + "numpy.random.Generator.permutation.html")
e("random", "rng-choice", "rng.choice", "Picks elements at random from an array, with or without replacement. Bootstrap samples and random mini-batches both use it.",
  "rng.choice(a, size=None, replace=True, p=None)",
  "import numpy as np\nrng = np.random.default_rng(0)\nprint(rng.choice(5, size=3, replace=False))   # 3 distinct positions out of 5\nprint(rng.choice(['a', 'b', 'c'], size=5))     # with replacement\nprint(rng.choice([0, 1], size=10, p=[0.9, 0.1]))   # weighted",
  ["replace=True by default, so repeats are possible unless you say otherwise."],
  "“rng.choice samples with or without replacement; bootstrapping is choice with replace=True and size=n.”",
  R + "numpy.random.Generator.choice.html")

# ---------------- compare ----------------
e("compare", "isclose", "np.isclose and np.allclose", "Floating-point arithmetic has rounding error, so 0.1 + 0.2 is not 0.3. isclose compares element by element within a small tolerance and returns a boolean array; allclose returns a single True if every element is close.",
  "np.isclose(a, b)  np.allclose(a, b, rtol=1e-5, atol=1e-8)",
  "import numpy as np\nprint(0.1 + 0.2 == 0.3)\nprint(np.isclose(0.1 + 0.2, 0.3))\nA = np.array([[2.0, 1.0], [1.0, 3.0]])\nprint(np.allclose(A @ np.linalg.inv(A), np.eye(2)))\nprint(np.isclose(np.log(np.array([0.9, 0.8, 0.95])).sum(), np.log(0.684), atol=1e-3))",
  ["Never test floats with ==. Every 'check it numerically' line in these notes uses isclose or allclose.",
   "The default tolerance is relative, so comparing against 0 needs an explicit atol."],
  "“Compare floats with allclose, not ==; it checks |a − b| ≤ atol + rtol·|b|.”",
  D + "numpy.isclose.html")
e("compare", "set-printoptions", "np.set_printoptions", "Controls how arrays print: number of decimals, whether to use scientific notation, how many elements before NumPy abbreviates with '...'.",
  "np.set_printoptions(precision=3, suppress=True)",
  "import numpy as np\nx = np.array([0.66524096, 0.24472847, 0.09003057, 1e-10])\nprint(x)\nnp.set_printoptions(precision=3, suppress=True)\nprint(x)",
  ["It is global for the session; call it once at the top of a notebook."],
  "“set_printoptions(precision, suppress) keeps printed arrays readable; it changes display only, never the values.”",
  D + "numpy.set_printoptions.html")
e("compare", "fill", ".fill and in-place updates", "a.fill(value) sets every element to one value without making a new array. a += b, a *= 2 and a[mask] = 0 also change the array in place. Useful in training loops where a gradient array is reused.",
  "a.fill(0)  a += b  a[mask] = value",
  "import numpy as np\ng = np.ones(3)\ng.fill(0)\nprint(g)\nw = np.array([1.0, 2.0])\nw -= 0.1 * np.array([10.0, 20.0])      # one gradient-descent step, in place\nprint(w)\nx = np.array([-1.0, 2.0, -3.0]); x[x < 0] = 0; print(x)",
  ["In-place on an integer array with a float value truncates: np.array([1, 2]) -= 0.5 raises an error in modern NumPy, which is a feature."],
  "“In-place updates avoid allocating a new array each step; w -= lr * grad is the literal gradient-descent update.”",
  D + "numpy.ndarray.fill.html")

# -------- run every example and capture its output --------
import warnings
out_entries = []
for ent in E:
    buf = io.StringIO()
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        with contextlib.redirect_stdout(buf):
            try:
                np.set_printoptions()  # reset
                exec(compile(ent["code"], ent["id"], "exec"), {})
            except Exception as ex:
                print("ERROR:", type(ex).__name__, ex)
    ent["output"] = buf.getvalue().rstrip("\n")
    out_entries.append(ent)
    if "ERROR" in ent["output"]:
        print("!!", ent["id"], ent["output"], file=sys.stderr)

np.set_printoptions()
ts = ["// Generated by scratchpad/gen_numpy.py. Every `output` below is real output from NumPy " + np.__version__ + ".",
      "// Do not edit outputs by hand: change the generator and rerun it.",
      "",
      "export interface NumpyGroup { id: string; title: string; intro: string }",
      "export interface NumpyEntry {",
      "  group: string;",
      "  /** Anchor id on the /numpy/ page; CodeBlock links np.* calls to it. */",
      "  id: string;",
      "  name: string;",
      "  plain: string;",
      "  sig: string;",
      "  code: string;",
      "  output: string;",
      "  pitfalls: string[];",
      "  interview: string;",
      "  doc: string;",
      "}",
      "",
      "export const numpyGroups: NumpyGroup[] = " + json.dumps(groups, ensure_ascii=False, indent=2) + ";",
      "",
      "export const numpyEntries: NumpyEntry[] = " + json.dumps([{k: v for k, v in x.items() if k not in ('aliases', 'when')} for x in out_entries], ensure_ascii=False, indent=2) + ";",
      "",
      "/** Which spelling in code links to which entry. Longest names must be tried first. */",
      "export const numpyLinks: Record<string, string> = {",
]
links = {
 "np.array":"array","np.arange":"arange","np.linspace":"linspace","np.zeros_like":"like","np.ones_like":"like","np.full_like":"like",
 "np.zeros":"zeros","np.ones":"ones","np.full":"full","np.eye":"eye","np.diag":"diag",
 "np.newaxis":"newaxis","np.stack":"stack","np.vstack":"stack","np.hstack":"stack","np.column_stack":"stack","np.concatenate":"stack",
 "np.where":"where","np.unravel_index":"unravel-index",
 "np.exp":"exp","np.log1p":"log","np.log2":"log","np.log10":"log","np.log":"log","np.sqrt":"sqrt","np.abs":"abs","np.round":"round",
 "np.maximum":"maximum","np.minimum":"maximum","np.clip":"clip","np.sin":"trig","np.cos":"trig","np.arccos":"trig","np.degrees":"trig",
 "np.e":"constants","np.pi":"constants","np.inf":"constants","np.nan":"constants","np.isnan":"constants","np.nanmean":"constants",
 "np.sum":"sum","np.mean":"mean","np.median":"median","np.percentile":"median","np.std":"std","np.var":"std","np.max":"max","np.min":"max",
 "np.argmax":"argmax","np.argmin":"argmax","np.sort":"sort","np.argsort":"sort","np.prod":"prod",
 "np.dot":"dot","np.matmul":"matmul","np.linalg.norm":"linalg-norm","np.linalg.inv":"linalg-inv","np.linalg.solve":"linalg-solve",
 "np.linalg.lstsq":"linalg-lstsq","np.linalg.matrix_rank":"linalg-rank","np.linalg.LinAlgError":"linalg-error",
 "np.linalg.eigh":"linalg-eig-svd","np.linalg.eig":"linalg-eig-svd","np.linalg.svd":"linalg-eig-svd",
 "np.random.default_rng":"default-rng","rng.normal":"rng-normal","rng.standard_normal":"rng-normal","rng.uniform":"rng-uniform","rng.random":"rng-uniform",
 "rng.integers":"rng-integers","rng.permutation":"rng-permutation","rng.shuffle":"rng-permutation","rng.choice":"rng-choice",
 "np.isclose":"isclose","np.allclose":"isclose","np.set_printoptions":"set-printoptions",
 ".reshape":"reshape",".shape":"shape",".ndim":"shape",".size":"shape",".dtype":"shape",".T":"T",".ravel":"ravel",".flatten":"ravel",".astype":"astype",
 ".sum":"sum",".mean":"mean",".std":"std",".var":"std",".max":"max",".min":"max",".argmax":"argmax",".argmin":"argmax",".fill":"fill",".prod":"prod",".dot":"dot",".round":"round",".clip":"clip",
 "@":"matmul","[:, None]":"newaxis","[None, :]":"newaxis",
}
ids = {x["id"] for x in E}
for k, v in links.items():
    assert v in ids, (k, v)
for k in sorted(links, key=len, reverse=True):
    ts.append("  " + json.dumps(k) + ": " + json.dumps(links[k]) + ",")
ts.append("};")
ts.append("")
open(sys.argv[1], "w").write("\n".join(ts) + "\n")
print(len(E), "entries written")
