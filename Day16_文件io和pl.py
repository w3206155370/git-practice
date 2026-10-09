
from pathlib import Path

# 1. 获取日志文件路径
path = Path("app.log")

# 2. 检查文件是否存在
if not path.exists():
    print("日志文件不存在！")
else:
    # 3. 读取文件的所有行
    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # 4. 统计总行数
    total_lines = len(lines)

    # 5. 统计 ERROR 行数
    error_count = 0

    # 6. 记录最长的一行
    longest_line = ""

    for line in lines:
        # 去掉末尾的换行符
        line = line.rstrip("\n")

        # 统计包含 ERROR 的行
        if "ERROR" in line:
            error_count += 1

        # 更新最长行
        if len(line) > len(longest_line):
            longest_line = line

    # 7. 输出统计结果
    print("日志文件：", path.name)
    print("总行数：", total_lines)
    print("ERROR 行数：", error_count)
    print("最长的一行：", longest_line)
    print("最长行字符数：", len(longest_line))