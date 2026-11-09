# Generates the scikit-learn and Python-tools reference pages' data:
#   src/data/sklearn.ts   (page /ai/sklearn/)
#   src/data/pytools.ts   (page /ai/python/)
# Every example is executed here, so each printed output is real. Plotting examples
# are saved as images to public/ai/ref/<id>.png.
#
# Run from the site folder, in an environment with numpy, scikit-learn, pandas, matplotlib:
#   python scripts/gen_reference.py
import io, json, contextlib, sys, traceback, warnings, os
import numpy as np
import sklearn, pandas as pd, matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SK = "https://scikit-learn.org/stable/modules/generated/"
SKU = "https://scikit-learn.org/stable/"
PY = "https://docs.python.org/3/"
MPL = "https://matplotlib.org/stable/api/_as_gen/"
PD = "https://pandas.pydata.org/docs/reference/api/"


def entry(store, group, id, name, plain, sig, code, pitfalls, interview, doc, taught=None, image=False):
    store.append(dict(group=group, id=id, name=name, plain=plain, sig=sig, code=code, pitfalls=pitfalls,
                      interview=interview, doc=doc, taught=taught or "", image=image))


# ============================================================================ scikit-learn
skGroups = [
  {"id": "pattern", "title": "The one pattern: fit, then predict", "intro": "scikit-learn is the standard Python library for classical machine learning. Every model and every preprocessing step in it is an object with the same few methods, so once you know fit, predict and transform you can read any scikit-learn code."},
  {"id": "data", "title": "Built-in datasets", "intro": "Small real datasets that ship with the library, used throughout the notes so that every example runs without downloading anything by hand."},
  {"id": "split", "title": "Splitting the data", "intro": "Tools for holding data back from the model so that you can measure it honestly. The idea is taught in the first ML note; these are the functions that do it."},
  {"id": "models", "title": "Models", "intro": "The models the notes use. Each one is a different rule for turning features into a prediction, but all of them are used the same way: make it, fit it, predict with it."},
  {"id": "prep", "title": "Preprocessing: changing the features", "intro": "Steps that change the input columns before the model sees them: rescaling numbers, turning categories into numbers, filling gaps, adding powers of a feature. They learn what they need from the training data with fit and apply it with transform."},
  {"id": "combine", "title": "Chaining steps together", "intro": "Real code rarely uses one step on its own. These tools glue preprocessing and a model into a single object, so that the right thing happens to training data and to new data automatically."},
  {"id": "metrics", "title": "Scoring predictions", "intro": "Functions that compare the true answers with the predictions and return one number. They always take the true answers first."},
]
SKE = []
e = lambda *a, **k: entry(SKE, *a, **k)

e("pattern", "import-sklearn", "from sklearn.… import …",
  "scikit-learn is imported as sklearn and split into modules by job: linear_model for linear models, preprocessing for feature changes, metrics for scores, and so on. You import the one class or function you need from its module.",
  "from sklearn.<module> import <Name>",
  "from sklearn.linear_model import LinearRegression     # a model\nfrom sklearn.preprocessing import StandardScaler      # a preprocessing step\nfrom sklearn.metrics import mean_squared_error        # a score\nimport sklearn\nprint(sklearn.__version__)",
  ["The package is installed as scikit-learn (pip install scikit-learn) but imported as sklearn.",
   "Class names are written in CapitalCase (LinearRegression) and are made with (); function names are lower_case (train_test_split) and are called directly."],
  "“scikit-learn organises estimators by module, linear_model, preprocessing, metrics, model_selection, and every estimator shares the same fit / predict / transform interface.”",
  SKU + "getting_started.html", taught="ml/what-is-machine-learning")

e("pattern", "fit-predict", ".fit(X, y) and .predict(X)",
  "Every model follows the same two steps. fit(X, y) is training: it looks at the inputs X and the right answers y and sets the model's parameters. predict(X) is inference: it uses those parameters to guess answers for inputs, including ones it has never seen. X is always 2-D, one row per example and one column per feature; y is 1-D, one answer per row.",
  "model = SomeModel(settings)\nmodel.fit(X_train, y_train)\npredictions = model.predict(X_new)",
  "import numpy as np\nfrom sklearn.linear_model import LinearRegression\n\nX = np.array([[1.0], [1.5], [2.0]])   # 3 houses, 1 feature (size): shape (3, 1)\ny = np.array([200.0, 300.0, 380.0])   # 3 prices: shape (3,)\n\nmodel = LinearRegression()   # 1. make the model (knobs not set yet)\nmodel.fit(X, y)              # 2. train: set the knobs from the data\nprint(model.predict([[1.8]]))   # 3. predict for a new house",
  ["X must be 2-D even with one feature: [[1.0], [1.5]], not [1.0, 1.5]. A 1-D X gives the error 'Expected 2D array, got 1D array instead'.",
   "fit returns the model itself, so model = LinearRegression().fit(X, y) makes and trains it in one line. That is why you will see that form often.",
   "Calling predict before fit raises a NotFittedError."],
  "“Every scikit-learn estimator has fit to learn parameters from training data and predict to apply them; X is (n_samples, n_features).”",
  SKU + "getting_started.html#fitting-and-predicting-estimator-basics", taught="ml/what-is-machine-learning")

e("pattern", "learned-attributes", ".coef_ and .intercept_",
  "After fit, a model stores what it learned in attributes whose names end with an underscore. For a linear model, coef_ holds the weights (one per feature) and intercept_ holds the bias. The trailing underscore is a convention meaning 'this was learned from data, it does not exist before fit'.",
  "model.coef_      model.intercept_",
  "import numpy as np\nfrom sklearn.linear_model import LinearRegression\n\nX = np.array([[1.0], [1.5], [2.0]])\ny = np.array([200.0, 300.0, 380.0])\nmodel = LinearRegression().fit(X, y)\nprint(model.coef_)        # one weight per feature\nprint(model.intercept_)   # the bias b",
  ["coef_ is always an array, even with one feature, so the slope is model.coef_[0]."],
  "“Learned attributes end in an underscore: coef_ and intercept_ are the fitted weights and bias of a linear model.”",
  SK + "sklearn.linear_model.LinearRegression.html", taught="ml/what-is-machine-learning")

e("pattern", "transform", ".fit_transform(X) and .transform(X)",
  "Preprocessing steps (scalers, encoders, imputers) do not predict; they change the data. fit learns what they need from the training data (for a scaler: each column's mean and spread). transform applies that change. fit_transform does both in one call and is used on the training data only; new data and test data get transform alone, so they are changed with the training data's numbers.",
  "step.fit_transform(X_train)\nstep.transform(X_test)",
  "import numpy as np\nfrom sklearn.preprocessing import StandardScaler\n\nX_train = np.array([[1.0], [2.0], [3.0]])\nX_test = np.array([[4.0]])\n\nscaler = StandardScaler()\nprint(scaler.fit_transform(X_train).ravel())   # learn mean 2 and spread, then apply\nprint(scaler.transform(X_test).ravel())        # apply the SAME numbers to new data",
  ["Calling fit_transform on the test set is the classic leak: the test data then influences the preprocessing. Fit on train, transform everything else.",
   "transform returns a new array; it does not change X in place."],
  "“Transformers learn statistics with fit on the training split and apply them with transform everywhere else; fit_transform is a shortcut for the training split only.”",
  SKU + "data_transforms.html", taught="ml/feature-scaling-encoding")

