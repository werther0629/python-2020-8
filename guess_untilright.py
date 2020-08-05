import random

ans = random.randint(1,20)

while True:
    guess = input('請在1~20間猜一個數字: ')
    guess = int(guess)

    if guess>20 or guess<0:
        print('輸入錯誤，請重新輸入!!!')
    else:
        if guess > ans:
            print('小一點')
        elif guess < ans:
            print('大一點')
        else:
            print('Bingo!!!')
            break
