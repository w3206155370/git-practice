tools = ["搜索工具", "计算器", "天气工具"]

print("当前 Agent 可使用的工具：")

for tool in tools:
    print(f"- {tool}")

tool = {
    "name": "weather",
    "description": "查询天气",
    "location": "Tokyo"
}

print(f"工具名称：{tool['name']}")
print(f"工具功能：{tool['description']}")
print(f"查询地点：{tool['location']}")
print({tool["name"]})