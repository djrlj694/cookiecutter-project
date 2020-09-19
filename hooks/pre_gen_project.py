#!/usr/bin/env python
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


# -- Main Program -- #


def main():
    """
    Run the main set of functions that define the program.
    """

    print('DEBUG =', DEBUG)


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
