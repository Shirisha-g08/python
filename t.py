'''import turtle
import colorsys
s=turtle.Turtle()
turtle.bgcolor("black")
h=0.0
s.color("blue")
s.shape("turtle")
s.speed(0)
for i in range(200,0,-1):
    s.color(colorsys.hsv_to_rgb(h,1,1))
    s.circle(i)
    s.right(4)
    h+=0.02
turtle.mainloop()'''


import turtle
s=turtle.Turtle()
turtle.bgcolor("light blue")
s.hideturtle()
s.fillcolor("yellow")
s.penup()
s.goto(0,50)
s.pendown()
for i in range(10):
    s.forward(100)
    s.goto(0,50)
    s.right(36)
s.penup()
s.goto(0,0)
s.pendown()
s.begin_fill()
s.circle(50)
s.end_fill()
turtle.mainloop()

