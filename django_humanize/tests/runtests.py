#!/usr/bin/env python

import os, sys
from os.path import dirname, join

# Hack to make tests working even in dev mode

clone_dir = dirname(dirname(dirname(__file__)))
if os.path.exists(join(clone_dir, 'setup.py')):
    sys.path.append(clone_dir)

from django.conf import settings
settings.configure(DEBUG=True,
               DATABASES={
                    'default': {
                        'ENGINE': 'django.db.backends.sqlite3',
                    }
                },
#               ROOT_URLCONF='myapp.urls',
               INSTALLED_APPS=('django.contrib.auth',
                              'django.contrib.contenttypes',
                              'django.contrib.sessions',
                              'django.contrib.admin',
                              'django_humanize',),
               USE_L10N = True)

import django; django.setup()

try:
    # Django <= 1.8
    from django.test.simple import DjangoTestSuiteRunner
    test_runner = DjangoTestSuiteRunner(verbosity=1)
except ImportError:
    # Django >= 1.8
    from django.test.runner import DiscoverRunner
    test_runner = DiscoverRunner(verbosity=1)

failures = test_runner.run_tests(['django_humanize.tests'])
if failures:
    sys.exit(failures)
