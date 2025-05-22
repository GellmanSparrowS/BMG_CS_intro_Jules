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
