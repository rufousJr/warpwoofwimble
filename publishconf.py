#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

OUTPUT_PATH = 'output-publish/'

SITEURL = 'http://www.warpwoofwimble.com'
RELATIVE_URLS = False

SHOW_FEEDS_TEST = False
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

DISQUS_SITENAME = "warpwoofwimble"
#GOOGLE_ANALYTICS = "UA-79837203-1"
#GOOGLE_ANALYTICS_SITEID = "auto"
