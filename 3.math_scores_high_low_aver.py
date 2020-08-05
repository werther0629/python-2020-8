scores = []
names = []
total = 0
highest = 0
lowest = 100

# How many people taking the exam?
n = input('班上有幾位同學?')
n = int(n)

# create the score list
for i in range(n):
    score = input("輸入同學數學成績:")
    score = int(score)
    scores.append(score)
    
for i in range(n):
    if scores[i] > highest:
        highest = scores[i]
    if scores[i] < lowest:
        lowest = scores[i]
    total = scores[i] + total
average = total / n

print("平均分:",average)            
print("最高分:",highest)
print("最低分:",lowest)

