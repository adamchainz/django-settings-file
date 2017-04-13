# -*- coding:utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import imp
import os

module = imp.load_source('module', os.environ['DJANGO_SETTINGS_FILE'])

# Take all the attributes
globals().update(module.__dict__)
