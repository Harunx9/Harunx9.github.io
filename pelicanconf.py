#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Szymon Wanot'
SITENAME = u'Programming warfare'
SITEURL = u'https://harunx9.github.io'
#SITEURL = u'http://localhost:8000'
SITELOGO = "/images/avatar.jpg"
PATH = 'content'

TIMEZONE = 'Europe/Warsaw'

DEFAULT_LANG = u'pl'

THEME = u"Flex"
DISQUS_SITENAME = "programmingwarfare"

GOOGLE_ANALYTICS = "UA-85776912-1"
STATIC_PATHS = ['images']
# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ATOM = 'feeds/feeds.atom.xml'
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
FEED_RSS = 'feeds/feeds.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
TAG_FEED_RSS = 'feeds/%stag.rss.xml'
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

JINJA_ENVIRONMENT = {
}

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
