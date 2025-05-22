# 06 - Introduction to Machine Learning with Python (Python 机器学习入门)

## What is Machine Learning (ML)? (什么是机器学习?)
Machine Learning is a field of Artificial Intelligence where algorithms allow computers to learn from data without being explicitly programmed for every single case.
机器学习是人工智能的一个领域，其算法允许计算机从数据中学习，而无需为每一种情况都进行显式编程。
Instead of writing exact rules to make a decision, you feed data to an ML algorithm, and it learns the patterns or rules from that data.
你不是编写精确的规则来做决策，而是将数据提供给机器学习算法，算法会从数据中学习模式或规则。

**Traditional Programming vs. Machine Learning (传统编程与机器学习对比):**
*   **Traditional Programming (传统编程):** You write explicit rules (code) that tell the computer what to do with input data to produce an output.
    **传统编程 (Traditional Programming):** 你编写明确的规则 (代码)，告诉计算机如何处理输入数据以产生输出。
    (Input Data + Your Program/Rules -> Output)
    (输入数据 + 你的程序/规则 -> 输出)
*   **Machine Learning (机器学习):** You provide input data and corresponding expected outputs (for supervised learning), and the ML algorithm creates the program/rules.
    **机器学习 (Machine Learning):** 你提供输入数据和相应的期望输出 (对于监督学习)，机器学习算法会创建程序/规则。
    (Input Data + Expected Output -> ML Algorithm -> Program/Model)
    (输入数据 + 期望输出 -> 机器学习算法 -> 程序/模型)

## Common ML Concepts (常见机器学习概念)

### Types of ML (机器学习的类型)
*   **Supervised Learning (监督学习):**
    The algorithm learns from labeled data, meaning each data point is tagged with a correct output or label.
    算法从标记数据中学习，这意味着每个数据点都标有正确的输出或标签。
    The goal is to learn a mapping function that can predict the output for new, unseen input.
    目标是学习一个映射函数，该函数可以预测新的、未见过输入的输出。
    *   **Classification (分类):** The output variable is a category (e.g., "spam" or "not spam", "material A" or "material B").
        **分类 (Classification):** 输出变量是一个类别 (例如，“垃圾邮件”或“非垃圾邮件”，“材料A”或“材料B”)。
    *   **Regression (回归):** The output variable is a continuous value (e.g., predicting temperature, material strength, price).
        **回归 (Regression):** 输出变量是一个连续值 (例如，预测温度、材料强度、价格)。
*   **Unsupervised Learning (无监督学习):**
    The algorithm learns from unlabeled data, trying to find patterns, structures, or relationships within the data itself.
    算法从未标记的数据中学习，试图在数据本身中找到模式、结构或关系。
    *   **Clustering (聚类):** Grouping similar data points together (e.g., grouping customers with similar purchasing behavior).
        **聚类 (Clustering):** 将相似的数据点分组在一起 (例如，将具有相似购买行为的客户分组)。
    *   **Dimensionality Reduction (降维):** Reducing the number of variables (features) while preserving important information, often used for visualization or to simplify data.
        **降维 (Dimensionality Reduction):** 在保留重要信息的同时减少变量 (特征) 的数量，通常用于可视化或简化数据。
*   **Reinforcement Learning (强化学习) (Briefly - 简要提及):**
    The algorithm learns by interacting with an environment, receiving rewards or penalties for its actions. (Think of training a robot to navigate a maze).
    算法通过与环境交互来学习，根据其行为获得奖励或惩罚。(可以想象成训练机器人在迷宫中导航)。

### Dataset (数据集)
A collection of data that you use to train and test your ML model.
用于训练和测试机器学习模型的数据集合。
*   **Features (特征):** These are the input variables or attributes used to make predictions (e.g., if predicting material strength, features could be composition, processing temperature, etc.). Often denoted as `X`.
    **特征 (Features):** 用于进行预测的输入变量或属性 (例如，如果预测材料强度，特征可以是成分、处理温度等)。通常表示为 `X`。
*   **Target Variable (目标变量) / Labels (标签):** This is the output variable you are trying to predict (e.g., material strength itself, or the class label "spam"). Often denoted as `y`.
    **目标变量 (Target Variable) / 标签 (Labels):** 你试图预测的输出变量 (例如，材料强度本身，或类别标签“垃圾邮件”)。通常表示为 `y`。

