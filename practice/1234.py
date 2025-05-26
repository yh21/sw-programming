import turtle as t

t.shape('turtle')
t.speed(0)
colors = ['red', 'orange', 'crimson', 'blue']

def circles():
    radius = 10
    while radius <= 150:
        t.circle(radius)
        radius += 10
def up():
    t.penup()
    t.home()
    t.setheading(0) 
    t.pendown()
    t.color(colors[0])
    circles()
def right():
    t.penup()
    t.home()
    t.setheading(270)  
    t.pendown()
    t.color(colors[1])
    circles()
def down():
    t.penup()
    t.home()
    t.setheading(180)  
    t.pendown()
    t.color(colors[2])
    circles()

def left():
    t.penup()
    t.home()
    t.setheading(90)  
    t.pendown()
    t.color(colors[3])
    circles()
def cross():
    t.color('green')
    t.penup()

    t.goto(-350, 0)
    t.pendown()
    t.goto(350, 0)
    t.penup()

    t.goto(0, -350)
    t.pendown()
    t.goto(0, 350)
    t.penup()

    t.goto(0, -350)
    t.setheading(270)

t.listen()
t.onkeypress(up, 'Up')
t.onkeypress(right, 'Right')
t.onkeypress(down, 'Down')
t.onkeypress(left, 'Left')
t.onkeypress(cross, 'space')
t.mainloop()