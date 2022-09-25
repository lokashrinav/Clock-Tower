#Rayan Zafar
#Shrinav Loka
#LITE ClockTower
# Moving clock inside of an hour so its a clockclocktower in a sunny day.
#The clock will revolve with both the hour and and minute hand moving in cohesion.
#The buildings are made by using for loops of rectangles stacking up on to each other
#The goal and purpose is to create a working clock tower which has a moving hour and minute hand. 
import turtle as trtl
wn = trtl.Screen()
clocktower = trtl.Turtle()
#sets screen update as zero
trtl.tracer(0,0)
#sets the array with colors
color = ["peru", "yellow", "red", "black", "white", "light blue", "silver"]
#creates the rectangular part of the building
y=0

clocktower.penup()
clocktower.goto(-200,-400)
clocktower.pendown()
if y == 0:
    clocktower.fillcolor(color[3])
clocktower.begin_fill()
clocktower.left(90)
clocktower.forward(500)
clocktower.right(90)
clocktower.forward(400)
clocktower.right(90)
clocktower.forward(500)
clocktower.right(90)
clocktower.forward(400)
clocktower.end_fill()

#creates the triangle on top of the building
clocktower.fillcolor(color[0])
clocktower.begin_fill()
clocktower.goto(-200,100)
clocktower.right(135)
clocktower.forward(282.84)
clocktower.right(90)
clocktower.forward(282.84)
clocktower.right(135)
clocktower.forward(400)
clocktower.end_fill()

vertical_line_y=-400
#imports a clock image for the tower and sets in in the middle of the clock tower
robot_image = "clocknohands.gif"
wn.addshape("clocknohands.gif")
clock = trtl.Turtle(shape="clocknohands.gif")
clock.penup()
clock.goto(0,-50)
clock.pendown()
trtl.update()
#Creates the bricks for the building by using white lines
#Creates vertical lines for the bricks
clocktower.left(180)
for widthbricks in range(10):
    clocktower.pencolor(color[4])
    clocktower.penup()
    clocktower.goto(-200,vertical_line_y)
    clocktower.pendown()
    clocktower.forward(400)
    vertical_line_y=vertical_line_y+50
#Creates the horizontal lines for the bricks
j=-150
k=-400
clocktower.left(90)
for g in range(7):
    for y in range(5):
        clocktower.pencolor(color[4])
        clocktower.penup()
        clocktower.goto(j,k)
        clocktower.pendown()
        clocktower.forward(50)
        k=k+100
    k=-400
    j=j+50
gg=-175
tt=-350
#creates vertical lines for the bricks
for q in range(8):
    for w in range(5):
        clocktower.pencolor(color[4])
        clocktower.penup()
        clocktower.goto(gg,tt)
        clocktower.pendown()
        clocktower.forward(50)
        tt=tt+100
    tt=-350
    gg=gg+50
# creates turtle's for the hand's, erasers and clock center.
minutehand = trtl.Turtle()
minutehand.speed(0)
wn.bgcolor(color[5])
minhanderaser = trtl.Turtle()
clockcenter = trtl.Turtle()
hourhand = trtl.Turtle()
hourhanderaser = trtl.Turtle()
minutehand.speed(0)
#creates the center of the clock
def center():
    clockcenter.penup()
    clockcenter.goto(0,-60)
    clockcenter.pendown()
    clockcenter.hideturtle()
    clockcenter.fillcolor(color[6])
    clockcenter.begin_fill()
    clockcenter.circle(10)
    clockcenter.end_fill()
