# -*- coding:utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import os
import sys

__version__ = '1.0.0'


class DjangoSettingsFileError(Exception):
    pass


def setup():
    if 'DJANGO_SETTINGS_MODULE' in os.environ:
        raise DjangoSettingsFileError(
            'DJANGO_SETTINGS_MODULE should not be defined, only DJANGO_SETTINGS_FILE is obeyed',
        )
    if 'DJANGO_SETTINGS_FILE' not in os.environ:
        raise DjangoSettingsFileError('DJANGO_SETTINGS_FILE is not defined')
    os.environ['DJANGO_SETTINGS_MODULE'] = 'django_settings_file.settings_py{}'.format(sys.version_info[0])
