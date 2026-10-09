import os

from dotenv import load_dotenv
from openai import OpenAI

# 读取环境变量
load_dotenv()

api_key = os.getenv("DEEPSEEK_API_KEY")

if not api_key:
    raise ValueError("未读取到 DeepSeek API Key，请检查 .env 文件。")

# 创建客户端
client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com",
)

# 初始化对话历史
messages = [
    {
        "role": "system",
        "content": "你是一名耐心的 AI 学习助教，请用简洁的中文回答。",
    }
]

print("欢迎使用 DeepSeek 聊天机器人！")
print("输入 exit 或 退出，即可结束对话。")

while True:
    user_input = input("\n你：").strip()

    # 检查是否退出
    if user_input.lower() in {"exit", "quit"} or user_input == "退出":
        print("聊天结束，再见！")
        break

    # 忽略空输入
    if not user_input:
        continue

    # 保存用户的问题
    messages.append({
        "role": "user",
        "content": user_input,
    })

    try:
        # 请求模型生成回答
        response = client.chat.completions.create(
            model="deepseek-flash",
            messages=messages,
        )

        reply = response.choices[0].message.content or ""

        print(f"\nDeepSeek：{reply}")

        # 保存模型的回答
        messages.append({
            "role": "assistant",
            "content": reply,
        })

    except Exception as e:
        # 请求失败时，移除未得到回答的用户消息
        messages.pop()
        print(f"请求失败：{e}")