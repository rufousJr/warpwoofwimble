#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#------#
# Info #
#------#

AUTHOR = 'Rufous Nightjar'
SITENAME = 'Warp-Woof-Wimble'
SITESUBTITLE = 'The Joanna Newsom Resource'
SITETAG = SITESUBTITLE
SITEURL = 'http://localhost:8000'
LOGO_PATH = 'images/ma.svg'
TIMEZONE = 'Europe/London'
DEFAULT_LANG = 'en'


#-------#
# Theme #
#-------#

THEME = 'theme/voidy-bootstrap'
CUSTOM_HTML_HEAD = 'header_favicon.html'
CUSTOM_FOOTER = 'footer.html'
#STYLESHEET_FILES = ('voidybootstrap.css')
BOOTSTRAP_STYLESHEET = 'bootstrap.min.css'
DEFAULT_PAGINATION = 5


#---------#
# Content #
#---------#

PATH = 'content'
STATIC_PATHS = ['images', 'pdfs','favicons','CNAME']
DEFAULT_DATE = 'fs'
DEFAULT_RELEASE = 'null'
DEFAULT_STATUS = 'hidden'
DEFAULT_METADATA = 	{
						'status':DEFAULT_STATUS,
						'release':DEFAULT_RELEASE
					}
MD_EXTENSIONS = ['toc','extra','admonition','smarty']
Typogrify = True
	
	
#---------#
# Sidebar #
#---------#

SIDEBAR = 'sidebar.html'
SIDEBAR_HIDE_TAGS = True	# NB tags requires the tag_cloud plugin
LINKS_TITLE = 'More cool sites'
LINKS = (
            ('Joanna Newsom lyrics',
             'http://joannanewsomlyrics.com/'),
            ('Milky Moon forums',
             'http://www.fromamouth.com/milkymoon/'),
            ('Facebook group',
             'https://www.facebook.com/groups/JoannaNewsomUnofficial/'),
            ('Blessing All the Birds Tumblr',
             'http://allthebirds.tumblr.com')
        )
SOCIAL_TITLE = 'Social'
SOCIAL = (('Email', 'mailto:thenightjarkid@gmail.com',
         'fa fa-envelope fa-fw fa-lg'),
        ('Pinboard', 'https://pinboard.in/u:rufousii/',
         'fa fa-thumb-tack fa-fw fa-lg')
        )


#-------#
# Feeds #
#-------#

SHOW_FEEDS_TEST = True
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


#------------#
# URL scheme #
#------------#

SLUGIFY = 'basename'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'
#RELATIVE_URLS = True

