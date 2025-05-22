# This script demonstrates a simple machine learning workflow using the Iris dataset
# and K-Nearest Neighbors (KNN) for classification with Scikit-learn.
# 本脚本使用 Iris 数据集和 K-最近邻 (KNN) 算法通过 Scikit-learn 演示一个简单的机器学习分类工作流程。

# --- 1. Imports (导入所需库) ---
print("--- 1. Importing Libraries (导入库) ---")
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import pandas as pd # For briefly showing data structure (用于简要展示数据结构)
print("Libraries imported successfully.\n (库导入成功。)\n")

# --- 2. Load Data (加载数据) ---
print("--- 2. Loading Data (加载数据) ---")
# Load the Iris dataset - 加载 Iris 数据集
iris = load_iris()
X = iris.data  # Features (特征)
y = iris.target # Target variable (labels) (目标变量 (标签))

print(f"Features (X) shape: {X.shape}") # Output: (150, 4) - 150 samples, 4 features (150个样本, 4个特征) (输出)
print(f"Target (y) shape: {y.shape}")   # Output: (150,) - 150 labels (150个标签) (输出)
print(f"Feature names (特征名称): {iris.feature_names}")
# Output: ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'] (输出)
print(f"Target names (目标类别名称): {iris.target_names}")
# Output: ['setosa', 'versicolor', 'virginica'] (输出)

# (Optional) Briefly convert to Pandas DataFrame to show data structure
# (可选) 短暂转换为 Pandas DataFrame 以显示数据结构
print("\n(Optional) Displaying first 5 rows of data using Pandas DataFrame:")
# (可选) 使用 Pandas DataFrame 显示数据的前5行：
df_features = pd.DataFrame(X, columns=iris.feature_names)
df_target = pd.DataFrame(y, columns=['species'])
df_combined = pd.concat([df_features, df_target], axis=1)
# Map target numbers to species names for display (将目标数字映射到物种名称以便显示)
df_combined['species'] = df_combined['species'].apply(lambda index: iris.target_names[index])

print("First 5 rows of combined DataFrame (DataFrame 前5行):\n", df_combined.head())
# print("\nDataFrame Info (DataFrame 信息):")
# df_combined.info() # This provides a summary of the DataFrame (这提供了 DataFrame 的摘要)
print("\n")

# --- 3. Split Data (划分数据) ---
print("--- 3. Splitting Data into Training and Testing Sets (将数据划分为训练集和测试集) ---")
# X_train, X_test: features for training and testing (训练和测试的特征)
# y_train, y_test: target labels for training and testing (训练和测试的目标标签)
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,  # Use 30% of data for testing (使用30%的数据进行测试)
    random_state=42 # Ensures the split is the same every time (for reproducibility)
                    # 确保每次划分都相同 (为了可复现性)
)
print(f"X_train shape (训练集特征形态): {X_train.shape}") # Output: (105, 4) (输出)
print(f"X_test shape (测试集特征形态): {X_test.shape}")   # Output: (45, 4) (输出)
print(f"y_train shape (训练集目标形态): {y_train.shape}") # Output: (105,) (输出)
print(f"y_test shape (测试集目标形态): {y_test.shape}")   # Output: (45,) (输出)
print("Data split successfully.\n (数据划分成功。)\n")

# --- 4. Initialize and Train Model (初始化并训练模型) ---
print("--- 4. Initializing and Training K-Nearest Neighbors (KNN) Model (初始化并训练K-最近邻模型) ---")
# Create an instance of the KNeighborsClassifier model
# 创建 KNeighborsClassifier 模型实例
# n_neighbors=3 means it will look at the 3 nearest neighbors.
# n_neighbors=3 表示它将查看3个最近的邻居。
knn_model = KNeighborsClassifier(n_neighbors=3)

# Train the model using the training data - 使用训练数据训练模型
knn_model.fit(X_train, y_train)
print("KNN Model trained successfully.\n (KNN 模型训练成功。)\n")

# --- 5. Make Predictions (进行预测) ---
print("--- 5. Making Predictions on the Test Set (在测试集上进行预测) ---")
# Use the trained model to make predictions on the test set
# 使用训练好的模型对测试集进行预测
y_pred = knn_model.predict(X_test)

print("First 5 predictions (前5个预测值):", y_pred[:5])
# Map these numbers to actual species names for clarity (为清晰起见，将这些数字映射到实际物种名称)
predicted_species_names = [iris.target_names[p] for p in y_pred[:5]]
actual_species_names = [iris.target_names[a] for a in y_test[:5]]
print(f"Predicted species for first 5 test samples (前5个测试样本的预测物种): {predicted_species_names}")
print(f"Actual species for first 5 test samples (前5个测试样本的实际物种): {actual_species_names}")
print("Predictions made.\n (预测完成。)\n")

# --- 6. Evaluate Model (评估模型) ---
print("--- 6. Evaluating the Model (评估模型) ---")
# Calculate the accuracy of the model
# 计算模型的准确率
# Accuracy = (Number of correct predictions) / (Total number of predictions)
# 准确率 = (正确预测的数量) / (总预测数量)
accuracy = accuracy_score(y_test, y_pred)

print(f"Model Accuracy (模型准确率): {accuracy:.4f}") # Format to 4 decimal places (格式化为4位小数)
# Example Output: Model Accuracy (模型准确率): 1.0000 (This means 100% accuracy on this specific split and model)
# 示例输出: 模型准确率: 1.0000 (这意味着在此特定划分和模型上达到100%的准确率)
print("\nScript finished.")
# 脚本结束。