#rotation of the hour hand by inserting a new arrow hand in front of him
def minutehandrotation():
    wn.tracer(0) 
    minhanderaser.penup()
    minhanderaser.goto(0,-50)
    minhanderaser.pendown()
    minhanderaser.hideturtle()
    center()
    minhanderaser.begin_fill()
    minhanderaser.backward(8)
    minhanderaser.left(90)
    minhanderaser.forward(48)
    minhanderaser.left(90)
    minhanderaser.forward(8)
    minhanderaser.right(135)
    minhanderaser.forward(20)
    minhanderaser.right(90)
    minhanderaser.forward(20)
    minhanderaser.right(135)
    minhanderaser.forward(8)
    minhanderaser.left(90)
    minhanderaser.forward(48)
    minhanderaser.right(90)
    minhanderaser.forward(8)
    minhanderaser.end_fill()
    center()
    minhanderaser.penup()
    minhanderaser.left(180)
    minhanderaser.pendown()
    minhanderaser.goto(0,-50)
    minhanderaser.right(2)
    center()
    trtl.update()
#rotation of the white minutehand eraser which deletes previous animation
#This works by inserting a white arrow on the previous animation to make it seem as though their is animation
def minuterotationeraser():
    minutehand.penup()
    minutehand.goto(0,-50)
    minutehand.pendown()
    minutehand.hideturtle()
    center()
    minutehand.begin_fill()
    minutehand.backward(8)
    minutehand.left(90)
    minutehand.forward(48)
    minutehand.left(90)
    minutehand.forward(8)
    minutehand.right(135)
    minutehand.forward(20)
    minutehand.left(135)
    minutehand.forward(24)
    minutehand.left(90)
    minutehand.forward(48)
    minutehand.end_fill()
    minutehand.penup()
    minutehand.left(180)
    minutehand.goto(0,-50)
    minutehand.pendown()
    minutehand.right(2)
    center()
#rotation of the hour hand by inserting a new arrow hand in front of it
def hourhandrotation():
    hourhand.speed(0)
    hourhand.penup()
    hourhand.goto(0,-50)
    hourhand.pendown()
    hourhand.hideturtle()
    center()
    hourhand.begin_fill()
    hourhand.backward(6)
    hourhand.left(90)
    hourhand.forward(32)
    hourhand.left(90)
    hourhand.forward(6)
    hourhand.right(135)
    hourhand.forward(20)
    hourhand.right(90)
    hourhand.forward(20)
    hourhand.right(135)
    hourhand.forward(6)
    hourhand.left(90)
    hourhand.forward(32)
    hourhand.right(90)
    hourhand.forward(6)
    hourhand.end_fill()
    center()
    hourhand.penup()
    hourhand.left(180)
    hourhand.pendown()
    hourhand.goto(0,-50)
    hourhand.right(1/6)
    center()
    #updatesscreen 
    trtl.update()
#rotation of the white hour hand eraser which deletes previous animation
#This works by inserting a white half arrow on the previous animation to make it seem as though this is an animation. Deletes previous animation
def hourrotationeraser():
    hourhanderaser.speed(0)
    hourhanderaser.penup()
    hourhanderaser.goto(0,-50)
    hourhanderaser.pendown()
    hourhanderaser.hideturtle()
    center()
    hourhanderaser.begin_fill()
    hourhanderaser.backward(6)
    hourhanderaser.left(90)
    hourhanderaser.forward(32)
    hourhanderaser.left(90)
    hourhanderaser.forward(6)
    hourhanderaser.right(135)
    hourhanderaser.forward(20)
    hourhanderaser.left(135)
    hourhanderaser.forward(24)
    hourhanderaser.left(90)
    hourhanderaser.forward(32)
    hourhanderaser.end_fill()
    center()
    hourhanderaser.penup()
    hourhanderaser.left(180)
    hourhanderaser.goto(0,-50)
    hourhanderaser.pendown()
    hourhanderaser.right(1/6)
    center()
#creates an infinite loop
infiniteloop = True
#color of the clock hands
#code for the rotation of the whole entire clock
while infiniteloop is True:
    wn.tracer(0) 
    minhanderaser.fillcolor(color[3])
    minutehandrotation()
    minutehand.pencolor(color[4])
    minutehand.fillcolor(color[4])
    minuterotationeraser()
    hourhandrotation()
    hourhanderaser.pencolor(color[4])
    hourhanderaser.fillcolor(color[4])
    hourrotationeraser()





wn.mainloop()