e("pattern", "score", ".score(X, y)",
  "A shortcut that predicts on X and compares with y in one call. For a regression model it returns R² (1 is perfect, 0 is no better than guessing the average); for a classifier it returns accuracy, the fraction of right answers.",
  "model.score(X_test, y_test)",
  "import numpy as np\nfrom sklearn.linear_model import LinearRegression\n\nX = np.array([[1.0], [1.5], [2.0], [2.5]])\ny = np.array([200.0, 300.0, 380.0, 470.0])\nmodel = LinearRegression().fit(X, y)\nprint(round(model.score(X, y), 4))   # R² of the line on these four houses",
  ["Which number score returns depends on the model type. When you need a specific metric, call it explicitly from sklearn.metrics instead."],
  "“score is a convenience: R² for regressors, accuracy for classifiers. For anything you report, use an explicit metric.”",
  SKU + "modules/model_evaluation.html", taught="ml/linear-regression")

e("data", "toy-datasets", "load_diabetes, load_iris, load_wine",
  "Small datasets that come inside the library. With return_X_y=True each one returns two arrays: X, the features (one row per example), and y, the answers. diabetes: 442 patients, 10 measurements, y is a disease-progression score (a number). iris: 150 flowers, 4 measurements, y is the species 0, 1 or 2. wine: 178 wines, 13 chemical measurements, y is the grower 0, 1 or 2.",
  "X, y = load_diabetes(return_X_y=True)",
  "from sklearn.datasets import load_diabetes, load_iris, load_wine\n\nfor load in [load_diabetes, load_iris, load_wine]:\n    X, y = load(return_X_y=True)\n    print(load.__name__, X.shape, y.shape, y[:5])",
  ["Without return_X_y=True you get a dictionary-like object; then the arrays are data.data and data.target, and data.feature_names lists the column names."],
  "“The bundled toy datasets are for examples; return_X_y gives the feature matrix and target vector directly.”",
  SKU + "datasets/toy_dataset.html", taught="ml/what-is-machine-learning")

e("data", "california", "fetch_california_housing",
  "A larger real dataset: 20,640 districts of California from the 1990 census, 8 features (median income, house age, rooms, location and so on), and y is the median house value in units of 100,000 dollars. It is downloaded once on first use and cached.",
  "X, y = fetch_california_housing(return_X_y=True)",
  "from sklearn.datasets import fetch_california_housing\n\ndata = fetch_california_housing()\nprint(data.data.shape, data.target.shape)\nprint(data.feature_names)\nprint(data.target[:3])     # 4.526 means $452,600",
  ["The first call needs an internet connection."],
  "“California housing is the standard small regression benchmark: 20k rows, 8 numeric features.”",
  SK + "sklearn.datasets.fetch_california_housing.html", taught="ml/linear-regression")

e("split", "train-test-split", "train_test_split",
  "Shuffles the rows and cuts them into a training part and a test part. test_size=0.2 keeps 20% back for testing. random_state fixes the shuffle so you get the same split every run. It returns four arrays, always in this order: X_train, X_test, y_train, y_test.",
  "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)",
  "import numpy as np\nfrom sklearn.model_selection import train_test_split\n\nX = np.arange(20).reshape(10, 2)   # 10 examples, 2 features\ny = np.arange(10)                  # 10 answers\nX_train, X_test, y_train, y_test = train_test_split(\n    X, y, test_size=0.2, random_state=0)\nprint(X_train.shape, X_test.shape)\nprint(y_test)                      # which rows went to the test set",
  ["The order of the four results is easy to get wrong: both X parts first, then both y parts.",
   "For classification with rare classes, pass stratify=y so both parts keep the same class proportions."],
  "“train_test_split shuffles then holds out a fraction; fix random_state for reproducibility and stratify on the label for imbalanced classification.”",
  SK + "sklearn.model_selection.train_test_split.html", taught="ml/what-is-machine-learning")

e("split", "cross-val", "KFold and cross_val_score",
  "Instead of one train/test cut, cross-validation cuts the training data into k equal parts (folds), trains k times, each time holding a different fold out, and gives you k scores. Their average is a steadier estimate than one split. KFold describes how to cut; cross_val_score runs the k trainings and returns the k scores.",
  "cross_val_score(model, X, y, cv=KFold(5, shuffle=True, random_state=0))",
  "from sklearn.datasets import load_diabetes\nfrom sklearn.linear_model import LinearRegression\nfrom sklearn.model_selection import KFold, cross_val_score\n\nX, y = load_diabetes(return_X_y=True)\nfolds = KFold(n_splits=5, shuffle=True, random_state=0)\nscores = cross_val_score(LinearRegression(), X, y, cv=folds)   # R² on each held-out fold\nprint(scores.round(3))\nprint(round(scores.mean(), 3))",
  ["The model you pass is copied and refitted for every fold; the model object you passed stays untrained.",
   "Any preprocessing must be inside the model (a pipeline) or it leaks across folds."],
  "“k-fold cross-validation trains k times, each fold serving once as validation, and averages the scores for a lower-variance estimate.”",
  SK + "sklearn.model_selection.cross_val_score.html", taught="ml/data-splits-cross-validation")

e("models", "linear-regression", "LinearRegression",
  "Fits the best straight line (with many features, the best flat surface): prediction = w1·x1 + w2·x2 + … + b, with the weights chosen to make the mean squared error on the training data as small as possible. It has no settings you need to choose.",
  "LinearRegression().fit(X, y)",
  "import numpy as np\nfrom sklearn.linear_model import LinearRegression\n\nX = np.array([[1.0], [1.5], [2.0]])\ny = np.array([200.0, 300.0, 380.0])\nmodel = LinearRegression().fit(X, y)\nprint(model.coef_, round(model.intercept_, 2))\nprint(model.predict([[1.8]]).round(2))",
  ["It is ordinary least squares: no penalty on large weights. For that, see Ridge."],
  "“LinearRegression is ordinary least squares: it minimises the training MSE in closed form.”",
  SK + "sklearn.linear_model.LinearRegression.html", taught="ml/linear-regression")

e("models", "ridge", "Ridge",
  "Linear regression with a penalty for large weights. The setting alpha says how strong the penalty is: 0 is plain linear regression, bigger values pull the weights toward zero. Used when there are many features or features that move together.",
  "Ridge(alpha=1.0).fit(X, y)",
  "import numpy as np\nfrom sklearn.linear_model import LinearRegression, Ridge\n\nX = np.array([[1.0], [1.5], [2.0]])\ny = np.array([200.0, 300.0, 380.0])\nfor model in [LinearRegression(), Ridge(alpha=0.1), Ridge(alpha=10)]:\n    model.fit(X, y)\n    print(type(model).__name__, model.coef_.round(1))",
  ["The penalty depends on the size of each weight, so features must be on the same scale first, or the penalty hits some features harder than others."],
  "“Ridge adds an L2 penalty alpha·‖w‖² to least squares, shrinking weights and stabilising the fit with correlated features.”",
  SK + "sklearn.linear_model.Ridge.html", taught="ml/regularization")

