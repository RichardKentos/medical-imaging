import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, accuracy_score

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
# TODO: Add the models you want to evaluate to the list
models_for_test_eval = models

for m_name, clf in models_for_test_eval:
    print(f"Model: {m_name}")
    print("-"*50)
    for me_name, metricf in metrics:
        y_pred = clf.predict(X_dev)
        s = metricf(y_dev, y_pred)
        print(f"{me_name}: {s}")
    print()
