'''
Turtle Recursion (30pts)

1)  Using the turtle library, create the H fractal pattern as shown in the image (htree4.jpg) in this directory. (15pts)

2)  Using the turtle library, create any of the other recursive patterns in the directory. (10pts)

# escher fractal: get to midpoint of line and turn 45 degrees

3)  Create your own work of art with a repeating pattern of your making.  It must be a repeated pattern using recursion. Snowflakes, trees, and spirals are a common choice.  Or you can create a third one from the directory. (5pt)


 Each fractal should
 - be recursive
 - have a depth of at least 4
 - be contained on the screen

  Have fun!
'''



import turtle
my_screen = turtle.Screen()
my_screen.bgcolor('white')

my_hfractal = turtle.Turtle()
my_hfractal.shape("turtle")
my_hfractal.speed(0)

my_hfractal.up()
my_hfractal.down()
my_hfractal.goto(0, 0)
my_hfractal.setheading(180)

def draw_hfractal(length, depth):
    if depth > 0:
        my_hfractal.forward(length / 2)
        my_hfractal.right(90)
        my_hfractal.forward(length / 2)
        my_hfractal.left(90)
        draw_hfractal(length / 2, depth - 1)
        my_hfractal.left(90)
        my_hfractal.forward(length)
        my_hfractal.right(90)
        draw_hfractal(length / 2, depth - 1)
        my_hfractal.right(90)
        my_hfractal.forward(length / 2)
        my_hfractal.right(90)
        my_hfractal.forward(length)
        my_hfractal.left(90)
        my_hfractal.forward(length / 2)
        my_hfractal.left(90)
        draw_hfractal(length / 2, depth - 1)
        my_hfractal.left(90)
        my_hfractal.forward(length)
        my_hfractal.right(90)
        draw_hfractal(length / 2, depth - 1)
        my_hfractal.right(90)
        my_hfractal.forward(length / 2)
        my_hfractal.left(90)
        my_hfractal.forward(length / 2)
draw_hfractal(300, 4)

my_screen.clear()
my_escherfractal = turtle.Turtle()
my_escherfractal.shape("turtle")
my_escherfractal.speed(0)

my_screen = turtle.Screen()
my_screen.bgcolor('white')

my_escherfractal.up()
my_escherfractal.down()
my_escherfractal.goto(200, -200)
my_escherfractal.setheading(180)


def draw_escherfractal(length, depth):
    if depth > 0:
        my_escherfractal.forward(length)
        my_escherfractal.right(90)
        my_escherfractal.forward(length)
        my_escherfractal.right(90)
        my_escherfractal.forward(length)
        my_escherfractal.right(90)
        my_escherfractal.forward(length)
        my_escherfractal.right(90)
        my_escherfractal.forward(length / 2)
        my_escherfractal.right(45)
        draw_escherfractal(length / pow(2, 1/2), depth - 1)

draw_escherfractal(400, 10)


my_screen.clear()
my_fractal = turtle.Turtle()
my_fractal.shape("turtle")
my_fractal.speed(10)

my_screen = turtle.Screen()
my_screen.bgcolor("white")

my_fractal.up()
my_fractal.down()
my_fractal.goto(-120, -200)
my_fractal.setheading(120)

def draw_spiral(length, depth):
    if depth > 0:
        my_fractal.forward(length)
        my_fractal.right(60)
        my_fractal.forward(length)
        my_fractal.right(60)
        my_fractal.forward(length)
        my_fractal.right(60)
        my_fractal.forward(length)
        my_fractal.right(60)
        my_fractal.forward(length)
        my_fractal.right(60)
        my_fractal.forward(length / 4)
        draw_spiral(length / 2, depth - 1)
draw_spiral(250, 10)
my_screen.exitonclick()