e("models", "kneighbors", "KNeighborsClassifier",
  "Classifies a new example by finding the k training examples closest to it (by straight-line distance) and taking a vote among their labels. fit just stores the training data. The setting n_neighbors is k.",
  "KNeighborsClassifier(n_neighbors=5).fit(X, y)",
  "import numpy as np\nfrom sklearn.neighbors import KNeighborsClassifier\n\nX = np.array([[1, 1], [1, 2], [8, 8], [9, 8]])   # two clusters of points\ny = np.array([0, 0, 1, 1])                       # their labels\nmodel = KNeighborsClassifier(n_neighbors=3).fit(X, y)\nprint(model.predict([[2, 1], [8, 9]]))",
  ["Because it compares distances, a feature measured in large numbers (salary) drowns out one in small numbers (age) unless you scale the features first."],
  "“kNN is a lazy learner: fit stores the data and prediction is a majority vote of the k nearest training points, so feature scaling matters.”",
  SK + "sklearn.neighbors.KNeighborsClassifier.html", taught="ml/knn-kmeans")

e("models", "dummy", "DummyRegressor and DummyClassifier",
  "Baselines packaged as models: they ignore the features and always predict one thing. DummyRegressor(strategy='mean') always predicts the training average; 'median' the training median. DummyClassifier(strategy='most_frequent') always predicts the most common class.",
  "DummyRegressor(strategy=\"mean\").fit(X, y)",
  "import numpy as np\nfrom sklearn.dummy import DummyRegressor, DummyClassifier\n\nX = np.zeros((4, 1))                     # the features are ignored anyway\nmean_model = DummyRegressor(strategy=\"mean\").fit(X, [10, 12, 14, 40])\nprint(mean_model.predict(X[:1]))         # always the training mean\nmajority = DummyClassifier(strategy=\"most_frequent\").fit(X, [0, 0, 0, 1])\nprint(majority.predict(X[:1]))           # always the most common class",
  ["A dummy model still needs an X to fit and predict, only to know how many rows there are."],
  "“Dummy estimators give the baseline score, the mean or majority class, that any real model has to beat.”",
  SKU + "modules/model_evaluation.html#dummy-estimators", taught="ml/what-is-machine-learning")

e("prep", "standard-scaler", "StandardScaler",
  "Rescales each column to have mean 0 and standard deviation 1: subtract the column's average, divide by its spread. After it, a value of 1.5 means '1.5 spreads above average' in every column, so columns measured in different units become comparable.",
  "StandardScaler().fit_transform(X_train)",
  "import numpy as np\nfrom sklearn.preprocessing import StandardScaler\n\nX = np.array([[50_000, 25], [80_000, 35], [110_000, 45]], dtype=float)   # salary, age\nscaler = StandardScaler().fit(X)\nprint(scaler.mean_)                        # the averages it learned\nprint(scaler.transform(X).round(2))",
  ["Fit it on the training data only, then transform the test data with it.",
   "It uses the population standard deviation (divides by n), the same as np.std by default."],
  "“StandardScaler standardises each feature to zero mean and unit variance using training-set statistics.”",
  SK + "sklearn.preprocessing.StandardScaler.html", taught="ml/feature-scaling-encoding")

e("prep", "minmax-scaler", "MinMaxScaler",
  "Rescales each column so that its smallest training value becomes 0 and its largest becomes 1, with everything else in proportion.",
  "MinMaxScaler().fit_transform(X_train)",
  "import numpy as np\nfrom sklearn.preprocessing import MinMaxScaler\n\nX = np.array([[10.0], [20.0], [40.0]])\nscaler = MinMaxScaler().fit(X)\nprint(scaler.transform(X).ravel())\nprint(scaler.transform([[50.0]]).ravel())   # bigger than anything in training: above 1",
  ["One extreme value squashes every other value into a tiny range near 0.",
   "New data outside the training range lands outside 0 to 1."],
  "“Min-max scaling maps the training range to [0, 1]; it is sensitive to outliers, unlike standardisation or robust scaling.”",
  SK + "sklearn.preprocessing.MinMaxScaler.html", taught="ml/feature-scaling-encoding")

e("prep", "one-hot", "OneHotEncoder",
  "Turns a column of categories into several 0/1 columns, one per category. 'red', 'green', 'blue' becomes three columns, and each row has a single 1 in the column of its category. Models need numbers; this is the safe way to give them categories without inventing an order.",
  "OneHotEncoder(handle_unknown=\"ignore\").fit_transform(X_cat)",
  "import numpy as np\nfrom sklearn.preprocessing import OneHotEncoder\n\ncolors = np.array([[\"red\"], [\"green\"], [\"blue\"], [\"green\"]])   # one column, 4 rows\nencoder = OneHotEncoder(handle_unknown=\"ignore\", sparse_output=False)\nencoder.fit(colors)\nprint(encoder.categories_)\nprint(encoder.transform(colors))\nprint(encoder.transform([[\"purple\"]]))   # unseen category: all zeros",
  ["Without handle_unknown='ignore', a category that never appeared in training raises an error at prediction time.",
   "By default it returns a sparse matrix (mostly zeros stored compactly); sparse_output=False gives a normal array for printing."],
  "“One-hot encoding maps a nominal feature to indicator columns; set handle_unknown='ignore' so unseen categories do not crash inference.”",
  SK + "sklearn.preprocessing.OneHotEncoder.html", taught="ml/feature-scaling-encoding")

e("prep", "target-encoder", "TargetEncoder",
  "Replaces each category by the average answer (target) for that category in the training data, for example each city by its average house price. Useful when a column has thousands of categories and one-hot would make thousands of columns. It mixes in the overall average for rare categories and uses cross-fitting internally so a row never sees its own answer.",
  "TargetEncoder(target_type=\"continuous\").fit_transform(X_cat, y)",
  "import numpy as np\nfrom sklearn.preprocessing import TargetEncoder\n\ncity = np.array([[\"A\"], [\"A\"], [\"B\"], [\"B\"], [\"C\"], [\"C\"]] * 5)\nprice = np.array([100, 120, 300, 320, 200, 220] * 5, dtype=float)\nencoder = TargetEncoder(target_type=\"continuous\", random_state=0)\nencoder.fit(city, price)\nprint(encoder.transform([[\"A\"], [\"B\"], [\"C\"]]).ravel().round(1))",
  ["Computing the category averages by hand on the whole dataset leaks the answers into the features; the encoder's internal cross-fitting exists to avoid exactly that."],
  "“Target encoding replaces a high-cardinality category with a smoothed mean of the target, fitted out-of-fold to avoid leakage.”",
  SK + "sklearn.preprocessing.TargetEncoder.html", taught="ml/feature-scaling-encoding")

