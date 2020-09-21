# Copyright © {% now 'local', '%Y' %} {{cookiecutter.team_name}}. All rights reserved.
# =========================================================================== #
# PROGRAM: Makefile
# AUTHORS: {{cookiecutter.lead_name}}
# CREATED: {{strftime('%d%b%Y', now)|upper}}
# REVISED: {{strftime('%d%b%Y', now)|upper}}
# =========================================================================== #


# =========================================================================== #
# EXTERNAL CONSTANTS
# =========================================================================== #


# -- Filesystem -- #

# Name of the main makefile.
MAKEFILE = $(firstword $(MAKEFILE_LIST))

# Absolute path of the directory containing the main makefile.
MAKEFILE_DIR ?= $(dir $(realpath $(MAKEFILE)))

# Path of the directory containing secondary makefiles.
MAKE_DIR ?= $(MAKEFILE_DIR).make


# ============================================================================ #
# PHONY TARGETS
# ============================================================================ #


# -- Main Targets -- #

.PHONY: all clean init test

all: help


# ============================================================================ #
# FILE TARGETS
# ============================================================================ #


# =========================================================================== #
# FEATURE DEPENDENCIES
# =========================================================================== #


include $(MAKE_DIR)/features/___FEATURE___.mk


# ============================================================================ #
# PLATFORM DEPENDENCIES
# ============================================================================ #


include $(MAKE_DIR)/platforms/___PLATFORM___.mk
