# This script demonstrates basic file input/output (I/O) operations in Python.
# 本脚本演示 Python 中的基本文件输入/输出 (I/O) 操作。

# --- Writing to a Text File (写入文本文件) ---
print("--- Writing to a Text File (写入文本文件) ---")

file_content_to_write = """Hello BMG Lab!
This is a tutorial on Python file I/O.
We are writing multiple lines to this file.
Python makes file operations straightforward.
你好 BMG 实验室！
这是一个关于 Python 文件 I/O 的教程。
我们正在向这个文件写入多行内容。
Python 使文件操作变得简单直接。
"""

# The 'w' mode opens the file for writing.
# If the file exists, its content is overwritten. If it doesn't exist, it's created.
# 'w' 模式打开文件用于写入。
# 如果文件存在，其内容将被覆盖。如果文件不存在，则会创建它。
file_path = "sample_output.txt"
try:
    with open(file_path, "w", encoding="utf-8") as f: # Using utf-8 encoding is good practice (使用 utf-8 编码是个好习惯)
        f.write(file_content_to_write)
    print(f"Successfully wrote to '{file_path}' (已成功写入 '{file_path}')")
except IOError as e:
    print(f"Error writing to file (写入文件时出错): {e}")

# --- Reading from a Text File (读取文本文件) ---
print("\n--- Reading from a Text File (读取文本文件) ---")

# The 'r' mode opens the file for reading. This is the default mode.
# 'r' 模式打开文件用于读取。这是默认模式。
try:
    with open(file_path, "r", encoding="utf-8") as f:
        print(f"\nReading the entire content of '{file_path}':")
        # 读取 '{file_path}' 的全部内容：
        full_content = f.read()
        print(full_content)

    with open(file_path, "r", encoding="utf-8") as f:
        print(f"\nReading '{file_path}' line by line:")
        # 逐行读取 '{file_path}'：
        for line in f:
            print(f"Line: {line.strip()}") # .strip() removes leading/trailing newline characters (移除前导/尾随的换行符)

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found. (错误：未找到文件 '{file_path}'。)")
except IOError as e:
    print(f"Error reading file (读取文件时出错): {e}")


# --- Appending to a Text File (追加到文本文件) ---
print("\n--- Appending to a Text File (追加到文本文件) ---")
# The 'a' mode opens the file for appending. New data is written to the end of the file.
# If the file doesn't exist, it's created.
# 'a' 模式打开文件用于追加。新数据会写入文件末尾。
# 如果文件不存在，则会创建它。
try:
    with open(file_path, "a", encoding="utf-8") as f:
        f.write("\nThis is an appended line.\n")
        # 这是追加的一行。
        f.write("Another appended line.\n")
        # 另一行追加的内容。
    print(f"Successfully appended to '{file_path}' (已成功追加到 '{file_path}')")

    # Verify by reading again (再次读取以验证)
    with open(file_path, "r", encoding="utf-8") as f:
        print(f"\nContent of '{file_path}' after appending:")
        # 追加后 '{file_path}' 的内容：
        appended_content = f.read()
        print(appended_content)

except IOError as e:
    print(f"Error appending to file (追加到文件时出错): {e}")


print("\nScript finished.")
# 脚本结束。
