tasks = []

while True:
    print("\n===== Todo List =====")
    print("1. 添加任务")
    print("2. 查看任务")
    print("3. 标记完成")
    print("4. 删除任务")
    print("5. 退出")

    choice = input("请输入你的选择：")

    if choice == "1":
        title = input("请输入任务名称：")
        task = {"title": title, "done": False}
        tasks.append(task)
        print("任务添加成功！")
    elif choice == "2":
        if len(tasks) == 0:
            print("当前没有任务。")
        else:
            for index, task in enumerate(tasks, start=1):
                status = "已完成" if task["done"] else "未完成"
                print(f"{index}. {task['title']} - {status}")

    elif choice == "3":
        if len(tasks) == 0:
            print("当前没有任务。")
        else:
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task['title']}")

            task_num = int(input("请输入要标记完成的任务编号："))

            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1]["done"] = True
                print("任务已标记完成！")
            else:
                print("无效的任务编号。")


    elif choice == "4":
        if len(tasks) == 0:
            print("当前没有任务。")
        else:
            for index, task in enumerate(tasks, start=1):
                status = "已完成" if task["done"] else "未完成"
                print(f"{index}. {task['title']} - {status}")

            task_num = int(input("请输入要删除的任务编号："))

            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"任务「{removed_task['title']}」已删除！")
            else:
                print("无效的任务编号。")
    
    
    elif choice == "5":
        print("程序已退出")
        break

    else:
        print("功能暂未实现，请重新选择。")
    