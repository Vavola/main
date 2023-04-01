# Це мій старий поєкт,
# я його скинув вам щоб ви подивилися,
# або ж, я просто хотів похизуватися ¯\_(ツ)_/¯

#P.S Не питайте мене як цей код працює, я вже сам забув.



import turtle
import math

# створення вікна для малювання
window = turtle.Screen()

# створення сонця
sun = turtle.Turtle()
sun.shape('circle')
sun.color('yellow')

# створення планет
mercury = turtle.Turtle()
mercury.color('gray')
mercury.penup()
mercury.goto(50, 0)
mercury.pendown()
mercury.shape('circle')
mercury.shapesize(0.3)
mercury.penup()

venus = turtle.Turtle()
venus.color('orange')
venus.penup()
venus.goto(80, 0)
venus.pendown()
venus.shape('circle')
venus.shapesize(0.5)
venus.penup()

earth = turtle.Turtle()
earth.color('blue')
earth.penup()
earth.goto(120, 0)
earth.pendown()
earth.shape('circle')
earth.shapesize(0.6)
earth.penup()

mars = turtle.Turtle()
mars.color('red')
mars.penup()
mars.goto(170, 0)
mars.pendown()
mars.shape('circle')
mars.shapesize(0.4)
mars.penup()

jupiter = turtle.Turtle()
jupiter.color('orange')
jupiter.penup()
jupiter.goto(240, 0)
jupiter.pendown()
jupiter.shape('circle')
jupiter.shapesize(1.5)
jupiter.penup()

saturn = turtle.Turtle()
saturn.color('brown')
saturn.penup()
saturn.goto(340, 0)
saturn.pendown()
saturn.shape('circle')
saturn.shapesize(1.3)
saturn.penup()

# створення орбіт для планет
mercury_orbit = turtle.Turtle()
mercury_orbit.speed(0)
mercury_orbit.penup()
mercury_orbit.goto(0, -50)
mercury_orbit.pendown()
mercury_orbit.circle(50)
mercury_orbit.hideturtle()

venus_orbit = turtle.Turtle()
venus_orbit.speed(0)
venus_orbit.penup()
venus_orbit.goto(0, -80)
venus_orbit.pendown()
venus_orbit.circle(80)
venus_orbit.hideturtle()

earth_orbit = turtle.Turtle()
earth_orbit.speed(0)
earth_orbit.penup()
earth_orbit.goto(0, -120)
earth_orbit.pendown()
earth_orbit.circle(120)
earth_orbit.hideturtle()

mars_orbit = turtle.Turtle()
mars_orbit.speed(0)
mars_orbit.penup()
mars_orbit.goto(0, -170)
mars_orbit.pendown()
mars_orbit.circle(170)
mars_orbit.hideturtle()

jupiter_orbit = turtle.Turtle()
jupiter_orbit.speed(0)
jupiter_orbit.penup()
jupiter_orbit.goto(0, -240)
jupiter_orbit.pendown()
jupiter_orbit.circle(240)
jupiter_orbit.hideturtle()

saturn_orbit = turtle.Turtle()
saturn_orbit.speed(0)
saturn_orbit.penup()
saturn_orbit.goto(0, -340)
saturn_orbit.pendown()
saturn_orbit.circle(340)
saturn_orbit.hideturtle()

help = turtle.Turtle()
help.hideturtle()


# рух планет
mercury_speed = 4
venus_speed = 3
earth_speed = 2
mars_speed = 1
jupiter_speed = 0.5
saturn_speed = 0.2

for i in range(10000):
    x = 50 * math.cos(math.radians(i * mercury_speed))
    y = 50 * math.sin(math.radians(i * mercury_speed))
    mercury.goto(x, y)

    venus.goto(x, y)

    x = 120 * math.cos(math.radians(i * earth_speed))
    y = 120 * math.sin(math.radians(i * earth_speed))
    earth.goto(x, y)

    x = 170 * math.cos(math.radians(i * mars_speed))
    y = 170 * math.sin(math.radians(i * mars_speed))
    mars.goto(x, y)

    x = 240 * math.cos(math.radians(i * jupiter_speed))
    y = 240 * math.sin(math.radians(i * jupiter_speed))
    jupiter.goto(x, y)

    x = 340 * math.cos(math.radians(i * saturn_speed))
    y = 340 * math.sin(math.radians(i * saturn_speed))
    saturn.goto(x, y)