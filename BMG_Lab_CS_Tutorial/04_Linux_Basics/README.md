# 04 - Linux Basics (Linux 基础命令)

## Why Learn Linux for Scientific Computing? (为什么要在科学计算中学习 Linux?)
Many High-Performance Computing (HPC) clusters, servers, and a lot of scientific software run on the Linux operating system.
许多高性能计算 (HPC) 集群、服务器以及大量的科学软件都在 Linux 操作系统上运行。
Linux is known for its stability, flexibility, and open-source nature, making it a powerful environment for research.
Linux 以其稳定性、灵活性和开源特性而闻名，使其成为一个强大的研究环境。
Understanding basic Linux commands is essential for navigating these systems and running your analyses.
理解基本的 Linux 命令对于操作这些系统和运行你的分析至关重要。

## Connecting to a Linux Server (连接到 Linux 服务器) (Optional but Recommended - 可选但推荐)
Often, you'll work on a remote Linux server or cluster. SSH (Secure Shell) is the standard way to connect.
通常，你会在远程的 Linux 服务器或集群上工作。SSH (安全外壳协议) 是标准的连接方式。
SSH provides a secure, encrypted connection between your computer and the remote server.
SSH 在你的计算机和远程服务器之间提供了一个安全的、加密的连接。

To connect, you typically use the `ssh` command in your local terminal (macOS or Linux) or an SSH client like PuTTY (on Windows):
要连接，你通常在本地终端 (macOS 或 Linux) 中使用 `ssh` 命令，或者在 Windows 上使用像 PuTTY 这样的 SSH 客户端：
```bash
ssh username@server_address
```
*   `username`: Your username on the remote server.
    `username`: 你在远程服务器上的用户名。
*   `server_address`: The IP address or hostname of the server (e.g., `mycluster.uni.edu`).
    `server_address`: 服务器的 IP 地址或主机名 (例如 `mycluster.uni.edu`)。
You will be prompted for your password.
系统会提示你输入密码。

For Windows users, PuTTY is a popular free SSH client. You can download it and enter the server address in its configuration window.
对于 Windows 用户，PuTTY 是一款流行的免费 SSH 客户端。你可以下载它并在其配置窗口中输入服务器地址。

## The Linux Command Line (Linux 命令行)
The command line, also known as the terminal or shell, is a text-based interface for interacting with the Linux system.
命令行，也称为终端或 shell，是一个基于文本的与 Linux 系统交互的界面。
You type commands, and the system executes them.
你输入命令，系统执行它们。

*   **Prompt (提示符):** When you open a terminal, you'll see a prompt, often like `username@hostname:~$` or `[username@hostname ~]$`.
    **提示符 (Prompt):** 当你打开终端时，你会看到一个提示符，通常类似于 `username@hostname:~$` 或 `[username@hostname ~]$`。
    *   `username`: Your current username.
        `username`: 你当前的用户名。
    *   `hostname`: The name of the computer you are logged into.
        `hostname`: 你登录的计算机的名称。
    *   `~`: Often indicates your home directory.
        `~`: 通常表示你的主目录。
    *   `$`: Usually indicates a normal user prompt (a `#` often indicates a root/administrator prompt).
        `$`: 通常表示普通用户提示符 (`#` 通常表示 root/管理员提示符)。
*   **Case Sensitivity (区分大小写):** Linux commands and filenames are case-sensitive. `MyFile.txt` is different from `myfile.txt`.
    **区分大小写 (Case Sensitivity):** Linux 命令和文件名是区分大小写的。`MyFile.txt` 与 `myfile.txt` 是不同的。

## Fundamental Commands (基本命令)

Here are some of the most common commands you'll use.
以下是一些你将会最常使用的命令。

---
### `ls`
*   Purpose: List directory contents.
    用途: 列出目录内容。
*   Examples (示例):
    *   List files and directories in the current location:
        列出当前位置的文件和目录：
        ```bash
        ls
        ```
        Example Output (示例输出):
        ```
        Desktop  Documents  Downloads  Music  Pictures  my_script.sh
        ```
    *   List in long format (shows permissions, owner, size, modification date):
        以长格式列出 (显示权限、所有者、大小、修改日期)：
        ```bash
        ls -l
        ```
        Example Output (示例输出):
        ```
        total 20
        drwxr-xr-x 2 user group 4096 May 20 10:00 Desktop
        drwxr-xr-x 2 user group 4096 May 20 10:00 Documents
        -rw-r--r-- 1 user group  123 May 20 10:05 my_script.sh
        ```
    *   List all files, including hidden files (those starting with a `.`)
        列出所有文件，包括隐藏文件 (以 `.` 开头的文件)：
        ```bash
        ls -a
        ```
        Example Output (示例输出):
        ```
        .    ..   .bash_history   .bashrc   Desktop   my_script.sh
        ```

