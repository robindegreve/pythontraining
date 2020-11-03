import turtle
from manneke import Manneke
from obstakel import Obstakel


wn = turtle.Screen()
wn.setup(width=700, height=500)
wn.title("Robinland")
wn.tracer(0)
wn.bgpic("bg.gif")


# manneke
speler = Manneke()

# obstakel
obstakel = Obstakel(-157)


# tegenstander


while True:
    wn.update()
