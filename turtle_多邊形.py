import turtle 

polygon = turtle.Turtle()

num_sides = int(input('要畫幾邊形(4-10)?'))
side_length = 70
angle = 360.0 / num_sides 

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
    
turtle.done()