e("prep", "simple-imputer", "SimpleImputer",
  "Fills in missing values (NaN) in each column, with the column's training median, mean, or most frequent value.",
  "SimpleImputer(strategy=\"median\").fit_transform(X_train)",
  "import numpy as np\nfrom sklearn.impute import SimpleImputer\n\nX = np.array([[1.0], [np.nan], [3.0], [100.0]])\nprint(SimpleImputer(strategy=\"median\").fit_transform(X).ravel())\nprint(SimpleImputer(strategy=\"mean\").fit_transform(X).ravel())",
  ["The median is the safer default: one extreme value moves the mean a lot."],
  "“SimpleImputer fills missing values with a training-set statistic; the median is robust to outliers.”",
  SK + "sklearn.impute.SimpleImputer.html", taught="ml/feature-scaling-encoding")

e("prep", "polynomial-features", "PolynomialFeatures",
  "Adds powers of each feature as new columns: with degree=3, the single column x becomes the columns 1, x, x², x³. A straight-line model given these columns can draw a curve, because its prediction is now w1·x + w2·x² + w3·x³ + b. A higher degree means a curve that can bend more times.",
  "PolynomialFeatures(degree=3).fit_transform(X)",
  "import numpy as np\nfrom sklearn.preprocessing import PolynomialFeatures\n\nx = np.array([[2.0], [3.0]])                    # one feature, two rows\nprint(PolynomialFeatures(degree=3).fit_transform(x))   # columns: 1, x, x^2, x^3",
  ["The number of columns grows very fast with several features (all products of features are added too).",
   "High degrees give huge numbers (x¹² for x = 10 is a trillion), so scale the feature first."],
  "“PolynomialFeatures expands inputs with powers and interactions so a linear model can fit curves; high degree is the textbook route to overfitting.”",
  SK + "sklearn.preprocessing.PolynomialFeatures.html", taught="ml/linear-regression")

e("combine", "pipeline", "make_pipeline and Pipeline",
  "Glues several steps and a model into one object that behaves like a single model. Calling fit on the pipeline runs fit_transform on each step in turn with the training data, then fits the model on the result. Calling predict runs transform on each step (with what it learned in fit) and then predicts. So you cannot forget a step on new data, and the test data never influences the preprocessing. make_pipeline names the steps for you; Pipeline lets you name them yourself.",
  "model = make_pipeline(step1, step2, final_model)",
  "import numpy as np\nfrom sklearn.pipeline import make_pipeline, Pipeline\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.linear_model import LinearRegression\n\nX = np.array([[1.0], [1.5], [2.0]])\ny = np.array([200.0, 300.0, 380.0])\n\nmodel = make_pipeline(StandardScaler(), LinearRegression())   # scale, then fit a line\nmodel.fit(X, y)                     # scaler learns mean and spread, then the line is fitted\nprint(model.predict([[1.8]]).round(2))   # 1.8 is scaled the same way, then predicted\nprint(list(model.named_steps))     # the names make_pipeline chose\n\n# Pipeline: the same thing, but you choose the step names\nsame = Pipeline([\n    (\"scale\", StandardScaler()),\n    (\"line\", LinearRegression()),\n])\nsame.fit(X, y)\nprint(same.named_steps[\"line\"].coef_.round(2))",
  ["Everything except the last step must be a transformer (have transform); the last can be a model.",
   "To reach a step after fitting, use named_steps with its name, as in the last line."],
  "“A Pipeline chains transformers and a final estimator so that fit and predict apply identical preprocessing; it is the standard guard against train/test leakage, including inside cross-validation.”",
  SK + "sklearn.pipeline.Pipeline.html", taught="ml/feature-scaling-encoding")

e("combine", "column-transformer", "ColumnTransformer",
  "Applies different steps to different columns and puts the results side by side: for example, scale the number columns and one-hot encode the category columns. You give it a list of (name, step, which columns) triples. get_feature_names_out lists the output columns.",
  "ColumnTransformer([(\"num\", StandardScaler(), [\"size\"]), (\"cat\", OneHotEncoder(), [\"city\"])])",
  "import pandas as pd\nfrom sklearn.compose import ColumnTransformer\nfrom sklearn.preprocessing import StandardScaler, OneHotEncoder\n\ndf = pd.DataFrame({\"size\": [1.0, 1.5, 2.0], \"city\": [\"A\", \"B\", \"A\"]})\nprep = ColumnTransformer([\n    (\"num\", StandardScaler(), [\"size\"]),                      # numbers: scale\n    (\"cat\", OneHotEncoder(sparse_output=False), [\"city\"]),   # categories: one-hot\n])\nprint(prep.fit_transform(df).round(2))\nprint(prep.get_feature_names_out())",
  ["Columns you do not list are dropped unless you pass remainder='passthrough'."],
  "“ColumnTransformer routes column subsets to different transformers, the standard way to preprocess mixed numeric and categorical tables inside one pipeline.”",
  SK + "sklearn.compose.ColumnTransformer.html", taught="ml/feature-scaling-encoding")

e("metrics", "mse", "mean_squared_error",
  "The average of the squared differences between the true answers and the predictions. True answers come first.",
  "mean_squared_error(y_true, y_pred)",
  "from sklearn.metrics import mean_squared_error\n\ny_true = [200, 300, 380]\ny_pred = [200, 295, 390]\nprint(mean_squared_error(y_true, y_pred))   # (0 + 25 + 100) / 3",
  ["It is in squared units (squared dollars). Its square root, the RMSE, is back in the original units and easier to say out loud."],
  "“MSE is the mean of squared residuals; RMSE is its square root, in the target's units.”",
  SK + "sklearn.metrics.mean_squared_error.html", taught="ml/what-is-machine-learning")

e("metrics", "mae", "mean_absolute_error",
  "The average size of the misses, ignoring whether each was too high or too low.",
  "mean_absolute_error(y_true, y_pred)",
  "from sklearn.metrics import mean_absolute_error\n\nprint(mean_absolute_error([200, 300, 380], [200, 295, 390]))   # (0 + 5 + 10) / 3",
  ["Unlike MSE it does not punish one big miss extra, so it is less affected by outliers."],
  "“MAE is the mean absolute residual: same units as the target and robust to outliers.”",
  SK + "sklearn.metrics.mean_absolute_error.html", taught="ml/what-is-machine-learning")

e("metrics", "r2", "r2_score",
  "How much of the error of 'always guess the average' the predictions remove: 1 is perfect, 0 is no better than the average, below 0 is worse.",
  "r2_score(y_true, y_pred)",
  "from sklearn.metrics import r2_score\n\ny_true = [200, 300, 380]\nprint(round(r2_score(y_true, [200, 295, 390]), 3))   # close to the truth\naverage = sum(y_true) / len(y_true)\nprint(round(r2_score(y_true, [average] * 3), 3))     # just the average: 0",
  ["Here the 'average' is the average of y_true itself, so R² on a test set compares against the test mean, not the training mean."],
  "“R² is one minus residual sum of squares over total sum of squares: the fraction of variance explained, which can be negative on held-out data.”",
  SK + "sklearn.metrics.r2_score.html", taught="ml/linear-regression")

