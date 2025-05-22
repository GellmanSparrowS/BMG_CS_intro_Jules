# 05 - Python Programming Basics (Python 基础编程)

## Why Python for Scientific Computing? (为什么选择 Python 进行科学计算?)
Python is a popular choice for scientific computing for several key reasons:
Python 因其几个关键原因而成为科学计算的热门选择：
*   **Readability (易读性):** Python's syntax is designed to be clear and easy to read, similar to plain English. This makes it easier to learn and maintain code.
    **易读性 (Readability):** Python 的语法设计清晰易读，类似于普通英语。这使得学习和维护代码更加容易。
*   **Extensive Scientific Libraries (丰富的科学计算库):** Python has a vast ecosystem of powerful libraries specifically for scientific tasks. Some of the most notable include:
    **丰富的科学计算库 (Extensive Scientific Libraries):** Python 拥有一个庞大的、专为科学任务设计的强大库生态系统。其中一些最著名的包括：
    *   **NumPy:** For numerical operations, especially with arrays and matrices. (用于数值运算，特别是数组和矩阵。)
    *   **SciPy:** Builds on NumPy and provides a large number of functions that operate on NumPy arrays and are useful for different types of scientific and engineering applications. (基于 NumPy 构建，提供了大量操作 NumPy 数组的函数，可用于不同类型的科学和工程应用。)
    *   **Pandas:** For data manipulation and analysis, particularly with structured data (like tables). (用于数据操作和分析，特别是结构化数据 (如表格)。)
    *   **Matplotlib:** For creating static, animated, and interactive visualizations. (用于创建静态、动画和交互式可视化图表。)
*   **Strong Community (强大的社区):** Python has a large and active global community. This means plenty of online resources, tutorials, forums for help, and continuous development of new tools.
    **强大的社区 (Strong Community):** Python 拥有一个庞大且活跃的全球社区。这意味着有大量的在线资源、教程、可寻求帮助的论坛以及新工具的持续开发。

## Getting Started (入门)

### Running Python Code (运行 Python 代码)
*   **Interactive Mode (交互模式):**
    You can run Python code interactively by typing `python` in your terminal (Anaconda Prompt, or any terminal where `python` is in your PATH).
    你可以在终端 (Anaconda Prompt 或任何 `python` 在系统路径中的终端) 中输入 `python` 来交互式地运行 Python 代码。
    This opens the Python interpreter, indicated by `>>>`. You can type Python commands directly.
    这将打开 Python 解释器，提示符为 `>>>`。你可以直接输入 Python 命令。
    ```python
    # Example in interactive mode (交互模式示例)
    # >>> print("Hello, BMG Lab!")
    # Hello, BMG Lab!
    # >>> 3 + 5
    # 8
    ```
    To exit the interactive mode, type `exit()` or `quit()`.
    要退出交互模式，请输入 `exit()` 或 `quit()`。
*   **Running Scripts (运行脚本文件):**
    For more complex programs, you'll save your code in a file with a `.py` extension (e.g., `myscript.py`).
    对于更复杂的程序，你会将代码保存在一个以 `.py` 为扩展名的文件中 (例如 `myscript.py`)。
    You then run this script from the terminal using:
    然后你可以使用以下命令从终端运行此脚本：
    ```bash
    python myscript.py
    ```

### Comments (注释)
Comments are used to explain your code. They are ignored by the Python interpreter.
注释用于解释你的代码。Python 解释器会忽略它们。
In Python, a comment starts with a hash symbol (`#`) and extends to the end of the line.
在 Python 中，注释以井号 (`#`) 开始，并延伸到该行的末尾。
```python
# This is a single-line comment explaining something.
# 这是解释某些内容的单行注释。
x = 10  # This comment is after some code. (这行注释在代码之后。)
```

## Python Variables and Data Types (Python 变量和数据类型)