### Training and Testing (训练与测试)
To evaluate how well your model will perform on new, unseen data, you split your dataset:
为了评估你的模型在新的、未见过的数据上的表现如何，你需要划分数据集：
*   **Training Set (训练集):** A subset of the dataset used to train the ML model. The model learns patterns from this data.
    **训练集 (Training Set):** 数据集的一个子集，用于训练机器学习模型。模型从此数据中学习模式。
*   **Test Set (测试集):** A subset of the dataset that the model has not seen during training. It's used to evaluate the model's performance and generalization ability.
    **测试集 (Test Set):** 模型在训练期间未见过的数据集子集。它用于评估模型的性能和泛化能力。
*   **Splitting Data (划分数据):** Typically, you might split data 70-80% for training and 20-30% for testing.
    **划分数据 (Splitting Data):** 通常，你可能会将数据的 70-80% 用于训练，20-30% 用于测试。

### Model (模型)
In ML, a model is the specific mathematical representation learned from the training data.
在机器学习中，模型是从训练数据中学习到的特定数学表示。
It's the output of the training process and is what you use to make predictions on new data.
它是训练过程的输出，也是你用来对新数据进行预测的东西。

### Overfitting and Underfitting (过拟合与欠拟合)
*   **Overfitting (过拟合):** The model learns the training data too well, including its noise and specific details. As a result, it performs poorly on new, unseen data (test set) because it doesn't generalize well.
    **过拟合 (Overfitting):** 模型对训练数据学习得“太好”，包括其噪声和特定细节。结果，它在新的、未见过的数据 (测试集) 上表现不佳，因为它泛化能力差。
*   **Underfitting (欠拟合):** The model is too simple and fails to capture the underlying patterns in the training data. It performs poorly on both the training and test sets.
    **欠拟合 (Underfitting):** 模型过于简单，未能捕捉到训练数据中的基本模式。它在训练集和测试集上都表现不佳。

## Introduction to Scikit-learn (Scikit-learn 简介)
Scikit-learn is one of the most popular Python libraries for machine learning.
Scikit-learn 是最流行的 Python 机器学习库之一。
*   **Key Features (主要特点):** It provides simple and efficient tools for data mining and data analysis. It's built on NumPy, SciPy, and Matplotlib. It is accessible to everybody and reusable in various contexts.
    **主要特点 (Key Features):** 它为数据挖掘和数据分析提供了简单高效的工具。它构建于 NumPy、SciPy 和 Matplotlib 之上。它易于上手，并可在多种场景下复用。
*   **Wide Range of Algorithms (广泛的算法):** Includes tools for classification, regression, clustering, dimensionality reduction, model selection, and preprocessing.
    **广泛的算法 (Wide Range of Algorithms):** 包括用于分类、回归、聚类、降维、模型选择和预处理的工具。
