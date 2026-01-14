import os 
import random

import turtle
turtle.fd(0)
# set the animation speed to the maximum
turtle.speed(0)
#  change the background color 
turtle.bgcolor("black")
# hide the turtle cursor
turtle.ht()
# this saves memory
turtle.setundobuffer(1)
#  this speeds up drawing
turtle.tracer(1)

class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape = spriteshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.fd(0)
        self.goto(startx, starty)
        self.speed = 1
    def move(self):
        self.fd(self.speed)
        # boundary detection
        if self.xcor() > 290:
            self.rt(60)
            

class Player(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite. __init__(self, spriteshape, color, startx, starty)
        self.speed = 4
        self.lives = 3
    def turn_left(self):
        self.lt(45)
    def turn_right(self):
        self.rt(45)
    def accelerate(self):
        self.speed += 1
    def decelerate(self):
        self.speed -= 1
class Game():
    def __init__(self):
        self.level = 1
        self.score = 0
        self.state = "playing"
        self.pen = turtle.Turtle()
        self.lives = 3
    def draw_border(self):
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.goto(-300, 350)
        self.pen.pendown()
        for side in range(4):
            self.pen.fd(600)
            self.pen.rt(90)
        self.pen.penup()
        self.pen.ht()
# create game object
game =Game()
# Draw the game border
game.draw_border()

player = Player("triangle", "white", 0, 0)
    #  main game loop

#keyboard bindings
turtle.onkey(player.turn_left, "Left")
turtle.onkey(player.turn_right, "Right")
turtle.onkey(player.accelerate, "w")
turtle.onkey(player.decelerate, "s")
turtle.listen()
while True:
    player.move()
    player.turn_left()
    # player.fd(player.speed)

raw_input = input











delay = raw_input("press enter to finish. >")