### Variables (变量)
A variable is a name that refers to a value. Think of it as a label for a storage location.
变量是引用值的名称。可以将其视为存储位置的标签。
*   **Assignment (赋值):** You use the equals sign (`=`) to assign a value to a variable.
    **赋值 (Assignment):** 使用等号 (`=`) 将值赋给变量。
    ```python
    age = 30
    name = "BMG Lab"
    ```
*   **Naming Rules (命名规则):**
    *   Variable names can contain letters, numbers, and underscores (`_`).
        变量名可以包含字母、数字和下划线 (`_`)。
    *   They cannot start with a number.
        它们不能以数字开头。
    *   They are case-sensitive (`myVariable` is different from `myvariable`).
        它们区分大小写 (`myVariable` 不同于 `myvariable`)。
    *   Avoid using Python keywords (like `if`, `for`, `class`) as variable names.
        避免使用 Python 关键字 (如 `if`, `for`, `class`) 作为变量名。

### Common Data Types (常用数据类型)
Python has several built-in data types. Here are the most common:
Python 有几种内置数据类型。以下是最常见的：

*   **Integers (`int` - 整数):** Whole numbers, positive or negative, without decimals.
    **整数 (`int` - Integers):** 正或负的整数，不带小数点。
    ```python
    x = 10
    count = -5
    print(type(x))  # Output: <class 'int'> (输出)
    ```
*   **Floating-point numbers (`float` - 浮点数):** Numbers with a decimal point, or in exponential form.
    **浮点数 (`float` - Floating-point numbers):** 带小数点的数字，或指数形式的数字。
    ```python
    y = 3.14
    temperature = -2.5
    scientific_notation = 1.2e3  # Represents 1.2 * 10^3 = 1200.0 (表示)
    print(type(y))  # Output: <class 'float'> (输出)
    ```
*   **Strings (`str` - 字符串):** Sequences of characters, used for text. You can use single (`'`) or double (`"`) quotes.
    **字符串 (`str` - Strings):** 字符序列，用于文本。你可以使用单引号 (`'`) 或双引号 (`"`)。
    ```python
    lab_name = "BMG Lab"
    message = 'Hello, World!'
    print(type(lab_name))  # Output: <class 'str'> (输出)

    # String concatenation (字符串拼接)
    greeting = "Hello, " + lab_name
    print(greeting)  # Output: Hello, BMG Lab (输出)

    # f-strings (formatted string literals - 格式化字符串字面量) - Recommended for formatting
    # f-string (推荐用于格式化)
    version = 1.0
    info = f"{lab_name} Tutorial, version {version}"
    print(info)  # Output: BMG Lab Tutorial, version 1.0 (输出)
    ```
*   **Booleans (`bool` - 布尔型):** Represent truth values, either `True` or `False`.
    **布尔型 (`bool` - Booleans):** 表示真值，只有 `True` 或 `False`。
    ```python
    is_active = True
    is_ready = False
    print(type(is_active))  # Output: <class 'bool'> (输出)
    ```

### `type()` function (type() 函数)
You can use the `type()` function to check the data type of any variable.
你可以使用 `type()` 函数来检查任何变量的数据类型。
```python
number = 100
print(type(number)) # Output: <class 'int'> (输出)
pi_value = 3.14159
print(type(pi_value)) # Output: <class 'float'> (输出)
text = "Python is fun"
print(type(text)) # Output: <class 'str'> (输出)
```

## Operators (运算符)

### Arithmetic Operators (算术运算符)
Perform mathematical calculations.
执行数学计算。
```python
a = 10
b = 3

print(f"a + b = {a + b}")    # Addition (加法): 13
print(f"a - b = {a - b}")    # Subtraction (减法): 7
print(f"a * b = {a * b}")    # Multiplication (乘法): 30
print(f"a / b = {a / b}")    # Division (除法): 3.333...
print(f"a // b = {a // b}")   # Floor Division (整除): 3 (discards remainder - 舍去余数)
print(f"a % b = {a % b}")    # Modulo (取余): 1 (remainder of division - 除法的余数)
print(f"a ** b = {a ** b}")  # Exponentiation (幂运算): 10^3 = 1000
```

