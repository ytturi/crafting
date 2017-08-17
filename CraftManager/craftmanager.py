# -*- encoding utf-8 -*-
from __future__ import unicode_literals
from CraftManager.utils import CraftUtils
from CraftManager.utils import _ACT_INTERACTIVE
from CraftManager.utils import _TASK_HELP, _TASK_EXIT
from tqdm import tqdm
import click
import logging


def read_configs(config_path):
    utils.warn('Not implemented yet!')
    return {
        'db-host': 'localhost',
        'db-port': 5432,
        'db-user': 'test',
        'db-pass': 'test',
        'db-name': 'test',
    }


def start_interactive():
    utils.debug('Starting Menu display')
    utils.print_menu()
    exit = False
    try:
        while not exit:
            action = click.prompt('CRAFT-MANAGER:>').lower()
            task = action.split()[0]
            utils.debug('Input: "{action}"; Task: "{task}"'.format(**locals()))
            if task in _TASK_HELP:
                utils.print_menu()
            elif task in _TASK_EXIT:
                exit = True
            else:
                utils.error('Unknown TASK {task}'.format(**locals()))
    finally:
        utils.msg(u'Thank you for using me! \U0001f604')


@click.command()
@click.argument('action', default=False)
@click.option('--debug/--no-debug', 'debug_mode', flag_value=True, 
              default=False, help='Enable debug prints')
@click.option('--date/--no-date', 'show_date', flag_value=True, 
              default=False, help='Enable date on prints')
@click.option('--config', 'config_path', default='craftmanager.conf',
              help=('Path for the config file.'
                    'If not found it is created using default values'))
def craftmanager(action, debug_mode, show_date, config_path):
    log_level = (0 if debug_mode else 20)
    log_format = '%(message)s'
    if show_date:
        log_format = '[%(asctime)s] - {}'.format(log_format)
    logging.basicConfig(
        format=log_format,
        datefmt="%Y-%m-%d %H:%M:%S", level=log_level
    )
    logger = logging.getLogger(__name__)
    global utils
    utils = CraftUtils(logger)
    configs = read_configs(config_path)
    dbname = configs['db-name']
    dbhost = configs['db-host']
    dbport = configs['db-port']
    dbuser = configs['db-user']
    dbpass = configs['db-pass']
    utils.debug(
        'INIT STATS:\n'    
        'ACTION: \t"{action}"\n'
        'LOGGER:\n'
        '|  log_level:\t{log_level}\n'
        '|  log_format:\t"{log_format}"\n'
        'CONFIG_FILE: \t"{config_path}"\n'
        '|  db-name:\t{dbname}\n'
        '|  db-host:\t{dbhost}\n'
        '|  db-port:\t{dbport}\n'
        '|  db-user:\t{dbuser}\n'
        '|  db-pass:\t{dbpass}\n'
        '<----INIT STATS---->'.format(
            **locals()
        )
    )
    if action == _ACT_INTERACTIVE:
        start_interactive()
    else:
        if action:
            utils.warn(
                'Action {} Not implemented yet!'.format(action)
            )
        utils.error('No action provided!')
        utils.print_actions()

if __name__=='__main__':
    import sys
    # sys.setdefaultencoding() does not exist, here!
    reload(sys)  # Reload does the trick!
    sys.setdefaultencoding('UTF8')
    craftmanager()

