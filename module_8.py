import turtle

side_length = 450
level_number = 4
i = 1


def draw_first_side(a_turtle, side, level, vertex):
    if level == level_number:
        for n in range(3):
            a_turtle.forward(side)
            a_turtle.right(120)
            a_turtle.forward(side)
            a_turtle.left(60)
            n += 1
        a_turtle.forward(side)
        a_turtle.left(60)
        a_turtle.forward(side * 3)
        a_turtle.right(120)
        if a_turtle.towards(vertex) in [0, 120, 240]:
            a_turtle.right(180)
            draw_vertex(a_turtle, side_length / 3, 1)
        else:
            draw_first_side(a_turtle, side * 9, level - 2, vertex)
    else:
        a_turtle.forward(side / 3)
        a_turtle.left(60)
        draw_first_side(a_turtle, side / 3, level + 1, vertex)


def draw_vertex(a_turtle, side, level):
    a_turtle.forward(side)
    vertex = a_turtle.pos()
    a_turtle.right(120)
    draw_first_side(a_turtle, side * 3, level, vertex)


t = turtle.Turtle()
t.hideturtle()
t.penup()
t.setpos(-100, 100)
t.pendown()
t.seth(60)
draw_vertex(t, side_length / 3, i)

s = turtle.getscreen()
s.mainloop()

