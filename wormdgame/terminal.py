import os
import sys
import colorama

colorama.init()


class Terminal:
    @staticmethod
    def clear_terminal():
        os.system('clear' if sys.platform.startswith('linux') or sys.platform.startswith('darwin') else 'cls')

    @staticmethod
    def print_with_color(msg, color):
        print(colorama.Fore.__getattribute__(str(color).upper) + msg + colorama.Fore.RESET)
