#!/usr/bin/python

""" Downloading country flags from Wikimedia Commons

Copyright: (C) 2014 Michael Bemmerl
License: MIT License (see COPYING)

Requirements:
- Python (well, obviously ;-)
- simplemediawiki (https://pypi.python.org/pypi/simplemediawiki)

Tested with Python 2.7.6 and simplemediawiki 1.2.0b2
"""

import argparse
import urllib
import sys
from WikimediaCommons import WikimediaCommons
from resolver import *

parser = argparse.ArgumentParser(description="A tool for downloading country flags from Wikimedia Commons")
parser.add_argument('LIST', nargs='+', help="List of data separated by a space (e.g. 'DE AU')")
group = parser.add_mutually_exclusive_group()
group.add_argument('--tld', action='store_true', help="Interpret LIST as Top Level Domain (e.g. '.de')")
group.add_argument('--name', action='store_true', help="Interpret LIST as official English country name (e.g. 'Germany')")
group.add_argument('--iso-3166-1', action='store_true', help="Interpret LIST as ISO 3166-1 alpha-2 code (e.g. 'DE')")

# More to come: http://www.statoids.com/wab.html

parser.add_argument('--bitmap', action='store_true', help="Download a raster image instead of a vector graphic")
parser.add_argument('--bitmap-width', type=int, metavar='WIDTH', help="Width of the raster image in pixels")
parser.add_argument('--url', action='store_true', help="Do not download, print URL only")

args = parser.parse_args()

if args.tld:
    resolver = TLDResolver()
elif args.name:
    resolver = CountryNameResolver()
elif args.iso_3166_1:
    resolver = ISO31661Resolver()
else:
    parser.error("Too few arguments. At least one of the optional arguments ('--tld', '--name', etc.) must be given.")

for entry in args.LIST:
    entry = resolver.normalize(entry)
    flag = resolver.get_flag(entry)

    if flag is None:
        print >> sys.stderr, "No flag for '{0}' found.".format(entry)
        continue

    wmc = WikimediaCommons()
    
    if args.bitmap:
        width = args.bitmap_width
        # Use 200 pixels as default if the width was omitted
        if width is None:
            width = 200
        flag_url = wmc.get_thumb_image_url(flag, width=width)
    else:
        flag_url = wmc.get_image_url(flag)

    if args.url:
        print flag_url
    else:
        # Use flag name as file name
        file = flag
        bmptxt = ""
        
        if args.bitmap:
            bmptxt = "raster image version of "
            # Extract file extensions and fiddle all together
            file = '{0}-{1}px.{2}'.format(flag[:flag.rindex('.')], width, flag_url[flag_url.rindex('.') + 1:])
            
        print "Downloading {1}'{0}'...".format(flag, bmptxt)
        data = urllib.urlretrieve(flag_url, file)
        print "Done."
