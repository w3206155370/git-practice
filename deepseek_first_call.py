import os

from dotenv import load_dotenv
from openai import OpenAI

# 读取 .env 文件
load_dotenv()

# 获取 API Key
api_key = os.getenv("DEEPSEEK_API_KEY")

if not api_key:
    raise ValueError("没有读取到 DeepSeek API Key，请检查 .env 文件。")

# 创建客户端
client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com",
)

# 向模型发送一条消息
response = client.chat.completions.create(
    model="deepseek-flash",
    messages=[
        {
            "role": "system",
            "content": "你是一名耐心的 AI 学习助教，请用简洁的中文回答。",
        },
        {
            "role": "user",
            "content": "请用一句话解释什么是大语言模型。",
        },
    ],
)

# 获取并打印模型回复
reply = response.choices[0].message.content

print("DeepSeek 的回答：")
print(reply)