sk_links = {
  "LinearRegression": "linear-regression", "Ridge": "ridge", "KNeighborsClassifier": "kneighbors",
  "DummyRegressor": "dummy", "DummyClassifier": "dummy",
  "StandardScaler": "standard-scaler", "MinMaxScaler": "minmax-scaler", "OneHotEncoder": "one-hot",
  "TargetEncoder": "target-encoder", "SimpleImputer": "simple-imputer", "PolynomialFeatures": "polynomial-features",
  "make_pipeline": "pipeline", "Pipeline": "pipeline", "ColumnTransformer": "column-transformer",
  "train_test_split": "train-test-split", "KFold": "cross-val", "cross_val_score": "cross-val",
  "mean_squared_error": "mse", "mean_absolute_error": "mae", "r2_score": "r2",
  "load_diabetes": "toy-datasets", "load_iris": "toy-datasets", "load_wine": "toy-datasets",
  "fetch_california_housing": "california",
  ".fit": "fit-predict", ".predict": "fit-predict", ".fit_transform": "transform", ".transform": "transform",
  ".score": "score", ".coef_": "learned-attributes", ".intercept_": "learned-attributes",
  ".named_steps": "pipeline", ".get_feature_names_out": "column-transformer",
}

# ============================================================================ Python tools
pyGroups = [
  {"id": "python", "title": "Python beyond the basics", "intro": "The notes assume plain Python: variables, if, for, functions, lists and dictionaries, and simple f-strings like f\"{x}\". These are the slightly less common pieces that appear in the code, each in a few lines."},
  {"id": "plot", "title": "Plotting with matplotlib", "intro": "matplotlib draws charts. The notes use only a handful of its functions, always through the conventional short name plt. Each example below shows the picture it makes."},
  {"id": "pandas", "title": "Tables with pandas", "intro": "pandas holds a table with named columns, like a spreadsheet in code. The notes use it only where columns have names or mixed types (numbers and categories side by side)."},
]
PYE = []
p = lambda *a, **k: entry(PYE, *a, **k)

p("python", "import-as", "import … as …",
  "Imports a library or a function under a shorter name. The short names np (NumPy), pd (pandas) and plt (matplotlib's plotting part) are universal conventions.",
  "import numpy as np\nfrom module import long_name as short",
  "import numpy as np\nimport matplotlib.pyplot as plt\nfrom statistics import mean as average\nprint(np.__name__, plt.__name__)\nprint(average([1, 2, 3]))",
  ["The notes avoid renaming functions (as mse and so on) in new code, because it makes the code harder to search; you will still see it in other people's code."],
  "“Aliases like np, pd and plt are conventions everyone recognises; renaming arbitrary functions hurts readability.”",
  PY + "reference/simple_stmts.html#import")

p("python", "fstring-format", "f-string formats: {x:.2f}, {x:>6}, {x:.0%}",
  "Inside an f-string, a colon after the value says how to print it. .2f means 2 decimal places. A number before it is the total width, so 8.2f pads to 8 characters, which lines up columns. > aligns right, < left. % multiplies by 100 and adds a percent sign. , adds thousands separators.",
  "f\"{value:width.decimalsf}\"   f\"{text:>width}\"   f\"{fraction:.0%}\"",
  "x = 3.14159\nprint(f\"{x:.2f}\")         # 2 decimals\nprint(f\"[{x:8.2f}]\")      # width 8, 2 decimals (padded on the left)\nprint(f\"[{'mean':>6}]\")   # text, right-aligned in 6\nprint(f\"{0.3331:.0%}\")    # as a percentage\nprint(f\"{1234567:,}\")     # thousands separators\nprint(f\"{x = :.3f}\")      # name and value together",
  ["The format goes after a colon inside the braces, not outside: f\"{x:.2f}\", not f\"{x}:.2f\"."],
  "“Format specs after a colon control precision, width, alignment and percentages in f-strings.”",
  PY + "library/string.html#format-specification-mini-language")

p("python", "slicing-steps", "Slices: a[:5], a[-1], a[::2], a[::-1]",
  "a[start:stop] takes elements from start up to but not including stop; leaving one out means 'from the beginning' or 'to the end'. Negative numbers count from the end, so a[-1] is the last element and a[:-1] is everything but the last. A third number is the step: a[::2] takes every second element, a[1::2] every second starting at the second, a[::-1] reverses.",
  "a[start:stop:step]",
  "a = [0, 10, 20, 30, 40, 50]\nprint(a[:3])      # first three\nprint(a[-1])      # last\nprint(a[:-1])     # all but the last\nprint(a[::2])     # every second: positions 0, 2, 4\nprint(a[1::2])    # every second from position 1\nprint(a[::-1])    # reversed",
  ["The stop position is never included, so a[:3] has three elements.",
   "The same rules work on NumPy arrays, where a slice is a view: changing it changes the original array."],
  "“Slices are half-open, start:stop:step; on NumPy arrays basic slices are views, not copies.”",
  PY + "tutorial/introduction.html#lists")

p("python", "zip-enumerate", "zip and enumerate",
  "zip walks through two (or more) lists side by side, giving one pair at a time. enumerate walks through one list and gives each item together with its position, starting at 0.",
  "for a, b in zip(list_a, list_b): ...\nfor i, item in enumerate(items): ...",
  "sizes = [1.0, 1.5, 2.0]\nprices = [200, 300, 380]\nfor size, price in zip(sizes, prices):\n    print(size, price)\nfor i, price in enumerate(prices):\n    print(i, price)",
  ["zip stops at the shorter list without any warning; pass strict=True to get an error when lengths differ."],
  "“zip pairs iterables element-wise; enumerate adds the index.”",
  PY + "library/functions.html#zip")

p("python", "sorted-key", "sorted(…, key=lambda …), min and max with key",
  "sorted returns a new sorted list. key says what to sort by: a small function applied to each item. lambda x: … writes such a small function in one line without a name. min and max take a key the same way. reverse=True sorts from largest to smallest.",
  "sorted(items, key=lambda item: what_to_sort_by)",
  "words = [\"cat\", \"elephant\", \"ox\"]\nprint(sorted(words))                            # alphabetical\nprint(sorted(words, key=lambda w: len(w)))      # by length\nprint(max(words, key=len))                      # the longest\n\nscores = {\"a\": 0.9, \"b\": 0.2, \"c\": 0.5}\n# the keys, highest score first\nprint(sorted(scores, key=lambda k: scores[k], reverse=True))",
  ["lambda x: len(x) and plain len do the same job as a key; lambda is needed only when the rule is not already a function."],
  "“sorted with a key function sorts by a derived value; lambda defines that function inline.”",
  PY + "howto/sorting.html")

