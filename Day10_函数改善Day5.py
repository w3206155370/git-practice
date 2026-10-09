def calculate_average(scores):
    return sum(scores)/len(scores)
    


def get_level(score):
    if score >= 90:
        return "优秀"
    elif score >=80:
        return "良好"
    elif score >= 60:
        return "及格"
    else:
        return "不及格"

scores = [85, 92, 55, 78, 100]

average = calculate_average(scores)
print(f"平均分：{average}")

for score in scores:
    level = get_level(score)
    print(f"{score}分：{level}")
