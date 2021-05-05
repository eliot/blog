#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Elliott'
SITENAME = 'Elliott Chenoweth'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_DATE_FORMAT = '%B %-d, %Y'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

THEME = 'basic-theme' # folder in project root

#THEME_STATIC_DIR = ''

# MD_EXTENSIONS = ['codehilite(css_class=code)','extra']
# MD_EXTENSIONS = ['fenced_code(css_class=code)','extra']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True