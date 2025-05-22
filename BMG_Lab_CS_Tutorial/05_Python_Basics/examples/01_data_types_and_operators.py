# This script demonstrates basic Python data types and operators.
# 本脚本演示 Python 的基本数据类型和运算符。

# --- Data Types (数据类型) ---
print("--- Data Types (数据类型) ---")

# Integer (整数)
age = 30
print(f"Age (年龄): {age}, Type (类型): {type(age)}")  # Output: Age (年龄): 30, Type (类型): <class 'int'> (输出)

# Float (浮点数)
pi_approx = 3.14159
print(f"Pi Approximation (Pi 近似值): {pi_approx}, Type (类型): {type(pi_approx)}")  # Output: Pi Approximation (Pi 近似值): 3.14159, Type (类型): <class 'float'> (输出)

# String (字符串)
lab_name = "BMG Lab"
message = 'Python is versatile!'
# Using f-string for formatted output - 使用 f-string 进行格式化输出
full_message = f"Welcome to {lab_name}. {message}"
print(f"Message (消息): {full_message}, Type (类型): {type(lab_name)}")  # Output: Message (消息): Welcome to BMG Lab. Python is versatile!, Type (类型): <class 'str'> (输出)

# Boolean (布尔型)
is_learning = True
print(f"Is learning (正在学习): {is_learning}, Type (类型): {type(is_learning)}")  # Output: Is learning (正在学习): True, Type (类型): <class 'bool'> (输出)

print("\n--- Operators (运算符) ---")

# --- Arithmetic Operators (算术运算符) ---
print("--- Arithmetic Operators (算术运算符) ---")
a = 15
b = 4
print(f"a = {a}, b = {b}")
print(f"a + b (加法): {a + b}")          # Output: 19 (输出)
print(f"a - b (减法): {a - b}")          # Output: 11 (输出)
print(f"a * b (乘法): {a * b}")          # Output: 60 (输出)
print(f"a / b (除法): {a / b}")          # Output: 3.75 (输出)
print(f"a // b (整除): {a // b}")        # Output: 3 (输出)
print(f"a % b (取余): {a % b}")          # Output: 3 (输出)
print(f"a ** b (幂运算): {a ** b}")      # Output: 50625 (15^4) (输出)

# --- Comparison Operators (比较运算符) ---
print("\n--- Comparison Operators (比较运算符) ---")
x = 10
y = 20
print(f"x = {x}, y = {y}")
print(f"x == y (等于): {x == y}")     # Output: False (输出)
print(f"x != y (不等于): {x != y}")     # Output: True (输出)
print(f"x > y (大于): {x > y}")      # Output: False (输出)
print(f"x < y (小于): {x < y}")      # Output: True (输出)
print(f"x >= 10 (大于或等于): {x >= 10}") # Output: True (输出)
print(f"y <= 15 (小于或等于): {y <= 15}") # Output: False (输出)

# --- Logical Operators (逻辑运算符) ---
print("\n--- Logical Operators (逻辑运算符) ---")
p = True
q = False
print(f"p = {p}, q = {q}")
print(f"p and q (逻辑与): {p and q}")  # Output: False (输出)
print(f"p or q (逻辑或): {p or q}")   # Output: True (输出)
print(f"not p (逻辑非): {not p}")      # Output: False (输出)

print("\nScript finished.")
# 脚本结束。
