import blessed
import time

import constants as const
from answer import Answer
from score import Score
from font import Font

term = blessed.Terminal()


class Round:
    """
    Round

    @param round_number: The number of the round.
    @param multiplier: The score multiplier.
    @param question: The question for the round.
    @param answers: The list of answers from those that were surveyed.
    @param answered: An array of surveyed answers that were correctly guessed by the players.
    @param x_count: The number of wrong answers that have been guessed.
    @param winner: The team that won the round.
    @param score: The current score for the round.
    """

    def __init__(self) -> None:
        self.round_number: int = 0
        self.multiplier: int = 3
        self.question: str = ''
        self.answers: list[Answer] = list()
        self.answered: set[int] = set()
        self.x_count: int = 0
        self.winner: str = ''
        self.score: Score = Score(const.ROUND_SCORE_X, const.ROUND_SCORE_Y, score=0)

    def draw_title_screen(self) -> None:
        """Draws the title screen."""

        print(term.home + term.clear, end='')

        if self.round_number == 1:
            Font.print(const.ROUND_TITLE_LINE1_X, const.ROUND_TITLE_LINE1_Y, 'ROUND 1')
        elif self.round_number == 2:
            Font.print(const.ROUND_TITLE_LINE1_X, const.ROUND_TITLE_LINE1_Y, 'ROUND 2')
        elif self.round_number == 3:
            Font.print(const.ROUND_TITLE_LINE1_X, const.ROUND_TITLE_LINE1_Y, 'ROUND 3')

        x = const.ROUND_TITLE_LINE2_X
        y = const.ROUND_TITLE_LINE2_Y

        if self.multiplier == 2:
            print(term.bright_blue, end='')
            print(term.move_xy(x, y + 0) + f" ___           _    _       ___     _     _", end='')
            print(term.move_xy(x, y + 1) + f"|   \\ ___ _  _| |__| |___  | _ \\___(_)_ _| |_ ___", end='')
            print(term.move_xy(x, y + 2) + f"| |) / _ \\ || | '_ \\ / -_) |  _/ _ \\ | ' \\  _(_-<", end='')
            print(term.move_xy(x, y + 3) + f"|___/\\___/\\_,_|_.__/_\\___| |_| \\___/_|_||_\\__/__/", end='')
            print(term.normal, end='', flush=True)

        elif self.multiplier == 3:
            print(term.bright_blue, end='')
            print(term.move_xy(x + 1, y + 0) + f" _____    _      _       ___     _     _", end='')
            print(term.move_xy(x + 1, y + 1) + f"|_   _| _(_)_ __| |___  | _ \\___(_)_ _| |_ ___", end='')
            print(term.move_xy(x + 1, y + 2) + f"  | || '_| | '_ \\ / -_) |  _/ _ \\ | ' \\  _(_-<", end='')
            print(term.move_xy(x + 1, y + 3) + f"  |_||_| |_| .__/_\\___| |_| \\___/_|_||_\\__/__/", end='')
            print(term.move_xy(x + 1, y + 4) + f"           |_|", end='')
            print(term.normal, end='', flush=True)

        print(term.normal, end='', flush=True)

    def draw_game_screen(self) -> None:
        """Draws the game screen."""

        self.draw_background()
        self.draw_question()
        self.draw_answers()
        self.draw_score()

    def draw_background(self) -> None:
        """Draws the background."""

        print(term.home + term.clear + term.white, end='')

        for y in range(0, 9):
            print(':' * const.SCREEN_WIDTH)

        box_inner_width = (const.ANSWER_WIDTH * const.ANSWER_COLS) + 3
        box_outer_width = box_inner_width + 4

        box_top = ' ┌' + ('─' * (box_inner_width)) + '┐ '
        box_middle = ' │' + (' ' * (box_inner_width)) + '│ '
        box_bottom = ' └' + ('─' * (box_inner_width)) + '┘ '
        side_background = ':' * ((const.SCREEN_WIDTH - box_outer_width) // 2)

        print(side_background + term.yellow + box_top + term.white + side_background)
        for y in range(0, 12):
            print(side_background + term.yellow + box_middle + term.white + side_background)
        print(side_background + term.yellow + box_bottom + term.white + side_background)
        print(':' * const.SCREEN_WIDTH)

        print(term.normal, end='', flush=True)

    def draw_question(self) -> None:
        """Draws the question."""

        # question fits on 1 line
        if len(self.question) <= const.QUESTION_MAX_WIDTH:
            box_width = len(self.question) + 4
            x = ((const.SCREEN_WIDTH - box_width) // 2)
            y = const.QUESTION_Y

            print(term.yellow)
            print(term.move_xy(x, y + 0) + ' ┌' + ('─' * (box_width - 2)) + '┐ ')
            print(term.move_xy(x, y + 1) + ' │' + (' ' * (box_width - 2)) + '│ ')
            print(term.move_xy(x, y + 2) + ' └' + ('─' * (box_width - 2)) + '┘ ')

            print(term.bright_white)
            print(term.move_xy(x + 3, y + 1) + self.question.upper())

        # question fits on 2 lines
        else:
            pos = self.question.rfind(' ', 0, (len(self.question) // 2))
            line1 = self.question[0:pos]
            line2 = self.question[pos + 1:]

            box_width = len(line2) + 4
            x = ((const.SCREEN_WIDTH - box_width) // 2)
            y = const.QUESTION_Y

            print(term.yellow)
            print(term.move_xy(x, y + 0) + ' ┌' + ('─' * (box_width - 2)) + '┐ ')
            print(term.move_xy(x, y + 1) + ' │' + (' ' * (box_width - 2)) + '│ ')
            print(term.move_xy(x, y + 2) + ' │' + (' ' * (box_width - 2)) + '│ ')
            print(term.move_xy(x, y + 3) + ' └' + ('─' * (box_width - 2)) + '┘ ')

            print(term.bright_white)
            print(term.move_xy(x + 2, y + 1) + line1.upper().center(box_width - 2))
            print(term.move_xy(x + 2, y + 2) + line2.upper().center(box_width - 2))

        print(term.normal)

    def draw_answers(self) -> None:
        """Draws the answers."""

        for i in range(1, 9):
            if i in self.answered:
                self.draw_answer(i)
            else:
                self.hide_answer(i)

    def hide_answers(self) -> None:
        """Hides the answers."""

        for index, answer in enumerate(self.answers):
            self.hide_answer(index + 1)

        self.draw_score(0)

    def show_remaining_answers(self) -> None:
        """Shows the remaining answers, the answers that have not been guessed."""

        answered = self.answered.copy()

        for index in range(len(self.answers), 0, -1):
            if index not in self.answered:
                self.draw_answer(index, show_animation=True)
                time.sleep(const.ANSWER_DELAY)

        self.answered = answered

    def toggle_answer(self, index: int) -> None:
        """
        Toggle the visibility of the specified answer.

        @param index: The index of the answer to toggle (1 to 8).
        """

        if index in self.answered:
            self.hide_answer(index)
        else:
            self.draw_answer(index, show_animation=True)

        self.draw_score()

    def draw_answer(self, index: int, show_animation: bool = False) -> None:
        """
        Draw the specified answer.

        @param index: The index of the answer to draw (1 to 8).
        @param show_animation: Wether to show the animation or not.
        """

        if index not in self.answered:
            self.answered.add(index)

        # determine location of answer based on index
        x = const.ANSWER_X + (((index - 1) // const.ANSWER_ROWS) * (const.ANSWER_WIDTH + 1))
        y = const.ANSWER_Y + (((index - 1) % const.ANSWER_ROWS) * (const.ANSWER_HEIGHT))

        if show_animation:
            self.draw_answer_animation(x, y)

        print(term.bright_blue, end='')
        print(term.move_xy(x, y + 0) + ' ┌──────────────────┬────┐ ', end='')
        print(term.move_xy(x, y + 1) + ' │                  │    │ ', end='')
        print(term.move_xy(x, y + 2) + ' └──────────────────┴────┘ ', end='')

        answer_text = self.answers[(index - 1)].text
        answer_score = self.answers[(index - 1)].score

        # truncate long answers
        max_answer_length = const.ANSWER_WIDTH - 9
        if answer_text and len(answer_text) > max_answer_length:
            answer_text = answer_text[0:max_answer_length-1] + '…'

        print(term.bright_white, end='')
        print(term.move_xy(x + 3, y + 1) + answer_text.upper().ljust(max_answer_length), end='')
        print(term.move_xy(x + (const.ANSWER_WIDTH - 3), y + 1) + str(answer_score).rjust(2), end='')

        print(term.normal, end='', flush=True)

    def hide_answer(self, index: int) -> None:
        """
        Hide the specified answer.

        @param index: The index of the answer to hide (1 to 8).
        """

        if index in self.answered:
            self.answered.remove(index)

        # determine location of answer based on index
        x = const.ANSWER_X + (((index - 1) // const.ANSWER_ROWS) * (const.ANSWER_WIDTH + 1))
        y = const.ANSWER_Y + (((index - 1) % const.ANSWER_ROWS) * (const.ANSWER_HEIGHT))

        print(term.bright_blue, end='')
        print(term.move_xy(x, y + 0) + ' ┌───────────────────────┐ ', end='')
        print(term.move_xy(x, y + 1) + ' │                       │ ', end='')
        print(term.move_xy(x, y + 2) + ' └───────────────────────┘ ', end='')

        # draw placeholder number if this index has an answer
        if (index - 1) < len(self.answers):
            print(term.bright_white, end='')
            print(term.move_xy(x + 2, y + 1) + ('[' + str(index) + ']').center(const.ANSWER_WIDTH - 2), end='')

        print(term.normal, end='', flush=True)

    def draw_answer_animation(self, x: int, y: int) -> None:
        """
        Draw the answer animation.

        Simulates the flip animation from the game show.

        @param x: The horizontal location of the animation.
        @param y: The vertical location of the animation.
        """

        print(term.bright_blue)
        print(term.move_xy(x, y + 0) + ' ┌───────────────────────┐ ')
        print(term.move_xy(x, y + 1) + ' │                       │ ')
        print(term.move_xy(x, y + 2) + ' └───────────────────────┘ ', flush=True)
        time.sleep(const.ANSWER_ANIMATION_DELAY)

        print(term.move_xy(x, y + 0) + '                           ')
        print(term.move_xy(x, y + 1) + ' ┌───────────────────────┐ ')
        print(term.move_xy(x, y + 2) + ' └───────────────────────┘ ', flush=True)
        time.sleep(const.ANSWER_ANIMATION_DELAY)

        print(term.move_xy(x, y + 0) + '                           ')
        print(term.move_xy(x, y + 1) + '                           ')
        print(term.move_xy(x, y + 2) + ' ───────────────────────── ', flush=True)
        time.sleep(const.ANSWER_ANIMATION_DELAY)

        print(term.move_xy(x, y + 0) + '                           ')
        print(term.move_xy(x, y + 1) + '                           ')
        print(term.move_xy(x, y + 2) + '                           ', flush=True)
        time.sleep(const.ANSWER_ANIMATION_DELAY)

        print(term.move_xy(x, y + 0) + ' ───────────────────────── ')
        print(term.move_xy(x, y + 1) + '                           ')
        print(term.move_xy(x, y + 2) + '                           ', flush=True)
        time.sleep(const.ANSWER_ANIMATION_DELAY)

        print(term.move_xy(x, y + 0) + ' ┌──────────────────┬────┐ ')
        print(term.move_xy(x, y + 1) + ' └──────────────────┴────┘ ')
        print(term.move_xy(x, y + 2) + '                           ', flush=True)
        time.sleep(const.ANSWER_ANIMATION_DELAY)

        print(term.move_xy(x, y + 0) + ' ┌──────────────────┬────┐ ')
        print(term.move_xy(x, y + 1) + ' │                  │    │ ')
        print(term.move_xy(x, y + 2) + ' └──────────────────┴────┘ ', flush=True)
        time.sleep(const.ANSWER_ANIMATION_DELAY)

    def draw_score(self) -> None:
        """Draws the round score."""

        score = 0
        for i in self.answered:
            score += self.answers[i - 1].score

        self.score.draw(score)

    def show_x(self) -> None:
        """Shows an X when a wrong answer is given."""

        if self.x_count < const.WRONG_ANSWER_MAX:
            self.x_count += 1

        # center the Xs horizontally
        x = ((const.SCREEN_WIDTH - (self.x_count * (const.WRONG_ANSWER_WIDTH + 3))) // 2) + 2
        y = const.WRONG_ANSWER_Y

        for i in range(0, self.x_count):
            self.draw_x(x, y)
            x += const.WRONG_ANSWER_WIDTH + 3

        # trigger the ssh bell character
        print('\a')

        print(term.normal, end='', flush=True)

        # after a delay, redraw the answers to erase the Xs
        time.sleep(const.WRONG_ANSWER_DELAY)
        self.draw_answers()

    def remove_x(self) -> None:
        """Decrements the X count."""

        if self.x_count > 0:
            self.x_count -= 1

    def draw_x(self, x: int, y: int) -> None:
        """
        Draws the X.

        @param x: The horizontal location of the X.
        @param y: The vertical location of the X.
        """

        print(term.bright_red, end='')
        print(term.move_xy(x, y + 0) + r'┌───────┐', end='')
        print(term.move_xy(x, y + 1) + r'│  \ /  │', end='')
        print(term.move_xy(x, y + 2) + r'│   X   │', end='')
        print(term.move_xy(x, y + 3) + r'│  / \  │', end='')
        print(term.move_xy(x, y + 4) + r'└───────┘', end='')
        print(term.normal, end='', flush=True)

    def toggle_winner_team_a(self) -> None:
        """Toggle team A as the winner of this round."""

        if self.winner == 'A':
            self.winner = ''
        else:
            self.winner = 'A'

    def toggle_winner_team_b(self) -> None:
        """Toggle team B as the winner of this round."""

        if self.winner == 'B':
            self.winner = ''
        else:
            self.winner = 'B'