### Comparison Operators (比较运算符)
Compare two values and return a Boolean (`True` or `False`).
比较两个值并返回一个布尔值 (`True` 或 `False`)。
```python
x = 5
y = 10

print(f"x == y: {x == y}")  # Equal to (等于): False
print(f"x != y: {x != y}")  # Not equal to (不等于): True
print(f"x > y: {x > y}")   # Greater than (大于): False
print(f"x < y: {x < y}")   # Less than (小于): True
print(f"x >= 5: {x >= 5}") # Greater than or equal to (大于或等于): True
print(f"y <= 10: {y <= 10}")# Less than or equal to (小于或等于): True
```

### Logical Operators (逻辑运算符)
Combine Boolean expressions.
组合布尔表达式。
```python
p = True
q = False

print(f"p and q: {p and q}")  # Logical AND (逻辑与): False (True if both are true - 仅当两者都为真时为真)
print(f"p or q: {p or q}")   # Logical OR (逻辑或): True (True if at least one is true - 只要有一个为真即为真)
print(f"not p: {not p}")      # Logical NOT (逻辑非): False (Inverts the boolean value - 反转布尔值)
```

## Basic Data Structures (基本数据结构)

### Lists (列表)
A list is an ordered collection of items, which can be of different types. Lists are mutable (changeable).
列表是一个有序的项目集合，项目可以是不同类型的。列表是可变的 (可以更改)。
```python
# Creating a list (创建列表)
my_list = [1, "hello", 3.0, True]
print(my_list)  # Output: [1, 'hello', 3.0, True] (输出)

# Accessing elements (访问元素) - indexing starts at 0 (索引从0开始)
print(f"First element: {my_list[0]}")   # Output: 1 (第一个元素)
print(f"Second element: {my_list[1]}")  # Output: 'hello' (第二个元素)

# Negative indexing (负索引) - starts from the end (从末尾开始)
print(f"Last element: {my_list[-1]}")   # Output: True (最后一个元素)

# Slicing (切片) - get a sublist (获取子列表) [start:stop:step] (stop is exclusive - 不包含stop)
print(f"Slice [1:3]: {my_list[1:3]}") # Output: ['hello', 3.0] (从索引1到索引3之前)

# Common methods (常用方法)
my_list.append("new_item")    # Add item to the end (在末尾添加项目)
print(my_list)              # Output: [1, 'hello', 3.0, True, 'new_item'] (输出)
my_list.insert(1, "Python") # Insert "Python" at index 1 (在索引1处插入 "Python")
print(my_list)              # Output: [1, 'Python', 'hello', 3.0, True, 'new_item'] (输出)
my_list.remove(3.0)         # Remove the first occurrence of 3.0 (移除第一个出现的3.0)
print(my_list)              # Output: [1, 'Python', 'hello', True, 'new_item'] (输出)
popped_item = my_list.pop(0) # Remove and return item at index 0 (移除并返回索引0处的项目)
print(f"Popped item: {popped_item}, List now: {my_list}")
# Output: Popped item: 1, List now: ['Python', 'hello', True, 'new_item'] (输出)
print(f"Length of list: {len(my_list)}") # Get length (获取长度) Output: 4 (输出)
```

### Tuples (元组)
A tuple is an ordered collection of items, similar to a list, but tuples are immutable (unchangeable) once created.
元组是一个有序的项目集合，类似于列表，但元组在创建后是不可变的 (不能更改)。
```python
# Creating a tuple (创建元组)
my_tuple = (1, "hello", 3.0, True)
print(my_tuple)  # Output: (1, 'hello', 3.0, True) (输出)

# Accessing elements and slicing (访问元素和切片) - same as lists (与列表相同)
print(f"First element: {my_tuple[0]}")  # Output: 1 (输出)
print(f"Slice [1:3]: {my_tuple[1:3]}") # Output: ('hello', 3.0) (输出)

# Tuples are immutable (元组是不可变的)
# my_tuple[0] = 5  # This would cause a TypeError (这会引发 TypeError)
```

