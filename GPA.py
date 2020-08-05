score = input('請輸入你的分數:')
score = int(score)

if score >= 0 and score <= 100:
    print('\n你的分數等級是')
    if score >= 90:
        print('A')
    elif score >= 80:
        print('B')
    elif score >= 70:
        print('C')
    elif score >= 60:
        print('D')
    else:
        print('F')
else:
    print('請輸入0~100的分數!!')
