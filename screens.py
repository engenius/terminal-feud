from enum import Enum


class Screens(Enum):
    """
    Screens

    The list of screens for the game.
    """

    GAME_TITLE_SCREEN = 1
    ROUND_1_TITLE_SCREEN = 2
    ROUND_1_GAME_SCREEN = 3
    ROUND_2_TITLE_SCREEN = 4
    ROUND_2_GAME_SCREEN = 5
    ROUND_3_TITLE_SCREEN = 6
    ROUND_3_GAME_SCREEN = 7
    FASTROUND_TITLE_SCREEN = 8
    FASTROUND_GAME_SCREEN = 9

    def next(self):
        """Return the next screen or the last screen if at the end."""
        items = list(self.__class__)
        index = items.index(self) + 1
        if index >= len(items):
            index = len(items) - 1
        return items[index]

    def prev(self):
        """Return the previous screen or the first screen if at the beginning."""
        items = list(self.__class__)
        index = items.index(self) - 1
        if index < 0:
            index = 0
        return items[index]
