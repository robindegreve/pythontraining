import turtle
from manneke import Manneke
from obstakel import Obstakel


wn = turtle.Screen()
wn.title("Robinland")
wn.bgpic("bg.gif")
wn.setup(width=700, height=500)
wn.tracer(0)

# manneke
speler = Manneke()

wn.listen()
wn.onkeypress(speler.go_left, "q")
wn.onkeypress(speler.go_right, "d")
wn.onkeypress(speler.jump, "z")


# obstakels
obstakel_a = Obstakel(0)


def main():
    running = True
    while running:
        wn.update()
        obstakel_a.check_colision(speler)


if __name__ == "__main__":
    main()


