from game import Game


def main() -> None:
    game = Game()
    game.load()
    game.loop()


if __name__ == '__main__':
    main()
