from turtle import Turtle, Screen
import random

milo = Turtle()
milo.shape("turtle")
milo.color("red")
milo.forward(100)
milo.right(90)

# Drawing a square with turtle challenge 1 option 1
milo.forward(100)
milo.right(90)
milo.forward(100)
milo.right(90)
milo.forward(100)
milo.right(90)
milo.forward(100)
milo.right(90)

# Drawing a square with turtle challenge 1 option 2
for _ in range(4):
    milo.forward(100)
    milo.right(90)

# Drawing a dashed line with turtle challenge 2
for _ in range(15):
    milo.forward(10)
    milo.penup()
    milo.forward(10)
    milo.pendown()

# Drawing a different shapes with turtle challenge 3
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        milo.forward(100)
        milo.right(angle)

for shape_side_n in range(3, 11):
    milo.color(random.choice(colours))
    draw_shape(shape_side_n)

# Drawing a Random Walk with list of colours turtle challenge 4
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
milo.pensize(10)
milo.speed(("fastest"))

for _ in range(200):
    milo.color(random.choice(colours))
    milo.forward(30)
    milo.setheading(random.choice(directions))

# Drawing a Random Walk with random colours turtle challenge 5
import turtle as t
import random

milo = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

directions = [0, 90, 180, 270]
milo.pensize(10)
milo.speed(("fastest"))

for _ in range(200):
    milo.color(random_color())
    milo.forward(30)
    milo.setheading(random.choice(directions))

# Making a Spirograph with turtle challenge 6
import turtle as t
import random

milo = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

milo.speed(("fastest"))

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        milo.color(random_color())
        milo.circle(100)
        milo.setheading(milo.heading() + size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()

