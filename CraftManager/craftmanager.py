# -*- encoding utf-8 -*-
from tqdm import tqdm
from CraftManager.utils import CraftUtils
from CraftManager.utils import _ACT_INTERACTIVE
import click
import logging


def start_interactive():
    utils.debug('Starting Menu display')
    utils.print_menu()


@click.command()
@click.argument('action', default=False)
@click.option('--debug/--no-debug', 'debug_mode', flag_value=True, 
              default=False, help='Enable debug prints')
@click.option('--date/--no-date', 'show_date', flag_value=True, 
              default=False, help='Enable date on prints')
def craftmanager(action, debug_mode, show_date):
    log_level = (0 if debug_mode else 20)
    log_format = "%(message)s"
    if show_date:
        log_format = '[%(asctime)s] - {}'.format(log_format)
    logging.basicConfig(
        format=log_format,
        datefmt="%Y-%m-%d %H:%M:%S", level=log_level
    )
    logger = logging.getLogger(__name__)
    global utils
    utils = CraftUtils(logger)
    utils.debug(
        'INIT STATS:\n'    
        'ACTION: \t"{action}"\n'
        'LOGGER:\n'
        '|  log_level:\t{log_level}\n'
        '|  log_format:\t"{log_format}"'
        ''.format(
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
    craftmanager()

