#!/usr/bin/env python

from setuptools import setup

with open('README.md', 'r') as readme:
      long_description = readme.read()

setup(name='humanize-gcode',
      version='0.0.3',
      description='Annotates GCode files with human readable descriptions of commands',
      author='Oskar Haarklou Veileborg',
      author_email='ohv1020@hotmail.com',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/BarrensZeppelin/humanize-gcode',
      install_requires=[
	      'requests_html',
	      'crayons',
	      'appdirs',
      ],
      packages=['humanize_gcode'],
      scripts=['scripts/hucode'],
      classifiers=(
            'Programming Language :: Python :: 3.6',
      ))
