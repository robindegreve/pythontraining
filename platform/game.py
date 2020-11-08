from obstakel import Obstakel
import turtle


class Game:

    obstacles = []
    screen = turtle.Screen()

    def __init__(self, player):
        self.player = player
        self.obstacles.append(Obstakel(0))
        # self.obstacles.append(Obstakel(100))
        # self.obstacles.append(Obstakel(200))
        self.init_screen()

    def gameloop(self):
        self.check_colision()
        self.screen.update()


    def check_colision(self):
        for obst in self.obstacles:
            if (self.player.xcor()) > (obst.xpos - obst.act_w) \
                    and (self.player.ycor() - self.player.act_l) >= (obst.ypos - obst.act_l) \
                    and self.player.xcor() < (obst.xpos + obst.act_w):
                self.player.limit_gravity((obst.ypos + obst.act_l))
            elif (obst.xpos - obst.act_w) < (self.player.xcor() + self.player.act_w) < (obst.xpos + obst.act_w) \
                    and (self.player.ycor() - self.player.act_l) < (obst.ypos + obst.act_l):
                self.player.setx((self.player.xcor() - self.player.size_w))
            elif (obst.xpos + obst.act_w) > (self.player.xcor() - self.player.act_w) > (obst.xpos - obst.act_w) \
                    and (self.player.ycor() - self.player.act_l) < (obst.ypos + obst.act_l):
                self.player.setx((self.player.xcor() + self.player.size_w))
            else:
                self.player.gravity()


    def init_screen(self):
        self.screen.title("Robinland")
        self.screen.bgpic("bg.gif")
        self.screen.setup(width=700, height=500)
        self.screen.tracer(0)
        self.screen.listen()
        self.screen.onkeypress(self.player.go_left, "q")
        self.screen.onkeypress(self.player.go_right, "d")
        self.screen.onkeypress(self.player.jump, "z")
