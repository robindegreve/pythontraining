import turtle
from time import sleep


class Manneke(turtle.Turtle):

    size_w = 3
    size_l = 3
    act_w = size_w * 10
    act_l = size_l * 10
    jump_h = 250
    tilted = "right"
    max_gravity = -157

    def __init__(self):
        super(Manneke, self).__init__()
        self.speed(0)
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(-350, self.max_gravity)
        self.shapesize(stretch_len=self.size_l, stretch_wid=self.size_w)  # maal 15
        self.dx = 0.1
        self.dy = 0.07


    def go_left(self):
        x = self.xcor()
        x -= 20
        self.setx(x)

        if self.tilted == "right":
            self.tilt(180)
            self.tilted = "left"


    def go_right(self):
        x = self.xcor()
        x += 20
        self.setx(x)

        if self.tilted == "left":
            self.tilt(180)
            self.tilted = "right"


    def jump(self):
        self.sety(self.ycor() + self.jump_h)


    def gravity(self):
        if self.ycor() > self.max_gravity:
            self.sety(self.ycor() - self.dy)


    def limit_gravity(self, maxgravity):
        if (self.ycor() - self.act_l) > maxgravity:
            self.sety(self.ycor() - self.dy)
