answer=10
guess=0
count=0
while guess != answer:
    guess = int(input("请输入数字："))
    if guess>answer:
        print("猜大了")
    elif guess<answer:
        print("猜小了")
    else:
        print("猜对了")
        break
    count+=1
    if count==3:
        print("游戏结束！")
        break
        
        
