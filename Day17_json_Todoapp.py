import json
from pathlib import Path

# 保存数据的文件路径
path = Path("todo.json")

# 如果文件存在，就读取旧数据
if path.exists():
    with open(path, "r", encoding="utf-8") as file:
        todos = json.load(file)
else:
    # 第一次运行时，创建空列表
    todos = []

print("当前待办事项：", todos)


# 添加一个新任务
new_task = input("请输入一个待办事项：")
todos.append(new_task)

# 把更新后的列表保存到 JSON 文件
with open(path, "w", encoding="utf-8") as file:
    json.dump(todos, file, ensure_ascii=False, indent=4)

print("保存成功！")
print("当前待办事项：", todos)