p("python", "comprehensions", "Comprehensions: [f(x) for x in xs]",
  "A one-line way to build a list from another: [x * 2 for x in xs] is a loop that collects x * 2 for every x. An if at the end filters. Curly braces with key: value build a dictionary the same way. Without brackets inside a function call, as in sum(x * x for x in xs), it feeds the values one by one without building a list.",
  "[expression for item in items if condition]",
  "xs = [1, 2, 3, 4]\nprint([x * 2 for x in xs])                 # list\nprint([x for x in xs if x % 2 == 0])       # with a filter\nprint({x: x * x for x in xs})              # dictionary\nprint(sum(x * x for x in xs))              # straight into sum",
  ["If the line gets long or has two for parts, a normal loop is easier to read."],
  "“Comprehensions build lists, dicts or sets declaratively; generator expressions stream values without materialising a list.”",
  PY + "tutorial/datastructures.html#list-comprehensions")

p("python", "tuple-unpacking", "Unpacking: a, b = …",
  "When something gives back several values at once, you can name them all in one line. The underscore _ is the conventional name for a value you do not need.",
  "a, b = pair      first, _ = pair",
  "pair = (180, 23.3)\nw, b = pair\nprint(w, b)\nname, _ = (\"slope\", 180)     # keep the first, ignore the second\nprint(name)\nx, y = 1, 2\nx, y = y, x                   # swap two values in one line\nprint(x, y)",
  ["The number of names must match the number of values exactly, or Python raises a ValueError."],
  "“Tuple unpacking binds multiple return values in one statement; underscore marks values you ignore.”",
  PY + "tutorial/datastructures.html#tuples-and-sequences")

p("python", "assert", "assert",
  "assert condition checks that something is true and stops the program with an AssertionError if it is not. The notes use it as a built-in self-check: 'this result must equal that one'.",
  "assert condition, \"message if it fails\"",
  "import numpy as np\nby_loop = sum(a * b for a, b in zip([1, 2, 3], [4, 5, 6]))\nby_numpy = np.dot([1, 2, 3], [4, 5, 6])\nassert by_loop == by_numpy, \"the two ways should agree\"\nprint(\"checks passed:\", by_loop)",
  ["Compare floating-point results with np.isclose or np.allclose inside the assert, not ==, because tiny rounding differences make == fail."],
  "“assert is a cheap invariant check; for floats compare with a tolerance.”",
  PY + "reference/simple_stmts.html#the-assert-statement")

p("python", "try-except", "try / except",
  "Runs some code and, if it raises a particular error, runs a fallback instead of crashing. The notes use it to show that an operation fails, for example inverting a matrix that has no inverse.",
  "try:\n    risky()\nexcept SomeError as err:\n    handle(err)",
  "import numpy as np\ntry:\n    np.linalg.inv(np.array([[1.0, 2.0], [2.0, 4.0]]))   # second row = 2 x first row\nexcept np.linalg.LinAlgError as err:\n    print(\"cannot invert:\", err)",
  ["Catch the specific error you expect, not every error, or real bugs get hidden."],
  "“try/except handles an expected exception type locally; never use a bare except to silence bugs.”",
  PY + "tutorial/errors.html#handling-exceptions")

p("python", "counter", "collections.Counter",
  "Counts how many times each item appears. most_common(n) gives the n most frequent items with their counts. The notes use it to take a vote among neighbours.",
  "Counter(items).most_common(1)",
  "from collections import Counter\nvotes = [\"cat\", \"dog\", \"cat\", \"cat\", \"dog\"]\ncounts = Counter(votes)\nprint(counts)\nprint(counts.most_common(1))          # [(item, count)] for the winner\nprint(counts.most_common(1)[0][0])    # just the winning item",
  ["most_common returns a list of (item, count) pairs, so the winner itself is [0][0]."],
  "“Counter is a dict subclass for tallies; most_common gives the mode.”",
  PY + "library/collections.html#collections.Counter")

p("python", "perf-counter", "time.perf_counter",
  "Returns the current time in seconds from a precise clock. Call it before and after some code and subtract to see how long the code took.",
  "start = time.perf_counter(); ...; seconds = time.perf_counter() - start",
  "import time\nstart = time.perf_counter()\ntotal = sum(range(1_000_000))\nseconds = time.perf_counter() - start\nprint(total, seconds < 1.0)",
  ["One measurement is noisy; repeat the work a few times and take the best or the average."],
  "“perf_counter is the monotonic high-resolution clock for timing code.”",
  PY + "library/time.html#time.perf_counter")

p("python", "number-literals", "Number spellings: 1e-12, 20_000",
  "Python lets you write numbers in handier ways. 1e-12 is scientific notation: 1 times 10 to the power -12, a tiny number often added to avoid dividing by zero. Underscores inside a number are ignored and only make it easier to read: 20_000 is 20000.",
  "1e-12   2.5e3   1_000_000",
  "print(1e-12)\nprint(2.5e3)\nprint(20_000 + 1)\nprint(1 / (0.0 + 1e-12))     # no division by zero",
  ["1e3 is a float (1000.0), not an int."],
  "“Scientific notation and digit separators are just literals; a small epsilon like 1e-12 guards divisions.”",
  PY + "reference/lexical_analysis.html#numeric-literals")

p("python", "comparisons-in", "Chained comparisons and in",
  "a <= b <= c means a <= b and b <= c, the way you would write it in maths. x in items is True when x is one of the items (in a list, a set, a string or a dictionary's keys).",
  "low <= x <= high      x in items",
  "x = 0.7\nprint(0 <= x <= 1)            # inside the range\nprint(-1 <= -2 <= 1)          # outside\nprint(3 in [1, 2, 3])\nprint(\"cat\" in \"concatenate\")\nprint(\"b\" in {\"a\": 1, \"b\": 2})   # checks the keys",
  ["in on a list checks every element one by one, which is slow for big lists; on a set or dict it is instant."],
  "“Python chains comparisons; membership with in is O(n) on lists and O(1) on sets and dicts.”",
  PY + "reference/expressions.html#comparisons")

p("python", "sets", "Sets: set(a) & set(b)",
  "A set holds each value at most once, with no order. set(items) removes duplicates. & gives the values in both sets, | the values in either, - the values in the first but not the second. The notes use & to check that two lists share nothing.",
  "set(a) & set(b)   set(a) | set(b)   set(a) - set(b)",
  "a = [1, 2, 2, 3]\nb = [3, 4]\nprint(set(a))            # duplicates gone\nprint(set(a) & set(b))   # in both\nprint(set(a) | set(b))   # in either\nprint(len(set(a) & {9})) # 0: nothing shared",
  ["{} is an empty dictionary, not an empty set; write set() for an empty set."],
  "“A set is a hash-based collection of unique items with fast membership and set algebra.”",
  PY + "tutorial/datastructures.html#sets")

