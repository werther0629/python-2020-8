a = int(input('請問要有幾層'))

if a%2==1:
    for i in range(1,a+1,2):
        time_up = int((a-i)/2)
        print(' '*time_up,'*'*i,' '*time_up)
    for j in range(a-2,0,-2):
        time_down = int((a-j)/2)
        print(' '*time_down,'*'*j,' '*time_down)

b = input()




