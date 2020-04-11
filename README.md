flag-loader
===========

A tool for downloading country flags from Wikimedia Commons.

This is done not by specifying the filename of the flag, but some sort of
"country identifier". This can currently be the Top Level Domain of the
country, the English country name or the corresponding ISO 3166-1 alpha-2
code.

The default is to download the vector graphic version, but this can be changed
by specifying the --bitmap argument.

Usage
-----

    usage: flag-loader.py [-h] [--tld | --name | --iso-3166-1] [--bitmap]
                          [--bitmap-width WIDTH] [--url]
                          LIST [LIST ...]

    A tool for downloading country flags from Wikimedia Commons

    positional arguments:
      LIST                  List of data separated by a space (e.g. 'DE AU')

    optional arguments:
      -h, --help            show this help message and exit
      --tld                 Interpret LIST as Top Level Domain (e.g. '.de')
      --name                Interpret LIST as official English country name (e.g.
                            'Germany')
      --iso-3166-1          Interpret LIST as ISO 3166-1 alpha-2 code (e.g. 'DE')
      --bitmap              Download a raster image instead of a vector graphic
      --bitmap-width WIDTH  Width of the raster image in pixels
      --url                 Do not download, print URL only

Example
-----
Command line:

    flag-loader.py --tld .de .au .md

Output:

    Downloading 'Flag of Germany.svg'...
    Done.
    Downloading 'Flag of Australia.svg'...
    Done.
    Downloading 'Flag of Moldova.svg'...
    Done.

Requirements
-----

* Python 3
* simplemediawiki > 1.1.1 (https://github.com/iliana/python-simplemediawiki/releases)

Tested with Python 3.8.2 & simplemediawiki 1.2.0b2.

Installation
-----
Run ```pip install -r requirements.txt``` to install the dependencies with pip.

License
-----

MIT License (see LICENSE.txt)
