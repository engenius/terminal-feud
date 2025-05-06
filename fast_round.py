import blessed
import time

import constants as const
from guess import Guess
from score import Score
from font import Font

term = blessed.Terminal()


class FastRound:
    """
    FastRound

    @param current_step: The current step for the round.
    @param questions: The list of questions for the round.
    @param guesses: The list of player guesses.
    @param show_guesses: Whether to show the current guesses or not.
    @param winner: The team that won this round.
    @param score: The current score for the round.
    """

    def __init__(self) -> None:
        self.current_step: int = 0
        self.questions: list[Question] = list()
        self.guesses: list[Guess] = list()
        self.show_guesses: bool = True
        self.winner: str = ''
        self.score: Score = Score(const.FASTROUND_SCORE_X, const.FASTROUND_SCORE_Y, score=0)

    def draw_title_screen(self) -> None:
        """Draws the title screen."""

        print(term.home + term.clear, end='')
        Font.print(const.FASTROUND_TITLE_LINE1_X, const.FASTROUND_TITLE_LINE1_Y, 'FAST')
        Font.print(const.FASTROUND_TITLE_LINE2_X, const.FASTROUND_TITLE_LINE2_Y, 'MONEY')
        print(term.normal, end='', flush=True)

    def draw_game_screen(self) -> None:
        """Draws the game screen."""

        self.draw_background()
        self.draw_question('Fast Money')
        self.draw_guesses()
        self.draw_score()

    def draw_background(self) -> None:
        """Draws the background."""

        print(term.home + term.clear + term.white, end='')

        for y in range(0, 6):
            print(':' * const.SCREEN_WIDTH)

        box_inner_width = (const.GUESS_WIDTH * const.GUESS_COLS) + 3
        box_outer_width = box_inner_width + 4

        box_top = ' ┌' + ('─' * (box_inner_width)) + '┐ '
        box_middle = ' │' + (' ' * (box_inner_width)) + '│ '
        box_bottom = ' └' + ('─' * (box_inner_width)) + '┘ '
        side_background = ':' * ((const.SCREEN_WIDTH - box_outer_width) // 2)

        print(side_background + term.yellow + box_top + term.white + side_background)
        for y in range(0, 15):
            print(side_background + term.yellow + box_middle + term.white + side_background)
        print(side_background + term.yellow + box_bottom + term.white + side_background)
        print(':' * const.SCREEN_WIDTH)

        print(term.normal, end='', flush=True)

    def draw_question(self, text: str) -> None:
        """
        Draws the specified question.

        @param text: The question to be displayed.
        """

        # erase the old question
        print(term.home)
        for y in range(0, 5):
            print(':' * const.SCREEN_WIDTH)

        # question fits on 1 line
        if (len(text) <= const.QUESTION_MAX_WIDTH):
            box_width = len(text) + 4
            x = ((const.SCREEN_WIDTH - box_width) // 2)
            y = const.QUESTION_Y

            print(term.yellow)
            print(term.move_xy(x, y + 0) + ' ┌' + ('─' * (box_width - 2)) + '┐ ')
            print(term.move_xy(x, y + 1) + ' │' + (' ' * (box_width - 2)) + '│ ')
            print(term.move_xy(x, y + 2) + ' └' + ('─' * (box_width - 2)) + '┘ ')

            print(term.bright_white)
            print(term.move_xy(x + 3, y + 1) + text.upper())

        # question fits on 2 lines
        else:
            pos = text.rfind(' ', 0, (len(text) // 2))
            line1 = text[0:pos]
            line2 = text[pos + 1:]

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

    def draw_guesses(self) -> None:
        """Draw the guesses."""

        question_index = (self.current_step // const.GUESS_STEPS) % const.GUESS_ROWS
        guess_index = (self.current_step // const.GUESS_STEPS) + 1

        self.draw_question(self.questions[question_index])

        # draw completed guesses
        for i in range(1, guess_index):
            self.draw_guess(i, self.guesses[i - 1].text, self.guesses[i - 1].score)

        # draw current step of the last guess
        match self.current_step % const.GUESS_STEPS:
            case 0:
                self.draw_guess(guess_index)
            case 1:
                self.draw_guess(guess_index, self.guesses[guess_index - 1].text)
            case 2:
                self.draw_guess(guess_index, self.guesses[guess_index - 1].text, self.guesses[guess_index - 1].score)

        # draw placeholders for remaining guesses
        if guess_index < (const.GUESS_COLS * const.GUESS_ROWS):
            for i in range(guess_index + 1, 11):
                self.draw_guess(i)

    def toggle_guesses(self):
        """Toggle the visibility of the guesses."""

        self.show_guesses = not self.show_guesses

        if self.show_guesses:
            self.draw_guesses()

        else:
            self.draw_question('Fast Money')

            # hide already guessed guesses
            guess_index = (self.current_step // const.GUESS_STEPS) + 1
            for i in range(1, guess_index + 1):
                self.draw_guess(i)

    def draw_guess(self, index: int, text: str = None, score: int = None, show_animation: bool = False) -> None:
        """
        Draw the specified guess.

        @param index: The index of the guess to draw (1 to 10).
        @param text: The guess to be displayed.
        @param score: The score for the guess.
        @param show_animation: Whether to show the animation or not.
        """

        # determine location of guess based on index
        x = const.GUESS_X + (((index - 1) // const.GUESS_ROWS) * (const.GUESS_WIDTH + 1))
        y = const.GUESS_Y + (((index - 1) % const.GUESS_ROWS) * const.GUESS_HEIGHT)

        print(term.bright_blue, end='')
        print(term.move_xy(x, y + 0) + ' ┌──────────────────┬────┐ ', end='')
        print(term.move_xy(x, y + 1) + ' │                  │    │ ', end='')
        print(term.move_xy(x, y + 2) + ' └──────────────────┴────┘ ', end='')
        print(term.bright_white, end='')

        if text is not None:
            max_guess_length = const.GUESS_WIDTH - 9
            if text and len(text) > max_guess_length:
                text = text[0:max_guess_length-1] + '…'

            # draw guess with animation
            if score is None and show_animation:
                text = text.upper()
                print(term.move_xy(x + 3, y + 1), end='')

                for i in range(0, max_guess_length):
                    char = text[i] if i < len(text) else ' '
                    print(char + '█' + term.move_left, end='', flush=True)
                    time.sleep(const.GUESS_DELAY)

                print(' ', end='', flush=True)
                time.sleep(const.GUESS_DELAY * 3)

            # draw guess without animation
            else:
                print(term.move_xy(x + 3, y + 1) + text.upper().ljust(max_guess_length) + ' ', end='')

            print(term.move_right(2) + '██', end='', flush=True)

        # draw score for guess
        if score is not None:
            print(term.move_xy(x + (const.ANSWER_WIDTH - 3), y + 1) + str(score).rjust(2), end='')

        print(term.normal, end='', flush=True)

    def draw_score(self):
        """Draws the round score."""

        guess_index = (self.current_step // const.GUESS_STEPS)
        if (self.current_step % const.GUESS_STEPS) == 2:
            guess_index += 1

        score = 0
        for i in range(0, guess_index):
            score += self.guesses[i].score

        self.score.draw(score)

    def step_forward(self) -> None:
        """Step forward through the round, one step at a time."""

        max_steps = const.GUESS_ROWS * const.GUESS_COLS * const.GUESS_STEPS
        self.current_step += 1 if self.current_step < (max_steps - 1) else 0
        self.draw_step()

    def step_backward(self) -> None:
        """Step backward through the round, one step at a time."""

        self.current_step -= 1 if self.current_step > 0 else 0

        # step back one question (not one step) at a time
        self.current_step = (self.current_step // const.GUESS_STEPS) * const.GUESS_STEPS
        self.draw_step()

    def draw_step(self):
        """Draw the current step."""

        guess_text = self.guesses[self.current_step // const.GUESS_STEPS].text
        guess_score = self.guesses[self.current_step // const.GUESS_STEPS].score

        question_index = (self.current_step // const.GUESS_STEPS) % 5
        guess_index = (self.current_step // const.GUESS_STEPS) + 1

        match self.current_step % const.GUESS_STEPS:
            case 0:
                self.draw_question(self.questions[question_index])
                self.draw_guess(guess_index)
            case 1:
                self.draw_guess(guess_index, guess_text, show_animation=True)
            case 2:
                self.draw_guess(guess_index, guess_text, guess_score)

        self.draw_score()
