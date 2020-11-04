import turtle


class Obstakel(turtle.Turtle):

    ycor = -157

    def __init__(self, xpos):
        super(Obstakel, self).__init__()
        self.penup()
        self.goto(xpos, self.ycor)
        self.shape("square")
        self.resizemode("user")
        self.shapesize(stretch_len=1, stretch_wid=3)
        self.color("green")
        self.xpos = xpos


    def check_colision(self, player):
        # turtle mag niet tussen x coords zitten
        # -157 is midden, dus outline is -147 en -167
        if (player.xcor() > (self.xpos - 60)) and (player.ycor() < self.ycor):
            player.setx(self.xpos - 60)


