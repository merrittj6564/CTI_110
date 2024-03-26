#Joseph_Merritt
#26_Mar_24
#P4LAB1 - Using loops and turtle to draw shapes

import turtle
win = turtle.Screen()
t = turtle.Turtle()

# add some display options
t.pensize(4)         
t.pencolor("blue")   
t.shape("arrow")

#Use a for loop to draw the square

for side in range(4):
    t.forward(75)
    t.right(90)

#Use While loop to draw the triange

counter = 0

while counter <3:
    t.forward(75)
    t.left(120)
    counter += 1