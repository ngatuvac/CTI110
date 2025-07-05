# Caleb Ngatuvai
# 5 July 2025
# P4LAB1a
# Use turtle and a loop to draw a square and a triangle

#import turtle, create turtle execution window, and drawing object
import turtle
win = turtle.Screen()
cn = turtle.Turtle()

#set turtle options
cn.pensize(5)
cn.pencolor("blue")
cn.shape("turtle")

#draw square with for loop
for n in range(4):
    cn.forward(100)
    cn.right(90)

#draw triangle with for loop
for n in range(3):
    cn.forward(100)
    cn.left(120)

#wait to allow user to close window
win.mainloop()
