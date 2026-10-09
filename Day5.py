scores = [85, 60, 92, 45, 78, 92]

# 平均分
average = sum(scores)/len(scores)

# 最高分
highest = max(scores)

# 不及格人数
fail_count = 0

for score in scores:
    if score < 60:
        fail_count+=1

print("平均分：", average)
print("最高分：", highest)
print("不及格人数：", fail_count)