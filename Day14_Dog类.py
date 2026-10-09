class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name}今年{self.age}岁，汪汪！")
        
dog1 = Dog("旺财",3)
dog2 = Dog("小黑",5)

dog1.bark()
dog2.bark()