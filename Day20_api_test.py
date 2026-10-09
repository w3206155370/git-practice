import requests

url = "https://jsonplaceholder.typicode.com/todos/1"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()

    print("任务标题：", data["title"])

    if data["completed"]:
        print("任务状态：已完成")
    else:
        print("任务状态：尚未完成，需要继续处理")

except requests.exceptions.Timeout:
    print("请求超时，请检查网络后重试。")

except requests.exceptions.HTTPError as e:
    print(f"HTTP 状态错误：{e}")

except requests.exceptions.RequestException as e:
    print(f"请求失败：{e}")