#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import sys
sys.path.append(os.curdir)

PATH = 'content'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Common Settings
MARKUP = ('md', 'ipynb')
IGNORE_FILES = [".ipynb_checkpoints"]
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup', 'i18n_subsites', 'tipue_search', 'category_custom_order']
# Theme Settings
THEME = "theme"
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}
DIRECT_TEMPLATES = ('index', 'categories', 'tags', 'search')
PADDED_SINGLE_COLUMN_STYLE=True
IPYNB_USE_METACELL=True

# Site Settings
STATIC_PATHS = os.getenv('STATIC_PATH', '').strip(',').split(',')
AUTHOR = os.getenv('AUTHOR', 'Ming Wan')
SITENAME = os.getenv('SITENAME', 'NB to Web')
SITEURL = os.getenv('SITEURL', '')
TIMEZONE = os.getenv('TIMEZONE', 'UTC')
DEFAULT_LANG = os.getenv('DEFAULT_LANG', 'en')

try:
    DEFAULT_PAGINATION = int(os.getenv('DEFAULT_PAGINATION'))
except:
    DEFAULT_PAGINATION = False

CATEGORIES_CUSTOM_ORDER = os.getenv('CATEGORIES_CUSTOM_ORDER', '').strip(',').split(',')

from config import *