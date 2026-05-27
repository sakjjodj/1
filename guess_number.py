import random

number = random.randint(1, 100)
print("我想了一个1到100之间的数字，你来猜吧！")

while True:
    guess = input("请输入你的猜测（或输入q退出）：")
    if guess.lower() == 'q':
        print("游戏结束，再见！")
        break
    try:
        guess = int(guess)
    except:
        print("请输入有效的数字。")
        continue
    if guess < number:
        print("小了！")
    elif guess > number:
        print("大了！")
    else:
        print("恭喜你，猜对了！")
        break
