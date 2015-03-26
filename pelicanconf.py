#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Martin Thoma'
SITENAME = u'Python lernen - Spiel f\xfcr Spiel'
SITEURL = 'http://www.martin-thoma.de/python-lernen'

THEME = "/home/moose/pelican-themes/blueidea"
DISPLAY_AUTHOR_ON_POSTINFO = True

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = u'de'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

SLUGIFY_SOURCE = 'title'
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

# Blogroll
LINKS = (('martin-thoma.com', 'http://martin-thoma.com/'),
         ('Python.org', 'https://docs.python.org/3/library/functions.html'),
         ('StackOverflow', 'http://stackoverflow.com/'))

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/themoosemind'),
          ('github', 'https://github.com/MartinThoma'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
