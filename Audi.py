import turtle as t

t.pensize(5)
t.Screen().bgcolor("black")
t.pencolor("#fff")
t.speed(10)

for i in range(4):
    t.penup()
    t.goto(i*70, 0)
    t.pendown()
    t.circle(50)
    t.color("white")

t.penup()
t.goto(77, -40)
t.pendown()
t.hideturtle()

t.done()
