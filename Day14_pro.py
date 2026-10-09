class Student:
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def introduce(self):
        print(f"我是{self.name},成绩是{self.score}分。")
    def improve_score(self,points):
        if points>0:
            self.score+=points
            print("加分成功")
        else:
            print("加分必须大于0！")

student1=Student("Alice",80)
student2=Student("Bob",70)
student1.improve_score(10)
student2.improve_score(20)
student1.introduce()
student2.introduce()