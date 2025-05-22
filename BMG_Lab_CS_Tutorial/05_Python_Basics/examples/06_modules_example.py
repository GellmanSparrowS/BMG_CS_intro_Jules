# This script demonstrates how to import and use modules in Python.
# 本脚本演示如何在 Python 中导入和使用模块。

# --- Importing the entire module (导入整个模块) ---
print("--- Importing the entire module (导入整个模块) ---")
# 'import math' makes the entire 'math' module available.
# You access its functions and constants using `math.item_name`.
# 'import math' 使整个 'math' 模块可用。
# 你可以使用 `math.item_name` 来访问其函数和常量。
import math

square_root_of_16 = math.sqrt(16)
print(f"The square root of 16 (using math.sqrt) is: {square_root_of_16}") # Output: 4.0 (输出)
# 16的平方根 (使用 math.sqrt) 是: 4.0

value_of_pi = math.pi
print(f"The value of Pi (using math.pi) is: {value_of_pi}") # Output: 3.141592653589793 (输出)
# Pi 的值 (使用 math.pi) 是: 3.141592653589793

# --- Importing specific items from a module (从模块导入特定项目) ---
print("\n--- Importing specific items from a module (从模块导入特定项目) ---")
# 'from module_name import item1, item2' allows you to use item1 and item2 directly without the module_name prefix.
# 'from module_name import item1, item2' 允许你直接使用 item1 和 item2，而无需模块名前缀。
from math import sqrt, pi # Now sqrt and pi can be used directly (现在可以直接使用 sqrt 和 pi)

square_root_of_25 = sqrt(25)
print(f"The square root of 25 (using imported sqrt) is: {square_root_of_25}") # Output: 5.0 (输出)
# 25的平方根 (使用导入的 sqrt) 是: 5.0

print(f"The value of Pi (using imported pi) is: {pi}") # Output: 3.141592653589793 (输出)
# Pi 的值 (使用导入的 pi) 是: 3.141592653589793

# --- Importing a module with an alias (导入模块并使用别名) ---
print("\n--- Importing a module with an alias (导入模块并使用别名) ---")
# This is very common for libraries like NumPy, Pandas, etc.
# 这对于像 NumPy、Pandas 等库非常常见。
import numpy as np # 'np' is the conventional alias for numpy ('np' 是 numpy 的常规别名)

# Example: Create a NumPy array (示例：创建一个 NumPy 数组)
# This requires numpy to be installed in your environment (e.g., via 'conda install numpy')
# 这需要在你的环境中安装 numpy (例如，通过 'conda install numpy')
try:
    my_array = np.array([1, 2, 3, 4, 5])
    print(f"NumPy array created with alias 'np': {my_array}") # Output: [1 2 3 4 5] (输出)
    # 使用别名 'np' 创建的 NumPy 数组: [1 2 3 4 5]
    print(f"Type of my_array: {type(my_array)}") # Output: <class 'numpy.ndarray'> (输出)
except ImportError:
    print("NumPy library is not installed. This part of the example cannot run.")
    # NumPy 库未安装。此部分示例无法运行。
except Exception as e:
    print(f"An error occurred with NumPy: {e}")
    # 使用 NumPy 时发生错误

# You can also import specific items and give them aliases, though less common for built-ins.
# 你也可以导入特定的项目并给它们别名，尽管对于内置模块来说不太常见。
from math import factorial as fact
print(f"The factorial of 5 (5!) using 'fact' alias is: {fact(5)}") # Output: 120 (输出)
# 使用 'fact' 别名计算5的阶乘 (5!) 是: 120

print("\nScript finished.")
# 脚本结束。
