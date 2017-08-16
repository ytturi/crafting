# -*- encoding utf-8 -*-
import logging


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


class CraftUtils:
    def __init__(self, logger):
        self.logger = logger

    def msg(self, text):
        text = '> {text}'.format(**locals())
        self.logger.info(text)

    def info(self, text):
        colored_info = self.color_string('green', 'INFO')
        text = '{colored_info}: {text}'.format(**locals())
        self.logger.info(text)

    def debug(self, text):
        colored_info = self.color_string(
            'blue', 'DEBUG: {text}'.format(**locals())
        )
        text = '{colored_info}'.format(**locals())
        self.logger.debug(text)

    def warn(self, text):
        colored_info = self.color_string('yellow', 'WARNING')
        text = '{colored_info}: {text}'.format(**locals())
        self.logger.warning(text)

    def error(self, text):
        colored_info = self.color_string('red', 'ERROR')
        text = '{colored_info}: {text}'.format(**locals())
        self.logger.error(text)

    def critical(self, text):
        colored_info = self.color_string('red', 'CRITICAL')
        text = '{colored_info}: {text}'.format(**locals())
        self.logger.critical(text)

    @staticmethod
    def color_string(colour, text):
        if colour in _AVAILABLE_COLORS:
            return '{}{}{}'.format(
                COLORS[colour], text, COLORS['reset']
            )
        else:
            return text

    def print_menu(self):
        self.msg('Hi!')
    
    def print_actions(self):
        msg = '\nActions:\n'
        for action, description in _ACTIONS:
            msg += '\t{}\t{}\n'.format(action, description)
        self.info(msg)

