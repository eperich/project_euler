import turtle

side_length = 450
level_number = 3
i = 1


def snowflake(a_turtle, side, level):
    if level == 0:
        a_turtle.forward(side)
        return
    side /= 3.0
    snowflake(a_turtle, side, level-1)
    a_turtle.left(60)
    snowflake(a_turtle, side, level-1)
    a_turtle.right(120)
    snowflake(a_turtle, side, level-1)
    a_turtle.left(60)
    snowflake(a_turtle, side, level-1)


t = turtle.Turtle()
t.speed(50)
t.hideturtle()
t.penup()
t.setpos(-200, -100)
t.pendown()
t.seth(60)
for i in range(3):
    snowflake(t, side_length, level_number)
    t.right(120)

s = turtle.getscreen()
s.mainloop()

