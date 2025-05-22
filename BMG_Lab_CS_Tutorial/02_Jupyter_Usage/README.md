# 02 - Jupyter Notebook/Lab: Interactive Coding (Jupyter Notebook/Lab: 交互式编程)

## What are Jupyter Notebooks/JupyterLab? (什么是 Jupyter Notebook/JupyterLab?)
Jupyter Notebook and JupyterLab are interactive, web-based computing environments.
Jupyter Notebook 和 JupyterLab 是交互式的、基于 Web 的计算环境。
They allow you to combine live code, equations, visualizations, and narrative text (Markdown).
它们允许你将实时代码、方程式、可视化结果和叙述性文本 (Markdown) 结合起来。
This makes them excellent tools for data analysis, learning to code, and scientific research.
这使得它们成为数据分析、学习编码和科学研究的绝佳工具。

*   **Jupyter Notebook (经典 Jupyter Notebook):** The original application for creating single documents (`.ipynb` files) with mixed content.
    **Jupyter Notebook (经典 Jupyter Notebook):** 用于创建包含混合内容的单个文档 (`.ipynb` 文件) 的原始应用程序。
*   **JupyterLab (JupyterLab):** A newer, more integrated environment. It allows working with multiple notebooks, text editors, and even terminals in a single interface. We recommend starting with JupyterLab.
    **JupyterLab (JupyterLab):** 一个更新、更集成的环境。它允许在单个界面中处理多个笔记本、文本编辑器甚至终端。我们建议从 JupyterLab 开始。

## Launching JupyterLab/Notebook (启动 JupyterLab/Notebook)

### Via Anaconda Navigator (通过 Anaconda Navigator)
1.  Open Anaconda Navigator.
    打开 Anaconda Navigator。
2.  Find the JupyterLab or Jupyter Notebook icon on the dashboard.
    在主界面上找到 JupyterLab 或 Jupyter Notebook 的图标。
3.  Click the **Launch** button. This will open in your web browser.
    点击 **Launch** 按钮。这将在你的网络浏览器中打开。

### Via Command Line (通过命令行)
1.  **Activate your Conda environment (激活你的 Conda 环境):**
    Open Anaconda Prompt (Windows) or Terminal (macOS/Linux).
    打开 Anaconda Prompt (Windows) 或终端 (macOS/Linux)。
    If you have a specific environment (e.g., `myenv`), activate it:
    如果你有特定的环境 (例如 `myenv`)，请激活它：
    ```bash
    conda activate myenv
    ```
2.  **Launch JupyterLab (启动 JupyterLab):**
    ```bash
    jupyter lab
    ```
3.  **Launch Classic Jupyter Notebook (启动经典 Jupyter Notebook):**
    ```bash
    jupyter notebook
    ```
    The terminal window used for launching must stay open.
    用于启动的终端窗口必须保持打开状态。

## Interface Overview (界面概览 - 简要)

### JupyterLab
*   **Left Sidebar (左侧边栏):** File browser, running kernels list, command palette.
    **左侧边栏 (Left Sidebar):** 文件浏览器、正在运行的内核列表、命令面板。
*   **Main Work Area (主工作区):** Arrange multiple documents (notebooks, text files) as tabs or split views.
    **主工作区 (Main Work Area):** 将多个文档 (笔记本、文本文件) 排列为标签页或分割视图。

### Classic Jupyter Notebook
*   **Dashboard (仪表盘):** File browser to navigate and create new notebooks.
    **仪表盘 (Dashboard):** 文件浏览器，用于导航目录和创建新笔记本。

## Working with Notebooks (.ipynb files) (使用笔记本文件)

### Creating a notebook (创建新笔记本)
*   **JupyterLab:** Click "+" in the "Launcher" or `File > New > Notebook`. Select a kernel (e.g., `Python 3`).
    **JupyterLab:** 在“启动器”中点击“+”图标，或转到 `文件 > 新建 > Notebook`。选择一个内核 (例如 `Python 3`)。
*   **Classic Notebook:** Click `New` (top right on dashboard) and select `Python 3` under "Notebooks".
    **经典 Notebook:** 在仪表盘右上角点击 `New`，然后在“Notebooks”下选择 `Python 3`。

### Cells (单元格)
Notebooks are made of cells.
笔记本由单元格组成。
*   **Code Cells (代码单元格):** Write and execute code (e.g., Python). Output appears below.
    **代码单元格 (Code Cells):** 编写和执行代码 (例如 Python)。输出会显示在单元格下方。
*   **Markdown Cells (Markdown 单元格):** Write text with Markdown for explanations, notes, images.
    **Markdown 单元格 (Markdown Cells):** 使用 Markdown 编写文本，用于解释、笔记、插入图片等。

### Running cells (运行单元格)
*   `Shift + Enter`: Run the current cell, select/create cell below.
    `Shift + Enter`: 运行当前单元格，并选择/创建下方单元格。
*   `Ctrl + Enter` (Windows/Linux) / `Cmd + Enter` (macOS): Run selected cell(s), keep current cell selected.
    `Ctrl + Enter` (Windows/Linux) / `Cmd + Enter` (macOS): 运行选中的单元格，并保持当前单元格被选中。
*   **Toolbar "Run" button (工具栏“运行”按钮):** Executes the selected cell.
    **工具栏“运行”按钮 (Toolbar "Run" button):** 执行当前选中的单元格。

### Cell Modes (单元格模式)
Cells have two modes, indicated by the left border color.
单元格有两种模式，通过左边框颜色指示。
*   **Command Mode (命令模式):** Blue border. Press `Esc` to enter. For notebook-level operations.
    **命令模式 (Command Mode):** 蓝色边框。按 `Esc` 进入。用于笔记本级别的操作。
