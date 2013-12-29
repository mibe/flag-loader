#!/usr/bin/python

""" Downloading country flags from Wikimedia Commons

Copyright: (C) 2013 Michael Bemmerl
License: MIT License (see COPYING)

Requirements:
- Python (well, obviously ;-)

Tested with Python 2.7.6
"""

import argparse

parser = argparse.ArgumentParser(description="A tool for downloading country flags from Wikimedia Commons")
parser.add_argument('ARG')
parser.add_argument('--tld', action='store_true', help="Interpret ARG as Top Level Domain")
parser.add_argument('--name', action='store_true', help="Interpret ARG as official english country name")
parser.add_argument('--iso-3166-1', action='store_true', help="Interpret ARG as ISO 3166-1 alpha-2 code")

# More to come: http://www.statoids.com/wab.html

parser.add_argument('--png', help="Download a PNG image instead of a SVG")


args = parser.parse_args()
