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


    def check_colision(self, player):
        # komende van links
        # check eerst x-as
        # dan y-as
        # alleen terwijl in linker deel
        if ((player.xcor() + player.act_w) > (self.xpos - self.act_w)) \
                and ((player.ycor() - player.act_l) < (self.ypos + self.act_l)) \
                and (player.xcor() < self.xpos):
            player.setx(player.xcor() - player.size_w)

        # komende van rechts
        if ((player.xcor() - player.act_w) < (self.xpos + self.act_w)) \
                and ((player.ycor() - player.act_l) < (self.ypos + self.act_l)) \
                and (player.xcor() > self.xpos):
            player.setx(player.xcor() + player.size_w)


    # hitbox
    #   x-as links:
    #       self.ycor - (self.size_w * 10) - (player.size_w * 10)
    #
    #   x-as rechts:
    #       self.ycor + (self.size_w * 10) + (player.size_w * 10)
    #
    #   y-as boven:
    #

