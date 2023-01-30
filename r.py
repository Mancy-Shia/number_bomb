import random

r = random.randint(1, 100)
while True:
    guess = input()
    guess = int(guess)
    if guess == r:
        print("終於猜對了")
        break
    elif guess > r:
        print("太大")
    elif guess < r:
        print('太小')