*   **Website (官方网站):** [`https://scikit-learn.org/`](https://scikit-learn.org/)

## A Simple ML Workflow Example (一个简单的机器学习工作流程示例)
Let's outline a typical workflow using Scikit-learn. We'll use a simple classification example.
让我们概述一个使用 Scikit-learn 的典型工作流程。我们将使用一个简单的分类示例。

**Goal (目标):** Predict the species of an Iris flower based on its sepal and petal measurements.
**目标 (Goal):** 根据鸢尾花的花萼和花瓣测量值来预测其种类。

### 1. Load Data (加载数据)
We'll use the built-in Iris dataset from Scikit-learn for simplicity.
为简单起见，我们将使用 Scikit-learn 内置的鸢尾花 (Iris) 数据集。
This dataset contains measurements for 150 Iris flowers, each belonging to one of three species.
该数据集包含150朵鸢尾花的测量数据，每朵花属于三个种类之一。

```python
from sklearn.datasets import load_iris

# Load the dataset (加载数据集)
iris = load_iris()
X = iris.data  # Features (特征 - sepal length, sepal width, petal length, petal width)
y = iris.target # Target variable (目标变量 - species of iris: 0, 1, or 2)

print("Features (X) shape:", X.shape) # (150, 4) -> 150 samples, 4 features (150个样本, 4个特征)
print("Target (y) shape:", y.shape)   # (150,) -> 150 labels (150个标签)
print("Feature names:", iris.feature_names) # ['sepal length (cm)', ...] (特征名称)
print("Target names:", iris.target_names)   # ['setosa', 'versicolor', 'virginica'] (目标类别名称)
```

### 2. Data Exploration and Preprocessing (数据探索与预处理) (Simplified - 简化版)
In a real project, you'd do more exploration. Here, we'll just split the data.
在真实项目中，你会进行更多的数据探索。在这里，我们仅划分数据。
*   **Splitting data into features (X) and target (y) (将数据划分为特征 (X) 和目标 (y)):** This is already done when loading the Iris dataset (X and y are separate).
    **将数据划分为特征 (X) 和目标 (y) (Splitting data into features (X) and target (y)):** 加载 Iris 数据集时已经完成 (X 和 y 是分开的)。
*   **Splitting data into training and testing sets (将数据划分为训练集和测试集):**
    This helps us evaluate the model on data it hasn't seen before.
    这有助于我们在模型未见过的数据上评估模型。
    ```python
    from sklearn.model_selection import train_test_split

    # X_train, X_test: features for training and testing (训练和测试的特征)
    # y_train, y_test: target labels for training and testing (训练和测试的目标标签)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.3,  # 30% of data for testing (30% 的数据用于测试)
        random_state=42 # Ensures the split is the same every time (for reproducibility)
                        # 确保每次划分都相同 (为了可复现性)
    )

    print("X_train shape:", X_train.shape) # (105, 4) (输出)
    print("X_test shape:", X_test.shape)   # (45, 4) (输出)
    ```

### 3. Choose a Model and Train It (选择模型并训练)
We'll use K-Nearest Neighbors (KNN) classifier, a simple yet effective algorithm.
我们将使用 K-最近邻 (KNN) 分类器，这是一种简单但有效的算法。
KNN classifies a new data point based on the majority class of its 'k' nearest neighbors in the feature space.
KNN 根据特征空间中新数据点 'k' 个最近邻居的多数类别对其进行分类。

```python
from sklearn.neighbors import KNeighborsClassifier

# Create an instance of the model (创建模型实例)
# n_neighbors=3 means it will look at the 3 nearest neighbors.
# n_neighbors=3 表示它将查看3个最近的邻居。
knn_model = KNeighborsClassifier(n_neighbors=3)

# Train the model using the training data (使用训练数据训练模型)
knn_model.fit(X_train, y_train)
print("KNN Model trained successfully. (KNN 模型训练成功。)")
```

### 4. Make Predictions (进行预测)
Use the trained model to make predictions on the test set.
使用训练好的模型对测试集进行预测。

```python
y_pred = knn_model.predict(X_test)

# Display some predictions vs actual values (显示一些预测值与实际值)
# (For a few test samples - 对于一些测试样本)
print("\nSample Predictions (部分样本预测):")
for i in range(min(5, len(X_test))): # Print first 5 or fewer (打印前5个或更少)
    predicted_species = iris.target_names[y_pred[i]]
    actual_species = iris.target_names[y_test[i]]
    print(f"  Predicted (预测): {predicted_species}, Actual (实际): {actual_species}")
```

### 5. Evaluate the Model (评估模型)
Accuracy is a common metric for classification: (Number of correct predictions) / (Total number of predictions).
准确率是分类任务的常用指标：(正确预测的数量) / (总预测数量)。

```python
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy (模型准确率): {accuracy:.2f}") # e.g., 0.98 (例如：0.98)
# Accuracy is usually between 0 and 1. Higher is better.
# 准确率通常在0到1之间。越高越好。
```

## Code Example File (代码示例文件)
A full, runnable Python script demonstrating this simple K-Nearest Neighbors classification workflow on the Iris dataset will be available in the `examples/` directory:
一个完整的、可运行的 Python 脚本，演示在 Iris 数据集上使用 K-最近邻分类的简单工作流程，将位于 `examples/` 目录中：
*   `examples/01_simple_classification_iris.py`

We encourage you to try running this script and understanding how these different steps connect to build a basic machine learning model.
我们鼓励你尝试运行此脚本，并理解这些不同步骤是如何连接起来构建一个基本的机器学习模型的。

This is a very basic introduction. Machine learning is a vast and exciting field with many more algorithms and techniques to explore!
这是一个非常基础的入门介绍。机器学习是一个广阔且激动人心的领域，有更多的算法和技术等待探索！
