#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Szymon Wanot'
SITENAME = u'Programming warfare'
SITEURL = u'https://harunx9.github.io'

PATH = 'content'

TIMEZONE = 'Europe/Warsaw'

DEFAULT_LANG = u'pl'

THEME = u"pelican-blueidea"

DISQUS_SITENAME = "programmingwarfare"

GOOGLE_ANALYTICS = "UA-85776912-1"

STATIC_PATHS = ['images']
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget

SOCIAL = (('github', 'https://github.com/Harunx9'),
          ('linkedin', 'https://pl.linkedin.com/in/szymon-wanot-b0a146ab'),
          ('twitter', 'https://twitter.com/szwanot'),
          ('facebook', 'https://www.facebook.com/szymon.wanot'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
