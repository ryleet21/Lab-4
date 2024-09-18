#the authors names are rylee and elizabeth
import turtle
tod = turtle.Turtle()
tod.color("yellow")


for side in range(4):
    if side == 1:
        tod.color("blue")
    if side == 2:
        tod.color("red")
    if side == 3:
        tod.color("purple")
    tod.forward(100)
    tod.right(90)
