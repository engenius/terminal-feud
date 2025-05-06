import blessed

term = blessed.Terminal()


class Score:
    """
    Score

    @param x: The horizontal location of the score.
    @param y: The vertival location of the score.
    @param score: The current score.
    """

    def __init__(self, x: int, y: int, score: int = 0):
        self.x: int = x
        self.y: int = y
        self.score: int = score

    def draw(self, score: int = None) -> None:
        """
        Draw the specified score or the current score if none is specified.

        @param score: The score to display. Also changes the current score.
        """

        self.score = score if score is not None else self.score

        print(term.yellow, end='')
        print(term.move_xy(self.x, self.y + 0) + ' ╔═════╗ ', end='')
        print(term.move_xy(self.x, self.y + 1) + ' ║     ║ ', end='')
        print(term.move_xy(self.x, self.y + 2) + ' ╚═════╝ ', end='')

        print(term.bright_white, end='')
        print(term.move_xy(self.x + 3, self.y + 1) + str(self.score).rjust(3), end='')

        print(term.normal, end='', flush=True)
