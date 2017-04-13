# -*- coding:utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        print(getattr(settings, 'MY_EXAMPLE_SETTING', 'failfailfail'))