### Dictionaries (字典)
A dictionary is an unordered collection of key-value pairs (in Python 3.7+ dictionaries are ordered). Keys must be unique and immutable (e.g., strings, numbers, tuples). Dictionaries are mutable.
字典是键值对的无序集合 (在 Python 3.7+ 版本中字典是有序的)。键必须是唯一的且不可变的 (例如字符串、数字、元组)。字典是可变的。
```python
# Creating a dictionary (创建字典)
my_dict = {"name": "BMG Lab", "project": "Tutorial", "year": 2024}
print(my_dict)  # Output: {'name': 'BMG Lab', 'project': 'Tutorial', 'year': 2024} (输出)

# Accessing values using keys (使用键访问值)
print(f"Project name: {my_dict['project']}")  # Output: Tutorial (输出)

# Adding or modifying entries (添加或修改条目)
my_dict["year"] = 2025          # Modify existing entry (修改现有条目)
my_dict["language"] = "Python" # Add new entry (添加新条目)
print(my_dict)
# Output: {'name': 'BMG Lab', 'project': 'Tutorial', 'year': 2025, 'language': 'Python'} (输出)

# Common methods (常用方法)
print(f"Keys: {my_dict.keys()}")      # Get all keys (获取所有键)
print(f"Values: {my_dict.values()}")  # Get all values (获取所有值)
print(f"Items: {my_dict.items()}")    # Get all key-value pairs (获取所有键值对)
```

## Control Flow (控制流)

### Conditional Statements (`if`, `elif`, `else` - 条件语句)
Execute code based on whether a condition is true or false.
根据条件是真还是假来执行代码。
```python
temperature = 25

if temperature > 30:
    print("It's a hot day!") # 天气炎热！
elif temperature > 20: # 'elif' is short for 'else if' ('elif' 是 'else if' 的缩写)
    print("It's a pleasant day.") # 天气宜人。
else:
    print("It might be cold.") # 可能有点冷。
# Output: It's a pleasant day. (输出)
```
Indentation (spaces at the beginning of a line) is very important in Python; it defines blocks of code.
缩进 (行首的空格) 在 Python 中非常重要；它定义了代码块。

### Loops (循环)
Used to repeat a block of code.
用于重复执行一段代码块。

*   **`for` loops (for 循环):** Iterate over a sequence (like a list, tuple, string, or range).
    **`for` 循环 (for loops):** 遍历一个序列 (如列表、元组、字符串或范围)。
    ```python
    # Looping through a list (遍历列表)
    colors = ["red", "green", "blue"]
    for color in colors:
        print(color)
    # Output: red, then green, then blue (each on a new line - 每一行输出一个)

    # Looping using range() (使用 range() 循环)
    # range(5) generates numbers from 0 to 4 (range(5) 生成从0到4的数字)
    for i in range(5):
        print(f"Number: {i}")
    # Output: Number: 0, Number: 1, ..., Number: 4 (输出)
    ```

*   **`while` loops (while 循环):** Repeat as long as a condition is true.
    **`while` 循环 (while loops):** 只要条件为真就重复执行。
    ```python
    count = 0
    while count < 3:
        print(f"Count is {count}")
        count = count + 1  # Important: update the condition variable (重要：更新条件变量)
    # Output: Count is 0, Count is 1, Count is 2 (输出)
    ```

*   **`break` and `continue` statements (`break` 和 `continue` 语句):**
    *   `break`: Exits the current loop entirely.
        `break`: 完全退出当前循环。
    *   `continue`: Skips the rest of the current iteration and proceeds to the next iteration of the loop.
        `continue`: 跳过当前迭代的剩余部分，并继续下一次循环迭代。
    ```python
    for num in range(10):
        if num == 3:
            continue  # Skip printing 3 (跳过打印3)
        if num == 7:
            break     # Exit loop when num is 7 (当num为7时退出循环)
        print(num)
    # Output: 0, 1, 2, 4, 5, 6 (输出)
    ```

