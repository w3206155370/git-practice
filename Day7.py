students = [
    {"name": "Tom", "score": 85},
    {"name": "Jack", "score": 92},
    {"name": "Lucy", "score": 55},
    {"name": "Bob", "score": 76},
    {"name": "Alice", "score": 68}
]


for student in students:
    if student["name"]=="Jack":
        print(f"Jack的成绩是{student['score']}")
    if student["name"]=="Lucy":
        student['score']=70
students.append({"name":"David", "score":88})
scores=[]
for s in students:
    scores.append(s["score"])
average=sum(scores)/len(students)
print(average)

fail_student=[]

for student in students:
    if student["score"]<60:
        fail_student.append(student)
print(fail_student)


