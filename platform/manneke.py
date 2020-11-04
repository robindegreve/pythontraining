import turtle
from time import sleep


class Manneke(turtle.Turtle):

    def __init__(self):
        super(Manneke, self).__init__()
        self.speed(0)
        self.shape("turtle")
        self.color("brown")
        self.penup()
        self.goto(-350, -157)
        self.shapesize(stretch_len=3, stretch_wid=3)
        self.dx = 0.1
        self.dy = 0.1


    def go_left(self):
        x = self.xcor()
        x -= 20
        self.setx(x)


    def go_right(self):
        x = self.xcor()
        x += 20
        self.setx(x)


    def jump(self):
        if self.ycor() <= -157:
            self.sety(self.ycor() + 100)


    def gravity(self):
        if self.ycor() > -157:
            print("going down")
            self.sety(self.ycor() - self.dy)
