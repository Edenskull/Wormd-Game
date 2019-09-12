import sys
from wormdgame.wordapi import WordApi
from wormdgame.terminal import Terminal
from wormdgame.core import TurnManager


def run():
    Terminal.print_with_color('Welcome to the jungle', 'blue')
    Terminal.print_with_color('The aim of this game is to type fast. Ready ? (press enter)', 'blue')
    input()
    tmanager = TurnManager()
    Terminal.clear_terminal()
    token = WordApi.get_api_key()
    while True:
        Terminal.print_with_color('Niveau {}'.format(tmanager.overall), 'yellow')
        try:
            basic_timer = 5 - (tmanager.overall / 10)
            if 1 <= tmanager.turn <= 3:
                word_to_find = WordApi.get_random_word(token, 1)
            elif 4 <= tmanager.turn <= 6:
                word_to_find = WordApi.get_random_word(token, 2)
            elif 7 <= tmanager.turn <= 9:
                word_to_find = WordApi.get_random_word(token, 3)
            basic_timer = basic_timer * len(word_to_find)
            Terminal.print_with_color('You have {} secondes'.format(basic_timer), 'green')
            success = WordApi.compare_words(word_to_find, basic_timer)
            if not success:
                Terminal.print_with_color('This is the wrong word.', 'red')
                Terminal.print_with_color('You lost the game, please press enter to leave.', 'blue')
                input()
                sys.exit(123)
            else:
                tmanager.add_turn()
        except TimeoutError:
            Terminal.print_with_color('\nTimes up! You are too slow.', 'red')
            Terminal.print_with_color('You lost the game, please press enter to leave.', 'blue')
            input()
            sys.exit(123)


if __name__ == '__main__':
    run()
