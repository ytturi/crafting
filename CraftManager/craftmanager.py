# -*- encoding utf-8 -*-
from __future__ import unicode_literals
from CraftManager.manager import CraftManager
from CraftManager.manager import _ACT_INTERACTIVE
from CraftManager.manager import _TASK_HELP, _TASK_EXIT
from CraftManager.manager import _RES_OK, _RES_WARN, _RES_ERR
from CraftManager.manager import _RES_CRIT, _RES_EXIT
from tqdm import tqdm
import click
import logging


def read_configs(config_path):
    manager.warn('Not implemented yet!')
    return {
        'db-host': 'localhost',
        'db-port': 5432,
        'db-user': 'test',
        'db-pass': 'test',
        'db-name': 'test',
    }


def start_interactive():
    manager.print_menu()
    res = 0
    try:
        while not res == _RES_EXIT:
            action = click.prompt('CRAFT-MANAGER:>').split()
            if not action:
                continue
            task = action[0].lower()
            if not manager.valid_taskname(task):
                manager.error('Task "{task}" does not exist!'.format(**locals()))
                continue
            method = manager.run_task(task)
            res = method(task, action[1:] or [])
    finally:
        manager.msg(u'Thank you for using me! \U0001f604')


@click.command()
@click.argument('action', default=False)
@click.option('--debug/--no-debug', 'debug_mode', flag_value=True, 
              default=False, help='Enable debug prints')
@click.option('--date/--no-date', 'show_date', flag_value=True, 
              default=False, help='Enable date on prints')
@click.option('--config', 'config_path', default='craftmanager.conf',
              help=('Path for the config file.'
                    'If not found it is created using default values'))
def initialize(action, debug_mode, show_date, config_path):
    log_level = (0 if debug_mode else 20)
    log_format = '%(message)s'
    if show_date:
        log_format = '[%(asctime)s] - {}'.format(log_format)
    logging.basicConfig(
        format=log_format,
        datefmt="%Y-%m-%d %H:%M:%S", level=log_level
    )
    logger = logging.getLogger(__name__)
    global manager
    manager = CraftManager(logger)
    configs = read_configs(config_path)
    dbname = configs['db-name']
    dbhost = configs['db-host']
    dbport = configs['db-port']
    dbuser = configs['db-user']
    dbpass = configs['db-pass']
    manager.debug(
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
            manager.warn(
                'Action {} Not implemented yet!'.format(action)
            )
        manager.error('No action provided!')
        manager.print_actions()

if __name__=='__main__':
    import sys
    # sys.setdefaultencoding() does not exist, here!
    reload(sys)  # Reload does the trick!
    sys.setdefaultencoding('UTF8')
    initialize()

