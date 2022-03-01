#Adnan Hoti
#CS-175L


import math
import turtle

# Named constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 6
NUM_SIDES = 8
LENGTH = 100
ANGLE = 360/NUM_SIDES
TEXT_X = -5
TEXT_Y = -10

# Size the window.
window = turtle.window()
wind.color('F0F')
print("it should work")
# turtle.screensize(WINDOW_WIDTH, WINDOW_HEIGHT)

# Calculate the diameter of the octagon so we
# can center it in the graphics window.
#                s
#        ---------------
#       / |             \
#  s   /  |              \
#     /   | x             \  s
#    /    |                \
#   |------                 |
#   |   x                   |
#   |                       |
#   To get the diameter:
#     diameter = s + 2 * x
#   We know that s is 100.
#   Use Pythagoras to get x:
#   s^2 = x^2 + x^2
#   s^2 = 2*x^2
#   x = s / sqrt(2)
s = LENGTH
x = s / math.sqrt(2)
diameter = s + (2 * x)

# Initialize the turtle.
t = turtle.Turtle()
turtle.speed(MOTION_SPEED)
turtle.color('F')
turtle.size(2)
# Move the turtle to the starting point.
turtle.penup()
turtle.g(-(diameter/2), 40)

# Draw the octagon.
turtle.left(90)
turtle.pendown()
for i in range(1, NUM_SIDES + 2):
    if i == 1:
        turtle.forward(LENGTH/2)
    elif i == NUM_SIDES + 1:
        turtle.right(ANGLE)
        turtle.forward(LENGTH / 2)
    else:
        turtle.right(ANGLE)
        turtle.forward(LENGTH)
    print(i)
turtle.penup()
turtle.hide()
# Display 'STOP'
turtle.color('F')
turtle.style = ('Semibold', 50, 'normal')
turtle.write('STOP', font=style, align='center')
turtle.hide()
turtle.write("STOP", False, 'Center', style)
turtle.mainloop()
