# This script demonstrates Python control flow statements: if/elif/else, for loops, and while loops.
# 本脚本演示 Python 的控制流语句：if/elif/else、for 循环和 while 循环。

# --- Conditional Statements (if/elif/else - 条件语句) ---
print("--- Conditional Statements (条件语句) ---")
score = 85
# score = 85 (分数)

if score >= 90:
    grade = "A"
    # 等级 A
elif score >= 80:
    grade = "B"
    # 等级 B
elif score >= 70:
    grade = "C"
    # 等级 C
else:
    grade = "D"
    # 等级 D
print(f"Score (分数): {score}, Grade (等级): {grade}") # Output: Score (分数): 85, Grade (等级): B (输出)

# --- For Loops (for 循环) ---
print("\n--- For Loops (for 循环) ---")

# Iterating over a list (遍历列表)
print("Iterating over a list (遍历列表):")
colors = ["red", "green", "blue"]
for color in colors:
    print(f"- {color}")
# Output: - red, - green, - blue (each on a new line - 每行输出一个)

# Iterating with range() (使用 range() 遍历)
# range(n) generates numbers from 0 up to (but not including) n.
# range(n) 生成从 0 到 n (但不包括 n) 的数字。
print("\nIterating with range(5):")
for i in range(5):
    print(f"Number: {i}")
# Output: Number: 0, Number: 1, Number: 2, Number: 3, Number: 4 (输出)

# --- While Loops (while 循环) ---
print("\n--- While Loops (while 循环) ---")
count = 0
while count < 4:
    print(f"Current count (当前计数): {count}")
    count += 1 # Equivalent to count = count + 1 (等同于 count = count + 1)
# Output: Current count (当前计数): 0, Current count (当前计数): 1, Current count (当前计数): 2, Current count (当前计数): 3 (输出)

# --- Break and Continue in Loops (循环中的 break 和 continue) ---
print("\n--- Break and Continue ---")
print("Using 'continue' to skip an iteration, and 'break' to exit loop:")
# 使用 'continue' 跳过迭代，使用 'break' 退出循环：
for num in range(10): # 0 to 9 (0 到 9)
    if num == 3:
        print("Skipping number 3 with 'continue'. (使用 'continue' 跳过数字 3。)")
        continue  # Go to the next iteration (跳到下一次迭代)
    if num == 7:
        print("Exiting loop with 'break' at number 7. (在数字 7 处使用 'break' 退出循环。)")
        break     # Exit the loop completely (完全退出循环)
    print(f"Processed number (已处理数字): {num}")
# Output:
# Processed number (已处理数字): 0
# Processed number (已处理数字): 1
# Processed number (已处理数字): 2
# Skipping number 3 with 'continue'. (使用 'continue' 跳过数字 3。)
# Processed number (已处理数字): 4
# Processed number (已处理数字): 5
# Processed number (已处理数字): 6
# Exiting loop with 'break' at number 7. (在数字 7 处使用 'break' 退出循环。)

print("\nScript finished.")
# 脚本结束。
