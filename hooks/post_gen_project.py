#!/usr/bin/env python
import os
import sys


# =========================================================================== #
# METADATA
# =========================================================================== #

__author__ = 'Robert (Bob) L. Jones'
__credits__ = ['Robert (Bob) L. Jones']

__copyright__ = 'Copyright 2020, Cookiecutter Make'
__license__ = 'MIT'

__created_date__ = 'Sep 15, 2020'
__modified_date__ = 'Sep 19, 2020'


# =========================================================================== #
# CONSTANTS
# =========================================================================== #

# -- Debugging -- #

DEBUG = True


# =========================================================================== #
# FUNCTIONS
# =========================================================================== #

# -- Shell -- #

def cmd(*args):
    os.system(' '.join(args))


def mv(*args):
    cmd('mv', *args)


def rm(*args):
    cmd('rm -rf', *args)


def rename():
    cmd1 = 'for f in $(find . -type f -name "*.jinja2")'
    cmd2 = 'do mv -- "$f" "${f%.jinja2}"'
    cmd3 = 'done'
    cmd(cmd1, ';', cmd2, ';', cmd3)


# -- Main Program -- #

def main():
    """
    Run the main set of functions that define the program.
    """

    print('DEBUG =', DEBUG)

    mv('.boilerplate/Cookiecutter/*', '.')
    rm('.boilerplate')
    rm('template.*.jinja2')
    rename()


# =========================================================================== #
# MAIN EXECUTION
# =========================================================================== #

# -- Main Execution -- #

# If this module is in the main module, call the main() function.
if __name__ == '__main__':
    main()

# -- Housekeeping -- #

# Exit the program normally.
sys.exit(0)
