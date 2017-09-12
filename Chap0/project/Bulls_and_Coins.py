import random
from sys import exit

num = random.randint(0, 20)
print("开始猜数字啦")

for i in range(10):
    print("请输入数字~")
    x = int(input("> "))
    n = 9 - i

    if x > num:
        print("大了，再猜。你还有%d机会" % n)
    elif x < num:
        print("小了，再猜。你还有%d机会" % n)
    elif x == num:
        print("恭喜你猜对啦~~~")
        exit(0)

print("机会用光了下次再猜吧~")