---
### `cd`
*   Purpose: Change directory.
    用途: 切换目录。
*   Examples (示例):
    *   Navigate into a directory named `my_folder`:
        进入名为 `my_folder` 的目录：
        ```bash
        cd my_folder
        ```
    *   Go up to the parent directory (one level up):
        返回到上一级目录：
        ```bash
        cd ..
        ```
    *   Go to your home directory:
        进入你的主目录：
        ```bash
        cd ~
        ```
        or (或)
        ```bash
        cd
        ```
    *   Go to the root directory (topmost directory):
        进入根目录 (最顶层目录)：
        ```bash
        cd /
        ```

---
### `pwd`
*   Purpose: Print working directory (shows your current location).
    用途: 显示当前工作目录 (显示你当前所在的完整路径)。
*   Example (示例):
    ```bash
    pwd
    ```
    Example Output (示例输出):
    ```
    /home/username/my_project
    ```

---
### `mkdir`
*   Purpose: Make directory (create a new folder).
    用途: 创建目录 (创建一个新文件夹)。
*   Example (示例):
    *   Create a directory named `new_analysis_data`:
        创建一个名为 `new_analysis_data` 的目录：
        ```bash
        mkdir new_analysis_data
        ```

---
### `rmdir`
*   Purpose: Remove an *empty* directory.
    用途: 删除一个*空*目录。
*   Example (示例):
    *   Remove the empty directory `old_folder`:
        删除名为 `old_folder` 的空目录：
        ```bash
        rmdir old_folder
        ```
    *   If the directory is not empty, `rmdir` will give an error.
        如果目录非空，`rmdir` 会报错。

---
### `rm`
*   Purpose: Remove files or directories. **Use with caution!**
    用途: 删除文件或目录。**请谨慎使用！**
*   Examples (示例):
    *   Remove a file named `temp_data.txt`:
        删除名为 `temp_data.txt` 的文件：
        ```bash
        rm temp_data.txt
        ```
    *   Remove a directory and all its contents recursively (use with extreme caution!):
        递归删除一个目录及其所有内容 (请极度谨慎使用！)：
        ```bash
        rm -r logs_backup
        ```
    *   Prompt before every removal (interactive mode):
        在每次删除前提示 (交互模式)：
        ```bash
        rm -i old_file.txt
        ```

---
### `cp`
*   Purpose: Copy files or directories.
    用途: 复制文件或目录。
*   Examples (示例):
    *   Copy `source.txt` to `destination.txt` (creates `destination.txt`):
        将 `source.txt` 复制为 `destination.txt` (创建 `destination.txt`)：
        ```bash
        cp source.txt destination.txt
        ```
    *   Copy `input_data.csv` into the `results` directory (results directory must exist):
        将 `input_data.csv` 复制到 `results` 目录中 (`results` 目录必须已存在)：
        ```bash
        cp input_data.csv results/
        ```
    *   Copy a directory `raw_data` and its contents to `processed_data` (recursively):
        将目录 `raw_data` 及其内容复制到 `processed_data` (递归地)：
        ```bash
        cp -r raw_data processed_data
        ```

---
### `mv`
*   Purpose: Move or rename files or directories.
    用途: 移动或重命名文件或目录。
*   Examples (示例):
    *   Rename `old_filename.txt` to `new_filename.txt`:
        将 `old_filename.txt` 重命名为 `new_filename.txt`：
        ```bash
        mv old_filename.txt new_filename.txt
        ```
    *   Move `analysis_script.py` into the `scripts` directory:
        将 `analysis_script.py` 移动到 `scripts` 目录中：
        ```bash
        mv analysis_script.py scripts/
        ```
    *   Move all files from `temp_files` directory to `archive` directory (assuming `archive` exists):
        将 `temp_files` 目录下的所有文件移动到 `archive` 目录 (假设 `archive` 已存在)：
        ```bash
        mv temp_files/* archive/
        ```

---
### `cat`
*   Purpose: Concatenate and display file content. Mostly used to quickly view entire content of small files.
    用途: 连接并显示文件内容。主要用于快速查看小文件的全部内容。
*   Example (示例):
    ```bash
    cat my_notes.txt
    ```

---
### `less` (or `more`)
*   Purpose: View file content paginated (one screen at a time). `less` is generally more versatile than `more`.
    用途: 分页查看文件内容 (一次一屏)。`less` 通常比 `more` 功能更强大。
*   Example (示例):
    ```bash
    less large_logfile.log
    ```
