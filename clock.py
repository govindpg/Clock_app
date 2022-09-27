import turtle
import time 

wn=turtle.Screen()
wn.title("clock")
wn.bgcolor("black")
wn.setup(width=600,height=600)
wn.tracer(0)

#pen
t=turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(3)
t.color("white")


def clock(h,m,s,t):
    t.up()
    t.goto(0,210)
    t.setheading(180)
    
    t.pendown()
    t.circle(210)
 
    t.penup()
    t.goto(0,0)
    t.setheading(90)

    for i in range(12):
        t.fd(190)
        t.pendown()
        t.fd(20)
        t.penup()
        t.goto(0,0)
        t.rt(30)


    #Hour hand
    t.penup()
    t.goto(0,0)
    t.color("white")
    t.pensize(4)
    t.setheading(90)
    angle=(h/12) * 360
    t.rt(angle)
    t.pendown()
    t.fd(90)
    
     
    #minute 
    t.penup()
    t.goto(0,0)
    t.color("green")
    t.setheading(90)
    angle=(m/60) * 360
    t.rt(angle)
    t.pendown()
    t.fd(120)

    #second
    t.penup()
    t.goto(0,0)
    t.color("red")
    t.setheading(90)
    angle=(s/60) * 360
    t.rt(angle)
    t.pendown()
    t.fd(140)

while True:
    h= int(time.strftime("%I"))
    m =int(time.strftime("%M"))
    s=int(time.strftime("%s"))

    clock(h,m,s,t)
    time.sleep(1)
    wn.update()

    t.clear()

wn.mainloop()
