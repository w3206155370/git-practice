import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("DEEPSEEK_API_KEY")

if api_key:
    print("API Key 已成功读取")
else:
    print("没有读取到 API Key")