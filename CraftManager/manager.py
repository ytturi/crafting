# -*- encoding utf-8 -*-
from collections import namedtuple
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


_MODEL_PRODUCT = namedtuple(
    'product_obj', [
        'self_id', 'name', 'stock', 'recipe_id'
    ]
)
_MODEL_RECIPE = namedtuple(
    'recipe_obj', [
        'self_id', 'result_id',
        'requirement_id_1', 'requirement_amount_1',
        'requirement_id_2', 'requirement_amount_2',
        'requirement_id_3', 'requirement_amount_3',
        'requirement_id_4', 'requirement_amount_4',
    ]
)


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

    # Database methods
    def get_recipe(self, recipe_id):
        """
        Returns a named tuple with the data of a recipe
        NamedTuple _MODEL_RECIPE:
            self_id:              INT
            result_id:            INT
            requirement_id_1:     INT
            requirement_amount_1: INT
            requirement_id_2:     INT
            requirement_amount_2: INT
            requirement_id_3:     INT
            requirement_amount_3: INT
            requirement_id_4:     INT
            requirement_amount_4: INT
        """
        try:
            recipe_id = int(recipe_id)
        except ValueError:
            self.error('Trying to get RECIPE without ID')
            return False
        #TODO: get RECIPE from database using psycopg2
        recipe_obj = _MODEL_RECIPE(
            self_id=0, result_id=0, requirement_id_1=0, requirement_amount_1=0,
            requirement_id_2=0, requirement_amount_2=0, requirement_id_3=0,
            requirement_amount_3=0, requirement_id_4=0, requirement_amount_4=0
        )
        return recipe_obj
        
    def get_product(self, product_name=False, product_id=False):
        """
        Returns a named tuple with the data of a product
        NamedTuple _MODEL_PRODUCT:
            self_id:   INT
            name:      STR
            stock:     INT
            recipe_id: INT
        """
        if not product_name and not product_id:
            self.error("Can't look for a PRODUCT without NAME or ID")
            return False
        self.debug('Getting PRODUCT "{}" from database'
                   ''.format(product_name or product_id))
        #TODO: get PRODUCT from database using psycopg2
        prod_obj = _MODEL_PRODUCT(self_id=0, name='demo', stock=0, recipe_id=0)
        return prod_obj

    def write_product(self, product_obj):
        """
        Writes a PRODUCT in the DATABASE
        - PRODUCT must exist with the same ID
        :product_obj: The PRODUCT to UPDATE
            :type: _MODEL_PRODUCT
        :returns: 0 if WRITE, -1 if ERROR
        """
        if not isinstance(product_obj, _MODEL_PRODUCT):
            self.error('Trying to WRITE on PRODUCT without a MODEL_PRODUCT')
            return -1
        #TODO: update PRODUCT on database using psycopg2 and product_obj
        return 0

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
        if task_name in _TASK_HELP:
            return self.task_print_menu
        elif task_name in _TASK_INFO:
            return self.task_info
        elif task_name in _TASK_SHOW_STOCK:
            return self.task_stock
        elif task_name in _TASK_UPD_PROD:
            return self.task_single_update
        elif task_name in _TASK_EXIT:
            return self.task_exit
        else:
            return self.task_not_implemented

    def task_print_menu(self, taskname, args):
        self.print_menu()
        return _RES_OK

    def task_info(self, taskname, args):
        if not args:
            self.error('No task provided to get more info')
            return _RES_ERR
        task = args[0]
        for words, descr, pars in _TASKS:
            if task in words:
                str_pars = '\n'.join(
                    ['\t{word} {pars}'.format(**locals()) for word in words]
                )
                self.info(
                    '{descr}\nAvailable tags:\n'
                    '{str_pars}'.format(**locals())
                )
                return _RES_OK
        self.warn('Task {task} not found to get info'.format(**locals()))
        return _RES_WARN

    def task_stock(self, taskname, args):
        if not args:
            self.error('No <product name> provided to check amount')
            return _RES_ERR
        product = ' '.join(args)  # Concat product name
        self.debug('Getting amount of product "{product}"'.format(**locals()))
        prod_obj = self.get_product(product_name=product)
        if prod_obj is None or not prod_obj:
            self.error('Could not find "{product}" on database')
            return _RES_ERR
        amount = prod_obj.stock
        colored_name = color_string('yellow', product)
        self.info('{colored_name}:\t{amount}'.format(**locals()))
        return _RES_OK

    def task_single_update(self, taskname, args):
        if not args or len(args) < 2:
            self.error('No <product name> or <amount> provided to update amount')
            return _RES_ERR
        product = ' '.join(args[:1])  # Concat product name
        try:
            amount = int(args[-1])
        except ValueError:
            self.error('Amount to update PRODUCT not sepecified as INTEGER')
            return _RES_ERR
        self.debug('Getting product "{product}" to update amount with {amount}'
                   ''.format(**locals()))
        prod_obj = self.get_product(product_name=product)
        if prod_obj is None or not prod_obj:
            self.error('Could not find "{product}" on database'
                       ''.format(**locals()))
            return _RES_ERR
        old_amount = prod_obj.stock
        self.debug('Updating stock amount {old_amount} -> {amount}'
                   ''.format(**locals()))
        prod_obj = prod_obj._replace(stock = amount)
        if self.write_product(prod_obj):
            self.error('Failed on write of {product} in database'
                       ''.format(**locals()))
            return _RES_ERR
        self.info('Updated "{prod_obj.name}" stock {old_amount} -> {prod_obj.stock}'
                  ''.format(**locals()))
        return _RES_OK

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
