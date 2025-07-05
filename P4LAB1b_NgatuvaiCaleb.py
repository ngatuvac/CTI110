# Caleb Ngatuvai
# 5 July 2025
# P4LAB1b
# Use turtle to draw your initials

#import turtle, create window, and drawing object
import turtle
win = turtle.Screen()
cn = turtle.Turtle()

#set turtle options
cn.pensize(5)
cn.pencolor("blue")
cn.shape("turtle")

#first initial "C"
cn.forward(50)
cn.left(90)
cn.penup()
cn.forward(100)
cn.left(90)
cn.pendown()
cn.forward(50)
cn.left(90)
cn.forward(100)
cn.left(90)

#second initial "N"
cn.penup()
cn.forward(100)
cn.pendown()
cn.left(90)
cn.forward(100)
cn.right(135)
cn.forward(141)
cn.left(135)
cn.forward(100)

#keeps window open until user closes it
win.mainloop()
