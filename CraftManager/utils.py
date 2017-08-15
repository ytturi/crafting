# -*- encoding utf-8 -*-

_ACT_INTERACTIVE = 'interactive'

_ACTIONS = [
     (_ACT_INTERACTIVE, 'Run manager interactively')
]


_AVAILABLE_COLORS = [
    'black', 'red', 'green', 'yellow',
    'blue', 'purple', 'cian', 'white'
]

COLORS = {
    'black': '\033[00;30m',
    'red': '\033[00;31m',
    'green': '\033[00;32m',
    'yellow': '\033[00;33m',
    'blue': '\033[00;34m',
    'purple': '\033[00;35m',
    'cian': '\033[00;36m',
    'white': '\033[00;37m',
    'reset': '\033[00m'
}


def color_string(colour, text):
    if colour in _AVAILABLE_COLORS:
        return '{}{}{}'.format(
            COLORS[colour], text, COLORS['reset']
        )
    else:
        return text


def print_menu():
    print('Hi!')


def print_actions():
    print('\nActions:')
    for action, description in _ACTIONS:
        print('\t{}\t{}'.format(action, description))