## Functions (函数)
A function is a reusable block of code that performs a specific task.
函数是一个可重用的代码块，用于执行特定任务。

### Defining Functions (`def` - 定义函数)
Use the `def` keyword.
使用 `def` 关键字。
```python
def greet(name):
    """This function greets the person passed in as a parameter.""" # This is a docstring (这是文档字符串)
    # 上面这行是文档字符串，用于解释函数的功能。
    message = f"Hello, {name}!"
    return message

# Calling the function (调用函数)
greeting_message = greet("BMG Student")
print(greeting_message)  # Output: Hello, BMG Student (输出)
```
*   **Parameters (参数):** Input values to the function (e.g., `name` in `greet(name)`).
    **参数 (Parameters):** 函数的输入值 (例如 `greet(name)` 中的 `name`)。
*   **Return Value (返回值):** The output of the function, specified by the `return` keyword. If no `return` statement is used, the function returns `None` by default.
    **返回值 (Return Value):** 函数的输出，由 `return` 关键字指定。如果没有 `return` 语句，函数默认返回 `None`。
*   **Docstrings (文档字符串):** A string literal (often triple-quoted) as the first statement in a function's body, used to document what the function does.
    **文档字符串 (Docstrings):** 函数体中第一个语句的字符串字面量 (通常是三引号)，用于记录函数的功能。

### Variable Scope (变量作用域)
*   **Local Variables (局部变量):** Variables defined inside a function are local to that function and cannot be accessed outside it.
    **局部变量 (Local Variables):** 在函数内部定义的变量是该函数的局部变量，不能在函数外部访问。
*   **Global Variables (全局变量):** Variables defined outside of any function are global and can be accessed (but not directly modified within functions without the `global` keyword, which is generally discouraged for beginners).
    **全局变量 (Global Variables):** 在任何函数外部定义的变量是全局变量，可以被访问 (但在函数内部若要直接修改，需要使用 `global` 关键字，通常不建议初学者这样做)。

## File Input/Output (文件输入/输出) (Simple - 简单示例)
Interacting with files.
与文件交互。

### Reading from a text file (读取文本文件)
```python
# Assume 'myfile.txt' exists with content: (假设 'myfile.txt' 文件存在且内容如下：)
# Line 1
# Line 2

# 'with open(...) as f:' ensures the file is properly closed afterwards.
# 'with open(...) as f:' 确保文件在使用后正确关闭。
try:
    with open("myfile.txt", "r") as f:  # "r" for read mode ( "r" 表示读取模式)
        # content = f.read()      # Read the entire file into one string (读取整个文件到一个字符串)
        # print(f"Full content:\n{content}")

        # line = f.readline()     # Read one line at a time (一次读取一行)
        # print(f"First line: {line.strip()}") # .strip() removes leading/trailing whitespace (移除首尾空白)

        lines = f.readlines()   # Read all lines into a list of strings (读取所有行到一个字符串列表)
        print("Content by lines:")
        for line in lines:
            print(line.strip()) # .strip() is useful here too (在这里也很有用)
except FileNotFoundError:
    print("Error: myfile.txt not found.") # 错误：未找到 myfile.txt
```

### Writing to a text file (写入文本文件)
```python
# "w" for write mode. Creates the file if it doesn't exist, overwrites it if it does.
# "w" 表示写入模式。如果文件不存在则创建，如果存在则覆盖。
with open("output.txt", "w") as f:
    f.write("This is the first line.\n")
    f.write("This is another line.\n")

# To append to a file, use mode "a" (要追加到文件，请使用模式 "a")
# with open("output.txt", "a") as f:
#     f.write("This line is appended.\n")
```

## Modules and `import` (模块和导入)
Modules are Python files (`.py`) containing definitions and statements (functions, variables, classes). They help organize code and provide reusable functionality.
模块是包含定义和语句 (函数、变量、类) 的 Python 文件 (`.py`)。它们有助于组织代码并提供可重用的功能。