p("python", "string-methods", "Strings: .split() and .count()",
  "text.split() cuts a string into a list of words at the spaces. items.count(x) counts how many times x appears in a list (or a string).",
  "words = text.split()     words.count(\"cat\")",
  "text = \"the cat sat on the mat\"\nwords = text.split()\nprint(words)\nprint(words.count(\"the\"))\nprint(len(words))",
  ["split() with no argument also handles several spaces and line breaks; split(\" \") does not."],
  "“str.split tokenises on whitespace; list.count is a linear scan.”",
  PY + "library/stdtypes.html#str.split")

p("python", "dict-get", "dict.get(key, default)",
  "Looks up a key in a dictionary but, instead of failing when the key is missing, gives back the default you chose. Handy for running totals: totals.get(c, 0.0) + x.",
  "d.get(key, default)",
  "totals = {}\nfor city, price in [(\"A\", 100), (\"B\", 300), (\"A\", 120)]:\n    totals[city] = totals.get(city, 0) + price\nprint(totals)\nprint(totals.get(\"Z\", 0))     # missing key: the default",
  ["d[key] raises KeyError for a missing key; d.get(key) returns None."],
  "“dict.get supplies a default for missing keys; collections.Counter or defaultdict do the same for tallies.”",
  PY + "library/stdtypes.html#dict.get")

p("python", "copy", ".copy()",
  "Makes an independent copy of a list or array. Without it, b = a gives a second name for the same object, so changing b also changes a. NumPy slices are also shared views of the original, so copy before changing them if the original must stay as it was.",
  "b = a.copy()",
  "import numpy as np\na = np.array([1, 2, 3])\nsame = a           # another name for the same array\nfresh = a.copy()   # a separate array\nsame[0] = 100\nprint(a)           # changed through 'same'\nfresh[1] = 200\nprint(a)           # unchanged by 'fresh'",
  ["This is the source of many silent bugs when scaling a column 'in a copy' that was not one."],
  "“Assignment binds a name, it does not copy; NumPy slices are views; use .copy() when you mutate.”",
  "https://numpy.org/doc/stable/reference/generated/numpy.ndarray.copy.html")

p("python", "classes", "class, self and methods",
  "A class bundles data with the functions that use it. def inside a class defines a method; its first parameter, self, is the object itself, so self.mean = … stores a number on the object and later methods can read it back. This is exactly how scikit-learn's scalers work: fit stores numbers on self, transform reads them.",
  "class Name:\n    def method(self, x): ...",
  "import numpy as np\n\nclass MeanCentre:\n    def fit(self, x):\n        self.mean = x.mean()      # remember a number on the object\n        return self\n    def transform(self, x):\n        return x - self.mean      # use the remembered number\n\nstep = MeanCentre().fit(np.array([1.0, 2.0, 3.0]))\nprint(step.mean)\nprint(step.transform(np.array([10.0])))",
  ["Forgetting self as the first parameter gives 'takes 1 positional argument but 2 were given'.",
   "return self at the end of fit is what lets you write MeanCentre().fit(x) in one line, as scikit-learn does."],
  "“A scikit-learn transformer is just a class whose fit stores learned state on self and whose transform reads it.”",
  PY + "tutorial/classes.html")

p("python", "functions-as-values", "Functions as values",
  "In Python a function is a value like any other: you can put it in a list or pass it to another function, then call it later with (). The notes use this to run several fitting methods in one loop.",
  "for name, fn in [(\"a\", f), (\"b\", g)]: fn(x)",
  "def double(x):\n    return 2 * x\n\ndef square(x):\n    return x * x\n\nfor name, fn in [(\"double\", double), (\"square\", square)]:\n    print(name, fn(5))",
  ["Write the name without () to pass the function; with () you pass its result instead."],
  "“Functions are first-class objects, so you can store them in data structures and pass them as arguments.”",
  PY + "tutorial/controlflow.html#defining-functions")

p("plot", "plt-plot", "plt.plot, labels, legend, plt.show",
  "plt.plot(xs, ys) draws a line through the points (xs[0], ys[0]), (xs[1], ys[1]), and so on. Pass label=… and call plt.legend() to name each line. plt.xlabel, plt.ylabel and plt.title write the axis names and the title. plt.show() opens the window (in a notebook the chart appears anyway).",
  "plt.plot(xs, ys, label=\"name\")\nplt.xlabel(\"x\"); plt.ylabel(\"y\"); plt.legend(); plt.show()",
  "import numpy as np\nimport matplotlib.pyplot as plt\n\nx = np.linspace(0, 3, 50)\nplt.plot(x, np.exp(x), label=\"exp(x)\")\nplt.plot(x, x ** 2, label=\"x squared\")\nplt.xlabel(\"x\")\nplt.ylabel(\"value\")\nplt.title(\"Two curves\")\nplt.legend()\nplt.show()",
  ["A smooth curve needs many x values; np.linspace(0, 3, 50) gives 50 of them."],
  "“plt.plot draws line series; label plus legend names them.”",
  MPL + "matplotlib.pyplot.plot.html", image=True)

p("plot", "plt-scatter", "plt.scatter",
  "Draws one dot per point, without joining them. Used for data, where joining the dots would suggest an order that is not there.",
  "plt.scatter(xs, ys)",
  "import matplotlib.pyplot as plt\n\nsizes = [1.0, 1.5, 2.0]\nprices = [200, 300, 380]\nplt.scatter(sizes, prices)\nplt.plot([1.0, 2.0], [203.3, 383.3], label=\"best line\")\nplt.xlabel(\"size (thousand sq ft)\")\nplt.ylabel(\"price\")\nplt.legend()\nplt.show()",
  [],
  "“Scatter for data points, plot for functions and fitted lines.”",
  MPL + "matplotlib.pyplot.scatter.html", image=True)

p("plot", "plt-lines", "plt.axhline and plt.axvline",
  "Draw a straight horizontal line across the whole chart at a given y (axhline), or a vertical one at a given x (axvline). Handy for marking zero, a threshold or a chosen value.",
  "plt.axhline(y)   plt.axvline(x)",
  "import numpy as np\nimport matplotlib.pyplot as plt\n\nx = np.linspace(-2, 2, 50)\nplt.plot(x, x ** 2 - 1)\nplt.axhline(0, color=\"gray\")                    # the x-axis\nplt.axvline(1, linestyle=\"--\", color=\"red\")     # mark x = 1\nplt.show()",
  [],
  "“axhline / axvline draw reference lines spanning the axes.”",
  MPL + "matplotlib.pyplot.axhline.html", image=True)

p("plot", "plt-subplots", "plt.subplots",
  "Makes a figure with a grid of separate charts. fig, axes = plt.subplots(1, 2) gives one row of two charts; you then draw on each one through axes[0] and axes[1], whose methods have the same names as plt's (plot, scatter) except that labels use set_xlabel and set_title.",
  "fig, axes = plt.subplots(rows, cols, figsize=(width, height))",
  "import numpy as np\nimport matplotlib.pyplot as plt\n\nx = np.linspace(0.1, 5, 50)\nfig, axes = plt.subplots(1, 2, figsize=(8, 3))\naxes[0].plot(x, np.exp(x))\naxes[0].set_title(\"exp\")\naxes[1].plot(x, np.log(x))\naxes[1].set_title(\"log\")\nplt.show()",
  ["On an axes object it is set_xlabel and set_title, not xlabel and title."],
  "“subplots returns a figure and an array of axes; draw on each axes object.”",
  MPL + "matplotlib.pyplot.subplots.html", image=True)

