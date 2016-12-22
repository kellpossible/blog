#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Luke Frisken'
SITENAME = 'Luke Frisken'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 15

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images', 'thumbnailer', 'files']


PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = [
	'photos',
	'pelican_vimeo'
	]

THEME = 'themes/lukefrisken'

# Gallery

PHOTO_LIBRARY = "./content/photos"
PHOTO_GALLERY = (2000, 2000, 80)
PHOTO_ARTICLE = ( 1024, 768, 80)
PHOTO_THUMB = (192, 144, 60)
PHOTO_RESIZE_JOBS = 5
PHOTO_WATERMARK = False
PHOTO_WATERMARK_TEXT = "Copyright Luke Frisken"
PHOTO_WATERMARK_IMG = ''

# Better Figures and Images

RESPONSIVE_IMAGES = True

# Disqus

DISQUS_SITENAME = "lukefrisken"