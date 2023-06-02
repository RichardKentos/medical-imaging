import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, accuracy_score


"""
This script performs various operations on the 'featuresFile.csv' dataset, including data preprocessing, model training, and evaluation.

The script follows the following steps:

1. Reading and Preprocessing Data:
   - Read the CSV file 'featuresFile.csv' into a pandas DataFrame.
   - Drop the 'image_id' and 'diagnosis' columns from the DataFrame.

2. Data Visualization:
   - Plot a count plot of the 'healthy' column in the DataFrame.
   - Plot a pair plot of the DataFrame with the hue set to 'healthy'.

3. Train-Dev-Test Split:
   - Split the data into features (X) and target variable (y).
   - Split the data into train and test sets with a test size of 0.3 and a random state of 42.
   - Further split the training set into train and dev sets with a test size of 0.25 and a random state of 42.

4. Model Training:
   - Initialize Logistic Regression and K-Nearest Neighbors classifiers.
   - Train the models on the training set.

5. Model Evaluation:
   - Evaluate the models on the training set and print F1 score and accuracy.
   - Evaluate the models on the dev set and print F1 score and accuracy.
   - Evaluate the models on the test set and print F1 score and accuracy.

Note: The evaluation metrics used are F1 score and accuracy. The models used are Logistic Regression (lr) and K-Nearest Neighbors (knn).
"""


df = pd.read_csv("featuresFile.csv")

df = df.drop(["image_id", "diagnosis"], axis=1)
sns.countplot(data=df, x="healthy")

sns.pairplot(data=df, hue="healthy")
plt.show()

# ------------------------------------------- Train, dev, test split
# Get the features labels into separate vars
X, y = df.iloc[:, :-1], df.iloc[:, -1]

# Train, dev (hyper-parameter tuning), test (use to evaluate your final model and include the stats to report) split
# -- Train, test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)

# -- Split the training dataset into train and dev
X_train, X_dev, y_train, y_dev = train_test_split(
    X_train, y_train, test_size=0.25, random_state=42)


# ------------------------------------------- Train the models
# Hyper-parameters
lr = LogisticRegression(random_state=42)
knn = KNeighborsClassifier(n_neighbors=3)
models = [("lr", lr), ("knn", knn)]

# Training
for _, clf in models:
    clf.fit(X_train, y_train)

# ------------------------------------------- Evaluate on training
metrics = [("f1", f1_score), ("acc", accuracy_score)]

for m_name, clf in models:
    print(f"Model: {m_name}")
    print("-"*50)
    for me_name, metricf in metrics:
        y_pred = clf.predict(X_train)
        s = metricf(y_train, y_pred)
        print(f"{me_name}: {s}")
    print()

# ------------------------------------------- Evaluate on dev dataset
metrics = [("f1", f1_score), ("acc", accuracy_score)]

for m_name, clf in models:
    print(f"Model: {m_name}")
    print("-"*50)
    for me_name, metricf in metrics:
        y_pred = clf.predict(X_dev)
        s = metricf(y_dev, y_pred)
        print(f"{me_name}: {s}")
    print()


# ------------------------------------------- Evaluate on test
metrics = [("f1", f1_score), ("acc", accuracy_score)]
models_for_test_eval = models

for m_name, clf in models_for_test_eval:
    print(f"Model: {m_name}")
    print("-"*50)
    for me_name, metricf in metrics:
        y_pred = clf.predict(X_dev)
        s = metricf(y_dev, y_pred)
        print(f"{me_name}: {s}")
    print()