*   Basic `less` navigation (基本 `less` 导航):
    *   `Spacebar`: Next page. (空格键：下一页。)
    *   `b`: Previous page. (b键：上一页。)
    *   `/search_term`: Search for `search_term`. (输入 `/搜索词`：搜索该词。)
    *   `q`: Quit `less`. (q键：退出 `less`。)

---
### `head`
*   Purpose: Display the first few lines of a file.
    用途: 显示文件的前几行。
*   Examples (示例):
    *   Display the first 10 lines (default):
        显示文件的前10行 (默认)：
        ```bash
        head data.csv
        ```
    *   Display the first 5 lines:
        显示文件的前5行：
        ```bash
        head -n 5 data.csv
        ```

---
### `tail`
*   Purpose: Display the last few lines of a file.
    用途: 显示文件的后几行。
*   Examples (示例):
    *   Display the last 10 lines (default):
        显示文件的后10行 (默认)：
        ```bash
        tail error_log.txt
        ```
    *   Display the last 20 lines:
        显示文件的后20行：
        ```bash
        tail -n 20 error_log.txt
        ```
    *   Follow a file (display new lines as they are added, useful for live logs):
        实时跟踪文件内容 (当文件有新行添加时立即显示，对查看实时日志很有用)：
        ```bash
        tail -f application.log
        ```
        (Press `Ctrl+C` to stop following - 按 `Ctrl+C` 停止跟踪。)

---
### `grep`
*   Purpose: Search text using patterns (strings or regular expressions).
    用途: 使用模式 (字符串或正则表达式) 搜索文本。
*   Examples (示例):
    *   Search for the word "Error" in `system.log`:
        在 `system.log` 文件中搜索单词 "Error"：
        ```bash
        grep "Error" system.log
        ```
    *   Search for "warning" (case-insensitive) in `output.txt`:
        在 `output.txt` 文件中不区分大小写地搜索 "warning"：
        ```bash
        grep -i "warning" output.txt
        ```
    *   Count the number of lines containing "simulation complete":
        统计包含 "simulation complete" 的行数：
        ```bash
        grep -c "simulation complete" results.dat
        ```

---
### `find`
*   Purpose: Search for files in a directory hierarchy.
    用途: 在目录结构中搜索文件。
*   Examples (示例):
    *   Find all files named `results.txt` starting from the current directory (`.`):
        从当前目录 (`.`) 开始查找所有名为 `results.txt` 的文件：
        ```bash
        find . -name "results.txt"
        ```
    *   Find all files ending with `.py` in your home directory (`~`):
        在你的主目录 (`~`) 中查找所有以 `.py` 结尾的文件：
        ```bash
        find ~ -name "*.py"
        ```
    *   Find directories named `data` starting from current directory:
        从当前目录开始查找名为 `data` 的目录：
        ```bash
        find . -type d -name "data"
        ```

---
## File Permissions (文件权限) (Basic - 基础)
Linux uses a permission system to control who can read, write, or execute files.
Linux 使用权限系统来控制谁可以读取、写入或执行文件。
When you run `ls -l`, the first part of the output (e.g., `-rw-r--r--` or `drwxr-xr-x`) shows permissions.
当你运行 `ls -l` 时，输出的第一部分 (例如 `-rw-r--r--` 或 `drwxr-xr-x`) 显示了权限。

*   `r`: Read permission (读取权限)
*   `w`: Write permission (写入权限)
*   `x`: Execute permission (for files, it means they can be run as a program; for directories, it means you can enter them)
    `x`: 执行权限 (对于文件，表示可以作为程序运行；对于目录，表示可以进入该目录)

The permissions are typically shown for three categories: User (owner), Group, and Others.
权限通常针对三类用户显示：用户 (所有者)、用户组、其他用户。
`drwxr-xr-x` means:
`drwxr-xr-x` 表示：
  `d`: It's a directory. (这是一个目录。)
  `rwx`: User (owner) has read, write, and execute permissions. (用户 (所有者) 具有读、写、执行权限。)
  `r-x`: Group has read and execute permissions (but not write). (用户组具有读和执行权限 (但没有写权限)。)
  `r-x`: Others have read and execute permissions (but not write). (其他用户具有读和执行权限 (但没有写权限)。)

### `chmod`
*   Purpose: Change file permissions.
    用途: 更改文件权限。
*   Example (示例):
    *   Make a script named `my_simulation_script.sh` executable for the user (owner):
        使名为 `my_simulation_script.sh` 的脚本对用户 (所有者) 可执行：
        ```bash
        chmod u+x my_simulation_script.sh
        ```
        (`u` for user, `+` to add permission, `x` for execute - `u` 代表用户，`+` 代表添加权限，`x` 代表执行。)
    *   This is a very basic introduction. `chmod` can be more complex.
        这是一个非常基础的介绍。`chmod` 的用法可以更复杂。

