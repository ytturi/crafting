# -*- encoding utf-8 -*-
import logging


_TASK_HELP = ['h', 'help', 'options', 'tasks']
_TASK_INFO = ['i', 'info']
_TASK_SHOW_STOCK = ['a', 'amount']
_TASK_UPD_PROD = ['m', 'manual-update', 'mod']
_TASK_UPD_STOCK = ['u', 'update']
_TASK_SHOW_RECIPE = ['r', 'recipe', 'required', 'requirements']
_TASK_SHOW_CRAFT = ['c', 'craft', 'check']
_TASK_SHOW_RECURSIVE = ['rc', 'rcraft', 'rcheck',
                    'recursive-craft', 'recursive-check']
_TASK_EXIT = ['e', 'exit']
_TASKS = [
    (_TASK_HELP, 'Print all available tasks', ''),
    (_TASK_INFO, 'Show more info about a task', '<task>'),
    (_TASK_SHOW_STOCK, 'Show the current amount of a PRODUCT', '<product>'),
    (_TASK_UPD_PROD,
     'Manual Update current amount of a PRODUCT',
     '<product> <int>'),
    (_TASK_UPD_STOCK,
     'Update the current amount of all PRODUCTs from a FILE',
     '<file>'),
    (_TASK_SHOW_RECIPE, 'Show the requirements of a RECIPE', '<recipe>'),
    (_TASK_SHOW_CRAFT, 'Show the PRODUCTS collected for a RECIPE', '<recipe>'),
    (_TASK_SHOW_RECURSIVE,
     'Show the recursive requirementts collected of a RECIPE',
     '<recipe>'),
    (_TASK_EXIT, 'Exit the Craft Manager', '')
]

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
        colored_info = self.color_string(
            'red', 'CRITICAL: {text}'.format(**locals())
        )
        text = '{colored_info}'.format(**locals())
        self.logger.debug(text)

    @staticmethod
    def color_string(colour, text):
        if colour in _AVAILABLE_COLORS:
            return '{}{}{}'.format(
                COLORS[colour], text, COLORS['reset']
            )
        else:
            return text

    def print_menu(self):
        msg = 'Available Tasks:\n'
        for words, description, args in _TASKS:
            msg += '>[{0}]{1}\n\t{0} {2}\n'.format(words[1], description, args)
        self.info(msg)
    
    def print_actions(self):
        msg = '\nActions:\n'
        for action, description in _ACTIONS:
            msg += '\t{}\t{}\n'.format(action, description)
        self.info(msg)

