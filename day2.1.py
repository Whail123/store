money=100
import random
num=random.randint(0,100)
print(num)
while money > 0:
        a=input("请输入一个数字")
        a=int(a)
        money=money-10
        if   a > num:
            print("输入数字太大")
        elif a < num:
            print("输入数字太小")
        else:
            print("恭喜你猜对了")
            break
print("游戏结束，剩余资金为",money)








