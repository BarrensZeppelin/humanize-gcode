#!/usr/bin/env python

from distutils.core import setup

setup(name='humanize-gcode',
      version='0.0.1',
      description='Generate description of GCode',
      author='Oskar Haarklou Veileborg',
      author_email='ohv1020@hotmail.com',
      url='https://www.python.org/sigs/distutils-sig/',
      install_requires=[
	      'requests_html',
	      'crayons',
      ],
      packages=['humanize_gcode'],
      scripts=['scripts/hucode'])
