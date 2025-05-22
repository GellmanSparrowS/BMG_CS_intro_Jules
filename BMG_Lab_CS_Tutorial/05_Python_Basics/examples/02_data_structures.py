# This script demonstrates basic Python data structures: Lists, Dictionaries, and Tuples.
# 本脚本演示 Python 的基本数据结构：列表、字典和元组。

# --- Lists (列表) ---
# Lists are ordered, mutable (changeable) collections of items.
# 列表是有序的、可变的 (可以更改的) 项目集合。
print("--- Lists (列表) ---")
fruits = ["apple", "banana", "cherry"]
print(f"Initial list (初始列表): {fruits}") # Output: ['apple', 'banana', 'cherry'] (输出)

# Indexing (索引) - Accessing elements (访问元素)
first_fruit = fruits[0]  # Python indexing starts at 0 (Python 索引从0开始)
print(f"First fruit (第一个水果): {first_fruit}") # Output: apple (输出)
last_fruit = fruits[-1] # Negative indexing from the end (从末尾开始的负索引)
print(f"Last fruit (最后一个水果): {last_fruit}") # Output: cherry (输出)

# Slicing (切片) - Getting a sublist (获取子列表)
# fruits[start:stop] - 'stop' index is not included (不包括 'stop' 索引)
some_fruits = fruits[0:2] # Gets elements at index 0 and 1 (获取索引0和1处的元素)
print(f"Slice [0:2] (切片 [0:2]): {some_fruits}") # Output: ['apple', 'banana'] (输出)

# append() - Add an item to the end (在末尾添加一个项目)
fruits.append("orange")
print(f"After append('orange') (添加 'orange' 后): {fruits}") # Output: ['apple', 'banana', 'cherry', 'orange'] (输出)

# pop() - Remove and return an item at a given index (or the last item if index is not specified)
# pop() - 移除并返回指定索引处的项目 (如果未指定索引，则为最后一个项目)
removed_fruit = fruits.pop(1) # Removes 'banana' (移除 'banana')
print(f"Removed fruit at index 1 (移除索引1处的水果): {removed_fruit}") # Output: banana (输出)
print(f"List after pop(1) (pop(1) 后的列表): {fruits}") # Output: ['apple', 'cherry', 'orange'] (输出)

# len() - Get the number of items in a list (获取列表中的项目数)
print(f"Length of list (列表长度): {len(fruits)}") # Output: 3 (输出)

# --- Dictionaries (字典) ---
# Dictionaries are unordered (in Python < 3.7) or ordered (Python 3.7+) collections of key-value pairs.
# Mutable and keys must be unique and immutable.
# 字典是键值对的无序 (Python < 3.7) 或有序 (Python 3.7+) 集合。
# 可变，并且键必须是唯一的且不可变的。
print("\n--- Dictionaries (字典) ---")
student = {"name": "John Doe", "age": 22, "major": "Physics"}
print(f"Initial dictionary (初始字典): {student}") # Output: {'name': 'John Doe', 'age': 22, 'major': 'Physics'} (输出)

# Accessing values using keys (使用键访问值)
student_name = student["name"]
print(f"Student name (学生姓名): {student_name}") # Output: John Doe (输出)
student_age = student.get("age") # Using get() is safer if key might not exist (如果键可能不存在，使用 get() 更安全)
print(f"Student age (using get()) (学生年龄 (使用 get())): {student_age}") # Output: 22 (输出)

# Adding/Modifying entries (添加/修改条目)
student["major"] = "Computational Physics" # Modify existing entry (修改现有条目)
student["graduation_year"] = 2025      # Add new entry (添加新条目)
print(f"Updated dictionary (更新后的字典): {student}")
# Output: {'name': 'John Doe', 'age': 22, 'major': 'Computational Physics', 'graduation_year': 2025} (输出)

# keys() - Get all keys (获取所有键)
print(f"Keys: {student.keys()}") # Output: dict_keys(['name', 'age', 'major', 'graduation_year']) (输出)

# values() - Get all values (获取所有值)
print(f"Values: {student.values()}") # Output: dict_values(['John Doe', 22, 'Computational Physics', 2025]) (输出)

# items() - Get all key-value pairs (获取所有键值对)
print(f"Items: {student.items()}") # Output: dict_items([('name', 'John Doe'), ...]) (输出)

# --- Tuples (元组) ---
# Tuples are ordered, immutable (unchangeable) collections of items.
# 元组是有序的、不可变的 (不能更改的) 项目集合。
print("\n--- Tuples (元组) ---")
coordinates = (10.0, 20.5, -5.2)
print(f"Tuple (元组): {coordinates}") # Output: (10.0, 20.5, -5.2) (输出)

# Accessing elements (访问元素) - same as lists (与列表相同)
x_coord = coordinates[0]
print(f"X-coordinate (X坐标): {x_coord}") # Output: 10.0 (输出)

# Tuples are immutable - you cannot change their content after creation
# 元组是不可变的 - 创建后无法更改其内容
# coordinates[0] = 5.0  # This would raise a TypeError (这会引发 TypeError)

print("\nScript finished.")
# 脚本结束。
