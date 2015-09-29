#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup

try:
    README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()
except IOError:
    README = ''


setup(name='django-humanize',
      version='0.1.2',
      description='Use humanize 3rd-party lib as template filters',
      long_description=README,
      author='Jocelyn Delalande',
      author_email='jdelalande@oasiswork.fr',
      url='https://github.com/oasiswork/django-humanize/',
      license='BSD License',
      packages=['django_humanize', 'django_humanize.templatetags'],
      install_requires=['humanize>=0.5.1', 'Django'],
      classifiers=[
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Framework :: Django'
      ]
)
