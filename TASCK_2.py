import turtle

# створення вікна для малювання
window = turtle.Screen()

# створення першого кола
circle1 = turtle.Turtle()
circle1.penup()
circle1.goto(-50, 0)
circle1.pendown()
circle1.circle(50)

# створення другого кола, що торкається першого кола
circle2 = turtle.Turtle()
circle2.penup()
circle2.goto(50, 0)
circle2.pendown()
circle2.circle(50)

# створення третього кола, яке перетинає перше коло
circle3 = turtle.Turtle()
circle3.penup()
circle3.goto(-100, -100)
circle3.pendown()
circle3.circle(50)

# створення четвертого кола, яке перетинає третє коло
circle4 = turtle.Turtle()
circle4.penup()
circle4.goto(-50, -100)
circle4.pendown()
circle4.circle(50)

# закриття вікна після натискання клавіші
window.exitonclick()