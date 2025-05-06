import blessed
import yaml

import constants as const
from round import Round
from fast_round import FastRound
from answer import Answer
from guess import Guess
from screens import Screens
from font import Font
from score import Score


term = blessed.Terminal()


class Game:
    """
    Game

    @param current_round: The current round number.
    @param current_screen: The current game screen.
    @param team_a_score:  The score for team A.
    @param team_b_score: The score for team B.
    @param rounds: A list of Round objects.
    """

    def __init__(self) -> None:
        self.current_round: int = 0
        self.current_screen: Screens = Screens.GAME_TITLE_SCREEN
        self.team_a_score: Score = Score(const.TEAM_A_SCORE_X, const.TEAM_A_SCORE_Y, score=0)
        self.team_b_score: Score = Score(const.TEAM_B_SCORE_X, const.TEAM_B_SCORE_Y, score=0)
        self.rounds: list[Round] = [Round(), Round(), Round(), FastRound()]

    def load(self) -> None:
        """Loads the game data from game.yaml."""

        with open('game.yaml', 'r', encoding='utf8') as f:
            data = yaml.load(f, Loader=yaml.SafeLoader)

        # add loaded data to regular rounds

        for round_index in range(0, 3):
            self.rounds[round_index].round_number = data['rounds'][round_index]['round']
            self.rounds[round_index].multiplier = data['rounds'][round_index]['multiplier']
            self.rounds[round_index].question = data['rounds'][round_index]['question']

            self.rounds[round_index].answers.clear()
            for answer in data['rounds'][round_index]['answers']:
                self.rounds[round_index].answers.append(Answer(answer['answer'], answer['score']))

            for i in range(len(data['rounds'][round_index]['answers']), 8):
                if i in self.rounds[round_index].answered:
                    self.rounds[round_index].answered.remove(i)

        # add loaded data to fast round

        round_index += 1

        self.rounds[round_index].questions.clear()
        for question in data['rounds'][round_index]['questions']:
            self.rounds[round_index].questions.append(question['question'])

        self.rounds[round_index].guesses.clear()
        for guess in data['rounds'][round_index]['guesses']:
            self.rounds[round_index].guesses.append(Guess(guess['guess'], guess['score']))

    def draw_title_screen(self) -> None:
        """Draws the title screen."""

        print(term.home + term.clear, end='')
        x = Font.print(const.GAME_TITLE_LINE1_X, const.GAME_TITLE_LINE1_Y, 'TERMINAL')
        Font.print(const.GAME_TITLE_LINE2_X, const.GAME_TITLE_LINE2_Y, 'FEUD')
        print(term.normal, end='', flush=True)

    def draw_screen(self, screen: Screens) -> None:
        """
        Draws the specified screen.

        screen: The screen to be drawn.
        """

        match screen:

            case Screens.GAME_TITLE_SCREEN:
                self.draw_title_screen()

            case Screens.ROUND_1_TITLE_SCREEN:
                self.current_round = 1
                self.rounds[self.current_round-1].draw_title_screen()

            case Screens.ROUND_1_GAME_SCREEN:
                self.current_round = 1
                self.rounds[self.current_round-1].draw_game_screen()
                self.team_a_score.draw()
                self.team_b_score.draw()

            case Screens.ROUND_2_TITLE_SCREEN:
                self.current_round = 2
                self.rounds[self.current_round-1].draw_title_screen()

            case Screens.ROUND_2_GAME_SCREEN:
                self.current_round = 2
                self.rounds[self.current_round-1].draw_game_screen()
                self.team_a_score.draw()
                self.team_b_score.draw()

            case Screens.ROUND_3_TITLE_SCREEN:
                self.current_round = 3
                self.rounds[self.current_round-1].draw_title_screen()

            case Screens.ROUND_3_GAME_SCREEN:
                self.current_round = 3
                self.rounds[self.current_round-1].draw_game_screen()
                self.team_a_score.draw()
                self.team_b_score.draw()

            case Screens.FASTROUND_TITLE_SCREEN:
                self.current_round = 4
                self.rounds[self.current_round-1].draw_title_screen()

            case Screens.FASTROUND_GAME_SCREEN:
                self.current_round = 4
                self.rounds[self.current_round-1].draw_game_screen()

    def update_team_scores(self) -> None:
        """Updates team scores."""

        team_a_score = 0
        team_b_score = 0

        for round in self.rounds:
            if round.winner == 'A':
                team_a_score += round.score.score
            elif round.winner == 'B':
                team_b_score += round.score.score

        self.team_a_score.draw(team_a_score)
        self.team_b_score.draw(team_b_score)

    def loop(self) -> None:
        """The game loop."""

        with term.fullscreen(), term.cbreak(), term.hidden_cursor():
            self.draw_title_screen()

            key: str = None
            while key != 'q':
                key = term.inkey()

                match key:

                    # load/reload game data
                    case 'l':
                        self.load()
                        self.draw_screen(self.current_screen)

                    # goto next round/screen
                    case 'r':
                        self.current_screen = self.current_screen.next()
                        self.draw_screen(self.current_screen)

                    # goto previous round/screen
                    case 'R':
                        self.current_screen = self.current_screen.prev()
                        self.draw_screen(self.current_screen)

                # regular rounds
                if self.current_screen in [
                    Screens.ROUND_1_GAME_SCREEN,
                    Screens.ROUND_2_GAME_SCREEN,
                    Screens.ROUND_3_GAME_SCREEN,
                ]:
                    match key:

                        # toggle respective answers
                        case '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8':
                            if int(key) <= len(self.rounds[self.current_round-1].answers):
                                self.rounds[self.current_round-1].toggle_answer(int(key))

                        # show remaining answers
                        case '9':
                            self.rounds[self.current_round-1].show_remaining_answers()

                        # hide all answers
                        case '0':
                            self.rounds[self.current_round-1].hide_all_answers()

                        # increment and show x
                        case 'x':
                            self.rounds[self.current_round-1].show_x()

                        # decrement x count
                        case 'X':
                            self.rounds[self.current_round-1].remove_x()

                        # toggle team A as the winner for this round
                        case 'a':
                            self.rounds[self.current_round-1].toggle_winner_team_a()
                            self.update_team_scores()

                        # toggle team B as the winner for this round
                        case 'b':
                            self.rounds[self.current_round-1].toggle_winner_team_b()
                            self.update_team_scores()

                # fast money round
                if self.current_screen == Screens.FASTROUND_GAME_SCREEN:
                    match key:

                        # step through fast money round
                        case 'f':
                            self.rounds[self.current_round-1].step_forward()

                        # step through fast money round in reverse
                        case 'F':
                            self.rounds[self.current_round-1].step_backward()

                        # show/hide guesses
                        case 'm':
                            self.rounds[self.current_round-1].toggle_guesses()