*   **Edit Mode (编辑模式):** Green border. Press `Enter` (on a selected cell) to enter. For typing code or text into the cell.
    **编辑模式 (Edit Mode):** 绿色边框。按 `Enter` (在选中的单元格上) 进入。用于在单元格中输入代码或文本。

### Essential Keyboard Shortcuts (核心快捷键)
In Command Mode (蓝色边框):
在命令模式下 (蓝色边框):
*   `A`: Insert new cell **a**bove.
    `A`: 在当前单元格**上**方插入新单元格。
*   `B`: Insert new cell **b**elow.
    `B`: 在当前单元格**下**方插入新单元格。
*   `M`: Change cell to **M**arkdown.
    `M`: 将当前单元格更改为 Markdown。
*   `Y`: Change cell to code.
    `Y`: 将当前单元格更改为代码。
*   `D,D` (press `D` twice): Delete current cell.
    `D,D` (快速按两次 `D`): 删除当前单元格。
*   `Z`: Undo last cell deletion.
    `Z`: 撤销上次删除单元格的操作。
*   `C`: Copy current cell. (Advanced: use sparingly if new)
    `C`: 复制当前单元格。(高级：如果是新手，请谨慎使用)
*   `V`: Paste cell. (Advanced: use sparingly if new)
    `V`: 粘贴单元格。(高级：如果是新手，请谨慎使用)

### Saving (保存)
*   `Ctrl + S` (Windows/Linux) or `Cmd + S` (macOS): Saves the notebook.
    `Ctrl + S` (Windows/Linux) 或 `Cmd + S` (macOS): 保存笔记本。
*   Or use `File > Save Notebook` from the menu.
    或者从菜单中使用 `文件 > 保存笔记本`。
*   Jupyter also auto-saves.
    Jupyter 也会自动保存。

### Kernels (内核)
*   **What is a kernel? (什么是内核?)** A kernel is a computational engine that runs the code in your notebook (e.g., an IPython kernel for Python code).
    **什么是内核? (What is a kernel?)** 内核是运行笔记本中代码的计算引擎 (例如，用于 Python 代码的 IPython 内核)。
*   **Interrupting/Restarting (中断/重启内核):**
    If code runs too long or gets stuck.
    如果代码运行时间过长或卡住。
    *   `Kernel > Interrupt Kernel`: Stops the current execution.
        `内核 > 中断内核`: 停止当前执行。
    *   `Kernel > Restart Kernel`: For a fresh start. Outputs can be cleared too.
        `内核 > 重启内核`: 用于重新开始。输出也可以被清除。

## Basic Markdown Syntax (基础 Markdown 语法)
Used in Markdown cells for rich text.
用于 Markdown 单元格以实现富文本。
*   **Headings (标题):** `## Heading 2`, `### Heading 3` (Use `#` for levels 1-6)
    **标题 (Headings):** `## 二级标题`, `### 三级标题` (使用 `#` 标记 1-6 级标题)
*   **Emphasis (强调):** `*italic*` (斜体), `**bold**` (粗体)
    **强调 (Emphasis):** `*斜体*`, `**粗体**`
*   **Lists (列表):**
    *   Unordered: `- Item` or `* Item`
        无序列表: `- 项目符号` 或 `* 项目符号`
    *   Ordered: `1. Item`
        有序列表: `1. 项目符号`
*   **Inline Code (行内代码):** `` `code` `` (e.g., `` `x = 10` ``)
    **行内代码 (Inline Code):** `` `代码` `` (例如 `` `x = 10` ``)
*   **Code Blocks (代码块):**
    ```markdown
    ```python
    print("Hello from a code block!")
    ```
    ```

## Exporting Notebooks (导出笔记本)
You can save your notebook in other formats.
你可以将笔记本保存为其他格式。
*   `File > Export Notebook As...` (JupyterLab) or `File > Download as` (Classic Notebook).
    `文件 > 将笔记本导出为...` (JupyterLab) 或 `文件 > 下载为` (经典 Notebook)。
*   **Common formats (常用格式):**
    *   **HTML:** For sharing a static, viewable version.
        **HTML:** 用于分享可在浏览器中查看的静态版本。
    *   **Python script (.py):** Exports only the code cells.
        **Python 脚本 (.py):** 仅导出代码单元格。
    *   **PDF:** For printing. May require extra software (LaTeX). (Advanced)
        **PDF:** 用于打印。可能需要额外软件 (LaTeX)。(高级)

## Tips for Effective Use (使用技巧)
*   **Document Your Work (记录你的工作):** Use Markdown cells to explain your code and findings.
    **记录你的工作 (Document Your Work):** 使用 Markdown 单元格来解释你的代码和发现。
*   **Keep Notebooks Focused (保持笔记本的专注性):** Break large tasks into smaller notebooks.
    **保持笔记本的专注性 (Keep Notebooks Focused):** 将大型任务分解成更小的笔记本。
*   **Restart and Run All (重启并全部运行):** Before finishing, always do `Kernel > Restart Kernel and Run All Cells...` to ensure everything runs correctly from a clean state.
    **重启并全部运行 (Restart and Run All):** 在完成之前，务必执行 `内核 > 重启内核并运行所有单元格...` 以确保所有内容在干净的状态下从头到尾正确运行。
*   **Name Notebooks Clearly (清晰命名笔记本):** Use descriptive names for your `.ipynb` files.
    **清晰命名笔记本 (Name Notebooks Clearly):** 为你的 `.ipynb` 文件使用描述性的名称。

Jupyter is a powerful tool. Practice these basics to become comfortable!
Jupyter 是一个强大的工具。练习这些基础知识以变得熟练！
