# -*- encoding utf-8 -*-
from tqdm import tqdm
from CraftManager.utils import print_menu, print_actions
from CraftManager.utils import _ACT_INTERACTIVE
import click


def start_interactive():
    print_menu()


@click.command()
@click.argument('action', default=False)
def craftmanager(action):
    if action == _ACT_INTERACTIVE:
        start_interactive()
    else:
        if action:
            print('Not implemented yet!')
        with click.Context(craftmanager) as ctx:
            click.echo(craftmanager.get_help(ctx))
        print_actions()

if __name__=='__main__':
    craftmanager()

