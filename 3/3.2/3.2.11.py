def donuts(n):
    if n <= 9:
        print("Всего пончиков: " + str(n))
    elif n > 9:
        print("Всего пончиков: много")


n = int(input())
donuts(n)
