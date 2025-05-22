# This script demonstrates defining and using functions in Python.
# 本脚本演示如何在 Python 中定义和使用函数。

# --- Defining a Simple Function (定义简单函数) ---
print("--- Defining and Calling a Simple Function (定义并调用简单函数) ---")

def greet():
    """This function prints a simple greeting. (此函数打印一个简单的问候语。)"""
    message = "Hello from the greet() function!"
    # 来自 greet() 函数的消息！
    print(message)

# Calling the function (调用函数)
greet() # Output: Hello from the greet() function! (输出)

# --- Function with Parameters (带参数的函数) ---
print("\n--- Function with Parameters (带参数的函数) ---")

def greet_person(name):
    """This function greets a person with their name. (此函数用姓名问候一个人。)"""
    message = f"Hello, {name}! Welcome."
    # 你好，{name}！欢迎。
    print(message)

greet_person("Dr. Ada")  # Output: Hello, Dr. Ada! Welcome. (输出)
greet_person("BMG Student") # Output: Hello, BMG Student! Welcome. (输出)

# --- Function with a Return Value (带返回值的函数) ---
print("\n--- Function with a Return Value (带返回值的函数) ---")

def add_numbers(num1, num2):
    """This function adds two numbers and returns the sum. (此函数将两个数字相加并返回总和。)"""
    total = num1 + num2
    return total

# Calling the function and storing the result (调用函数并存储结果)
sum_result = add_numbers(5, 7)
print(f"The sum of 5 and 7 is: {sum_result}") # Output: The sum of 5 and 7 is: 12 (输出)

another_sum = add_numbers(10.5, 2.3)
print(f"The sum of 10.5 and 2.3 is: {another_sum}") # Output: The sum of 10.5 and 2.3 is: 12.8 (输出)

# --- Function with Default Parameter Value (带默认参数值的函数) ---
print("\n--- Function with Default Parameter Value (带默认参数值的函数) ---")

def power(number, exponent=2):
    """
    Calculates number to the power of exponent.
    If exponent is not provided, it defaults to 2.
    计算数字的指数幂。
    如果未提供指数，则默认为2。
    """
    return number ** exponent

print(f"3 to the power of 2 (3的2次方): {power(3)}")       # Output: 9 (exponent defaults to 2 - 指数默认为2) (输出)
print(f"3 to the power of 3 (3的3次方): {power(3, 3)}")   # Output: 27 (exponent is 3 - 指数为3) (输出)

# --- Variable Scope (变量作用域) ---
print("\n--- Variable Scope (变量作用域) ---")

global_variable = "I am global"
# 我是全局变量

def scope_test():
    local_variable = "I am local to scope_test"
    # 我是 scope_test 函数的局部变量
    print(f"Inside function (函数内部): global_variable = '{global_variable}'") # Can access global (可以访问全局变量)
    print(f"Inside function (函数内部): local_variable = '{local_variable}'")

scope_test()
# Output:
# Inside function (函数内部): global_variable = 'I am global'
# Inside function (函数内部): local_variable = 'I am local to scope_test'

print(f"\nOutside function (函数外部): global_variable = '{global_variable}'") # Output: 'I am global' (输出)
# print(local_variable) # This would cause a NameError because local_variable is not defined globally
# 上面这行会引发 NameError，因为 local_variable 未在全局定义

# --- Docstrings (文档字符串) ---
print("\n--- Docstrings (文档字符串) ---")
# A docstring is a string literal that occurs as the first statement in a module, function, class, or method definition.
# It is used to explain what the function/module/class does.
# 文档字符串是出现在模块、函数、类或方法定义中第一个语句的字符串字面量。
# 它用于解释函数/模块/类等的功能。
# You can access it using help() or the __doc__ attribute.
# 你可以使用 help() 或 __doc__ 属性来访问它。

print(f"Docstring for 'greet_person' function (greet_person 函数的文档字符串):\n{greet_person.__doc__}")
# Output: Docstring for 'greet_person' function (greet_person 函数的文档字符串):
# This function greets a person with their name. (此函数用姓名问候一个人。)

help(add_numbers) # This will print the docstring for add_numbers as well. (这也将打印 add_numbers 的文档字符串。)

print("\nScript finished.")
# 脚本结束。