*   **`import <module_name>`:** Imports the entire module. You access its contents using `module_name.item_name`.
    **`import <module_name>`:** 导入整个模块。使用 `module_name.item_name` 访问其内容。
    ```python
    import math
    print(math.sqrt(16))  # Output: 4.0 (输出)
    print(math.pi)        # Output: 3.14159... (输出)
    ```
*   **`from <module_name> import <item_name>`:** Imports a specific item (function, variable) from a module directly into your current namespace.
    **`from <module_name> import <item_name>`:** 从模块中直接导入特定的项目 (函数、变量)到你当前的命名空间。
    ```python
    from math import sqrt, pi
    print(sqrt(25))  # Output: 5.0 (输出)
    print(pi)        # Output: 3.14159... (输出)
    ```
*   **`import <module_name> as <alias>`:** Imports a module and gives it an alias (a shorter name). This is very common for libraries like NumPy and Pandas.
    **`import <module_name> as <alias>`:** 导入一个模块并给它一个别名 (一个更短的名称)。这对于像 NumPy 和 Pandas 这样的库非常常见。
    ```python
    import numpy as np
    # array = np.array([1, 2, 3]) # Example of using NumPy (使用 NumPy 的示例)
    ```

This is a brief introduction to Python basics. Practice is key to mastering these concepts!
这是 Python 基础知识的简要介绍。练习是掌握这些概念的关键！

### Code Examples (代码示例)
The `examples/` subdirectory within this section contains Python scripts demonstrating the concepts discussed above.
本节中的 `examples/` 子目录包含演示上述概念的 Python 脚本。
You can run these scripts from your terminal while navigated to the `05_Python_Basics` directory.
你可以从终端导航到 `05_Python_Basics` 目录后运行这些脚本。

1.  **`examples/01_data_types_and_operators.py`**
    *   Demonstrates basic data types (integers, floats, strings, booleans) and common operators (arithmetic, comparison, logical).
        演示基本数据类型 (整数、浮点数、字符串、布尔型) 和常用运算符 (算术、比较、逻辑)。
    *   To run (运行): `python examples/01_data_types_and_operators.py`

2.  **`examples/02_data_structures.py`**
    *   Shows how to use lists, dictionaries, and tuples, including common operations.
        展示如何使用列表、字典和元组，包括常用操作。
    *   To run (运行): `python examples/02_data_structures.py`

3.  **`examples/03_control_flow.py`**
    *   Illustrates conditional statements (`if/elif/else`), `for` loops, and `while` loops, along with `break` and `continue`.
        说明条件语句 (`if/elif/else`)、`for` 循环、`while` 循环，以及 `break` 和 `continue`。
    *   To run (运行): `python examples/03_control_flow.py`

4.  **`examples/04_functions.py`**
    *   Covers defining functions, using parameters, return values, default arguments, and basic variable scope.
        涵盖定义函数、使用参数、返回值、默认参数以及基本变量作用域。
    *   To run (运行): `python examples/04_functions.py`

5.  **`examples/05_file_io.py`**
    *   Demonstrates how to write to and read from text files using `with open()`.
        演示如何使用 `with open()` 写入和读取文本文件。
    *   To run (运行): `python examples/05_file_io.py`
        (This script will create a `sample_output.txt` file in the `examples` directory. - 此脚本将在 `examples` 目录中创建一个 `sample_output.txt` 文件。)

6.  **`examples/06_modules_example.py`**
    *   Shows how to import modules (`math`) and specific functions from modules, including using aliases (`numpy as np`).
        展示如何导入模块 (`math`) 和模块中的特定函数，包括使用别名 (`numpy as np`)。
    *   To run (运行): `python examples/06_modules_example.py`
        (Note: The NumPy part requires NumPy to be installed in your environment. - 注意：NumPy 部分需要在你的环境中安装 NumPy。)
