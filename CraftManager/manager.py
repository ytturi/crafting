# -*- encoding utf-8 -*-
import logging

_RES_OK = 0
_RES_WARN = 1
_RES_ERR = 2
_RES_CRIT = 3
_RES_EXIT = 51 # ExIT -> 3x17 => 51

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


def color_string(colour, text):
    if colour in _AVAILABLE_COLORS:
        return '{}{}{}'.format(
            COLORS[colour], text, COLORS['reset']
        )
    else:
        return text


class CraftManager:
    def __init__(self, logger):
        self.logger = logger

    # Log utilities
    def msg(self, text):
        text = '> {text}'.format(**locals())
        self.logger.info(text)

    def info(self, text):
        colored_info = color_string('green', 'INFO')
        text = '{colored_info}: {text}'.format(**locals())
        self.logger.info(text)

    def debug(self, text):
        colored_info = color_string(
            'blue', 'DEBUG: {text}'.format(**locals())
        )
        text = '{colored_info}'.format(**locals())
        self.logger.debug(text)

    def warn(self, text):
        colored_info = color_string('yellow', 'WARNING')
        text = '{colored_info}: {text}'.format(**locals())
        self.logger.warning(text)

    def error(self, text):
        colored_info = color_string('red', 'ERROR')
        text = '{colored_info}: {text}'.format(**locals())
        self.logger.error(text)

    def critical(self, text):
        colored_info = color_string(
            'red', 'CRITICAL: {text}'.format(**locals())
        )
        text = '{colored_info}'.format(**locals())
        self.logger.debug(text)

    # Prompts and messages
    def print_menu(self):
        msg = 'Available Tasks:\n'
        for words, description, args in _TASKS:
            tag = color_string('yellow', words[1])
            msg += '>[{0}]{1}\n\t{0} {2}\n'.format(tag, description, args)
        self.info(msg)
    
    def print_actions(self):
        msg = '\nActions:\n'
        for action, description in _ACTIONS:
            msg += '\t{}\t{}\n'.format(action, description)
        self.info(msg)

    # Task processing
    def valid_taskname(self, taskname):
        for tags, descr, args in _TASKS:
            if taskname.lower() in tags:
                return True
        return False

    def run_task(self, task_name):
        if not task_name:
            self.error('No task name or tag provided')
            return self.task_error
        elif not self.valid_taskname(task_name):
            self.error('Task "{}" does not exist'.format(task_name))
            return self.task_error
        self.debug('Running task "{}"'.format(task_name))
        if task_name == _TASK_HELP:
            return self.print_menu
        elif task_name == _TASK_EXIT:
            return self.task_exit
        else:
            return self.task_not_implemented
     
    def task_error(self, taskname, args):
        self.debug(
            'Default error for TASK: [{taskname}|{args}]'.format(**locals())
        )
        return _RES_ERR

    def task_not_implemented(self, taskname, args):
        self.warn('Task not implemented yet!')
        return _RES_WARN

    def task_exit(self, taskname, args):
        self.debug('Exiting manager')
        return _RES_EXIT