p("pandas", "dataframe", "pd.DataFrame and df[\"column\"]",
  "A DataFrame is a table: named columns, one row per example, and each column can have its own type (numbers in one, words in another). Build one from a dictionary of column name to values. df[\"name\"] gives one column; df[[\"a\", \"b\"]] gives a smaller table.",
  "df = pd.DataFrame({\"col\": values, ...})",
  "import pandas as pd\n\ndf = pd.DataFrame({\n    \"size\": [1.0, 1.5, 2.0],\n    \"city\": [\"A\", \"B\", \"A\"],\n    \"price\": [200, 300, 380],\n})\nprint(df)\nprint(df[\"price\"].mean())\nprint(df.shape)",
  ["Most scikit-learn steps accept a DataFrame and use its column names; NumPy arrays have no names, only positions."],
  "“A DataFrame is a labelled, column-typed table; scikit-learn accepts it directly and ColumnTransformer can select columns by name.”",
  PD + "pandas.DataFrame.html")

p("pandas", "series", "pd.Series",
  "One column on its own: a list of values with a name and an index (the row labels). Taking one column out of a DataFrame gives a Series.",
  "pd.Series(values, name=\"col\")",
  "import pandas as pd\n\ncity = pd.Series([\"A\", \"B\", \"A\", \"C\"], name=\"city\")\nprint(city.value_counts())\nprint(city.nunique())",
  [],
  "“A Series is a single labelled column; value_counts tallies categories.”",
  PD + "pandas.Series.html")

p("pandas", "loc", ".loc[rows, columns]",
  "Picks rows and columns by their labels. df.loc[0, \"price\"] is one cell; df.loc[df[\"city\"] == \"A\", \"price\"] is the prices of the rows whose city is A.",
  "df.loc[row_selection, column_selection]",
  "import pandas as pd\n\ndf = pd.DataFrame({\"city\": [\"A\", \"B\", \"A\"], \"price\": [200, 300, 380]})\nprint(df.loc[0, \"price\"])\nprint(df.loc[df[\"city\"] == \"A\", \"price\"].tolist())",
  ["loc uses labels and includes the end of a slice; iloc uses positions and excludes it, like Python."],
  "“loc selects by label (and boolean masks), iloc by integer position.”",
  PD + "pandas.DataFrame.loc.html")

py_links = {
  "zip": "zip-enumerate", "enumerate": "zip-enumerate", "sorted": "sorted-key", "lambda": "sorted-key",
  "assert": "assert", "Counter": "counter", ".copy": "copy", ".split": "string-methods", ".count": "string-methods",
  ".get": "dict-get", "time.perf_counter": "perf-counter",
  "plt.plot": "plt-plot", "plt.xlabel": "plt-plot", "plt.ylabel": "plt-plot", "plt.title": "plt-plot",
  "plt.legend": "plt-plot", "plt.show": "plt-plot", "plt.scatter": "plt-scatter",
  "plt.axhline": "plt-lines", "plt.axvline": "plt-lines", "plt.subplots": "plt-subplots",
  "pd.DataFrame": "dataframe", "pd.Series": "series", ".loc": "loc",
}


# ============================================================================ run and write

WIDTH = 74  # characters that fit in a code block on a laptop screen


def tidy(code):
    """Move a trailing comment onto its own line above when the line is too wide for the code box."""
    out = []
    for line in code.split("\n"):
        if len(line) > WIDTH and "  # " in line and not line.lstrip().startswith("#"):
            stmt, comment = line.split("  # ", 1)
            indent = line[: len(line) - len(line.lstrip())]
            out.append(indent + "# " + comment.strip())
            out.append(stmt.rstrip())
        else:
            out.append(line)
    return "\n".join(out)
def run(entries, image_dir):
    out = []
    for ent in entries:
        buf = io.StringIO()
        plt.close("all")
        plt.rcParams.update({"figure.figsize": (6, 3.4), "figure.dpi": 110, "font.size": 10,
                             "figure.facecolor": "#faf5e6", "axes.facecolor": "#faf5e6"})
        code = tidy(ent["code"])
        with warnings.catch_warnings(), contextlib.redirect_stdout(buf):
            warnings.simplefilter("ignore")
            try:
                show = plt.show
                plt.show = lambda *a, **k: None
                exec(compile(code, ent["id"], "exec"), {"__name__": "__main__"})
            except Exception:
                print("ERROR\n" + traceback.format_exc(limit=1))
            finally:
                plt.show = show
        ent = dict(ent)
        ent["code"] = code
        if ent["image"]:
            os.makedirs(image_dir, exist_ok=True)
            plt.tight_layout()
            plt.savefig(os.path.join(image_dir, ent["id"] + ".png"))
            ent["image"] = "/ai/ref/" + ent["id"] + ".png"
        else:
            ent["image"] = ""
        ent["output"] = buf.getvalue().rstrip("\n")
        if "ERROR" in ent["output"]:
            print("!!", ent["id"], ent["output"], file=sys.stderr)
            sys.exit(1)
        out.append(ent)
    return out


def write(path, prefix, groups, entries, links, version_note):
    ids = {x["id"] for x in entries}
    for k, v in links.items():
        assert v in ids, (k, v)
    Cap = prefix[0].upper() + prefix[1:]
    ts = [f"// Generated by scripts/gen_reference.py. Every `output` below is real output ({version_note}).",
          "// Do not edit by hand: change the generator and rerun it.",
          "",
          "import type { RefGroup, RefEntry } from './reference';",
          "",
          f"export const {prefix}Groups: RefGroup[] = " + json.dumps(groups, ensure_ascii=False, indent=2) + ";",
          "",
          f"export const {prefix}Entries: RefEntry[] = " + json.dumps(entries, ensure_ascii=False, indent=2) + ";",
          "",
          "/** Which spelling in code links to which entry. */",
          f"export const {prefix}Links: Record<string, string> = {{"]
    for k in sorted(links, key=len, reverse=True):
        ts.append("  " + json.dumps(k) + ": " + json.dumps(links[k]) + ",")
    ts += ["};", ""]
    open(path, "w").write("\n".join(ts))
    print(path, len(entries), "entries")


img = os.path.join(ROOT, "public", "ai", "ref")
versions = f"scikit-learn {sklearn.__version__}, NumPy {np.__version__}, pandas {pd.__version__}, matplotlib {matplotlib.__version__}"
write(os.path.join(ROOT, "src/data/sklearn.ts"), "sklearn", skGroups, run(SKE, img), sk_links, versions)
write(os.path.join(ROOT, "src/data/pytools.ts"), "py", pyGroups, run(PYE, img), py_links, versions)
