import random
import time

students = ["Alice", "Bob", "Tom", "Lucy", "Jack"]

selected = random.sample(students, 3)

print("即将公布点名结果：")
time.sleep(2)
for student in selected:
    print(student)