# -*- encoding utf-8 -*-


available_colors = [
    'black', 'red', 'green', 'yellow',
    'blue', 'purple', 'cian', 'white'
]

colors = {
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


def color_string (colour, text):
    if colour in available_colors:
        return '{}{}{}'.format(
            colors[colour], text, colors['reset']
        )
    else:
        return text

