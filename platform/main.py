from manneke import Manneke
from game import Game

speler = Manneke()
game = Game(speler)


def main():
    running = True
    while running:
        game.gameloop()


if __name__ == "__main__":
    main()


