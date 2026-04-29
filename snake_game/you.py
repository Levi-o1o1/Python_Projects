import turtle 
import time
import random
delay = 0.1

# screen
windo = turtle.Screen()
windo.title("Snake Game By Levi-o1o1")
windo.bgcolor("green")
windo.setup(width=600, height=600)
windo.tracer(0)

# snake head
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,150)

# snake food
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

seg = []

# fuctions
def go_up():
    head.direction = "up"

def go_rigth():
    head.direction = "rigth"

def go_left():
    head.direction = "left"
        
def go_down():
    head.direction = "down"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "rigth":
        x = head.xcor()
        head.setx(x + 20)

# Keyborad bindings
windo.listen()
windo.onkeypress(go_up, "w")
windo.onkeypress(go_down, "s")
windo.onkeypress(go_rigth, "d")
windo.onkeypress(go_left, "a")
# main game loop
while True:
    windo.update()
    # check for a collision with the food
    if head.distance(food) < 20:
        # move the food to a random spot
        x = random.randint(-290,290)
        y = random.randint(-290, 290)
        food.goto(x,y)
        # add a segment
        new_segment = turtle.Turtle()
        new_segment.speed()
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        seg.append(new_segment)
    # move the end segment first in reverse order
    for index in range(len(seg)-1, 0, -1):
        x = seg[index-1].xcor()
        y = seg[index-1].ycor()
        seg[index].goto(x, y)

    # Move segment zero where the head is :
    if len(seg) > 0:
        x = head.xcor()
        y = head.ycor()
        seg[0].goto(x,y)
    
    move()
    time.sleep(delay)
windo.mainloop()