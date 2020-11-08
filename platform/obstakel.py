import turtle


class Obstakel(turtle.Turtle):

    ypos = -157
    size_w = 3
    size_l = 1
    act_w = size_w * 10
    act_l = size_l * 10

    def __init__(self, xpos):
        super(Obstakel, self).__init__()
        self.penup()
        self.goto(xpos, self.ypos)
        self.shape("square")
        self.resizemode("user")
        self.shapesize(stretch_len=self.size_l, stretch_wid=self.size_w)  # maal 15
        self.color("#663300")
        self.xpos = xpos

