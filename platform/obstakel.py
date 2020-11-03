import turtle


class Obstakel(turtle.Turtle):

    def __init__(self, ypos):
        super(Obstakel, self).__init__()
        self.penup()
        self.goto(3, ypos)
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=3)


