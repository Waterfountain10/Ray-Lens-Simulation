#draw border
import turtle
import math
from turtle import mainloop

wn = turtle.Screen()
turtle.screensize(305,305,"black")

#Pen set up
pointer = turtle.Turtle()
pointer.color("red")
pointer.shape("classic")

def initialize():
    mypen = turtle.Turtle()
    mypen.color("white")
    mypen.penup()
    mypen.setposition(-250,-250)
    mypen.pendown()
    mypen.pensize(3)
    for side in range(4):
        mypen.forward(500)
        mypen.left(90)
    mypen.hideturtle()
    return()
initialize()
def reset():
    turtle.clear()
def start():
    pointer.penup()
    pointer.goto(0,0)
    x = int(input("set x coordinate of pointer: "))
    y = int(input("set y coordinate of pointer: "))
    if x > 250 or x < -250:
        print("The input given is outside the border. Please input an x value that is between -250 and 250. Type restart() in the terminal")
        return
    if y > 250 or y < -250:
        print("The input given is outside the border. Please input an y value that is between -250 and 250. Type restart() in the terminal")
        return
    new_point = (x,y)
    pointer.goto(new_point)

def orient():
    opposite = pointer.ycor()
    adjacent = pointer.xcor()
    x = opposite/adjacent
    angle = math.atan(x)
    angle = math.degrees(x)
    if pointer.xcor() > 0 and pointer.xcor() > 0:
        tilt = angle + 180
        pointer.left(tilt)
    if pointer.xcor()> 0 and pointer.ycor()<0:
        tilt = angle + 180
        pointer.right(tilt)
    if pointer.xcor()< 0 and pointer.ycor()>0:
        tilt = angle
        pointer.right(tilt)
    if pointer.xcor()< 0 and pointer.ycor()<0:
        tilt = angle
        pointer.left(tilt)

def create_mirror(angle):
    m = turtle.Turtle()# m is at 0,0
    m.color("white")
    m.shape("square")
    m.tilt(angle)
    m.shapesize(0.1,5)  

theta_m = int(input("angle of mirror: "))
create_mirror(theta_m)


def reflexion():
    ref = turtle.Turtle()
    ref.color("pink")
    ref.penup()
    ref.setposition(0,0)
    ref.pendown()
    ref.pensize(2)

    ref.left(theta_r)
    while True:
        if ref.xcor() > 250 or ref.xcor() < -250 or ref.ycor() > 250 or ref.ycor() < -250:
            return()
        
        else:
            ref.forward(4)
            
    



start()
orient()
pointer.pendown()
theta_i = pointer.towards(0,0)

theta_j = 180 - theta_m
theta_k = 180 - theta_j - theta_i
theta_r = theta_k + theta_m


pointer.goto(0,0)
pointer.hideturtle()

reflexion()
print("---------------------------------")
print(f'Angle of incident ray: {theta_i}')
print(f'Angle of reflected ray: {theta_r}')
print("---------------------------------")
mainloop()