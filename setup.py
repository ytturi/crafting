#!/usr/bin/env python

from setuptools import setup

setup(name='CraftManager',
    version='1.0',
    description='Python Manager for crafting utilities',
    author='Ytturi',
    author_email='ytturi@gmail.com',
    packages=['CraftManager'],
    install_requires=[
        'click', 'tqdm'
    ]
)
