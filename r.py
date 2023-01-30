import random
start = input("請輸入下界")
end = input("輸入上界")
start = int(start)
end = int(end)
r = random.randint(start, end)
cout = 0
while True:
    guess = input()
    guess = int(guess)
    cout += 1
    if guess == r:
        print("終於猜對了")
        print("這是第", cout, "次")
        break
    elif guess > r:
        print("太大")
    elif guess < r:
        print('太小')
    print("這是第", cout, "次")


