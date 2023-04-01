import turtle

# Намалюємо рівносторонній трикутник з чорними лініями
turtle.pencolor("black")
for i in range(3):
    turtle.forward(100)
    turtle.left(120)

# Намалюємо жовтий рівносторонній трикутник
turtle.fillcolor("yellow")
turtle.begin_fill()
for i in range(3):
    turtle.forward(100)
    turtle.left(120)
turtle.end_fill()

# Намалюємо зафарбований червоний рівносторонній трикутник
turtle.pencolor("red")
turtle.fillcolor("red")
turtle.begin_fill()
for i in range(3):
    turtle.forward(100)
    turtle.left(120)
turtle.end_fill()


turtle.done()