---
## Input/Output Redirection (输入/输出重定向) (Simple - 简单示例)
You can redirect the output of commands or use the output of one command as input for another.
你可以重定向命令的输出，或将一个命令的输出用作另一个命令的输入。

*   **`>` (Redirect output - 重定向输出):** Sends the output of a command to a file, overwriting the file if it exists.
    **`>` (Redirect output - 重定向输出):** 将命令的输出发送到一个文件，如果文件已存在则覆盖它。
    Example (示例): Save the list of files to `file_listing.txt`:
    将文件列表保存到 `file_listing.txt`：
    ```bash
    ls -l > file_listing.txt
    ```

*   **`>>` (Append output - 追加输出):** Sends the output of a command to a file, appending to the end if the file exists.
    **`>>` (Append output - 追加输出):** 将命令的输出发送到一个文件，如果文件已存在则追加到文件末尾。
    Example (示例): Add a new message to `my_log.txt`:
    向 `my_log.txt` 添加一条新消息：
    ```bash
    echo "Simulation step 5 completed." >> my_log.txt
    ```

*   **`|` (Pipe - 管道):** Sends the output of one command as input to another command.
    **`|` (Pipe - 管道):** 将一个命令的输出作为另一个命令的输入发送。
    Example (示例): List all files, then find only those containing ".txt":
    列出所有文件，然后只找出其中包含 ".txt" 的行：
    ```bash
    ls -l | grep ".txt"
    ```

---
## Basic Shell Scripting (基础 Shell 脚本) (Very Simple Examples - 非常简单的示例)
A shell script is a text file containing a series of commands that are executed sequentially.
Shell 脚本是一个包含一系列命令的文本文件，这些命令会按顺序执行。
It's a way to automate tasks.
这是一种自动化任务的方法。

*   **Shebang (释伴):** The first line of a script often tells the system which interpreter to use. For bash scripts (common in Linux):
    **Shebang (释伴):** 脚本的第一行通常告诉系统使用哪个解释器。对于 bash 脚本 (在 Linux 中很常见)：
    `#!/bin/bash`

*   **Making a script executable (使脚本可执行):**
    You need to give it execute permission first.
    你首先需要给它执行权限。
    ```bash
    chmod u+x script_name.sh
    ```

*   **Running a script (运行脚本):**
    If the script is in your current directory:
    如果脚本在你的当前目录中：
    ```bash
    ./script_name.sh
    ```

*   **Example 1: Create a directory and list its (empty) contents (示例1：创建一个目录并列出其 (空) 内容)**
    File name (in examples/ directory) (文件名 (在 examples/ 目录中)): `examples/make_and_show.sh`
    ```bash
    #!/bin/bash
    echo "Creating a directory named 'my_test_dir'..."
    # 创建一个名为 'my_test_dir' 的目录...
    mkdir my_test_dir
    echo "Directory created. Navigating into it..."
    # 目录已创建。正在进入该目录...
    cd my_test_dir
    echo "Current directory:"
    # 当前目录：
    pwd
    echo "Contents of 'my_test_dir':"
    # 'my_test_dir' 的内容：
    ls
    echo "Script finished."
    # 脚本结束。
    ```
    To run (from the `04_Linux_Basics` directory) (从 `04_Linux_Basics` 目录运行):
    ```bash
    chmod u+x examples/make_and_show.sh
    ./examples/make_and_show.sh
    ```

*   **Example 2: Simple backup script (示例2：简单的备份脚本)**
    File name (in examples/ directory) (文件名 (在 examples/ 目录中)): `examples/simple_backup.sh`
    ```bash
    #!/bin/bash
    echo "Creating a backup of important_data.txt..."
    # 正在创建 important_data.txt 的备份...

    # Create a dummy important_data.txt if it doesn't exist, so the script is runnable
    # 如果 important_data.txt 不存在，则创建一个虚拟文件，以便脚本可以运行
    if [ ! -f important_data.txt ]; then
        echo "Creating dummy important_data.txt for demonstration."
        echo "This is important data." > important_data.txt
    fi

    cp important_data.txt important_data_backup.txt
    echo "Backup created as important_data_backup.txt"
    # 备份已创建为 important_data_backup.txt
    ls -l important_data.txt important_data_backup.txt
    echo "Backup script finished."
    # 备份脚本结束。
    ```
    To run (from the `04_Linux_Basics` directory) (从 `04_Linux_Basics` 目录运行):
    ```bash
    chmod u+x examples/simple_backup.sh
    ./examples/simple_backup.sh
    ```

This is just a starting point. Linux offers a vast range of commands and capabilities!
这仅仅是一个开始。Linux 提供了非常广泛的命令和功能！
