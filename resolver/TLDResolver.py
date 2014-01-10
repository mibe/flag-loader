"""Part of the flag-loader project.

Copyright: (C) 2014 Michael Bemmerl
License: MIT License (see LICENSE.txt)

Exported classes: TLDResolver
"""

from Wikidata import Wikidata
from WikidataTitleResolver import WikidataTitleResolver

class TLDResolver(WikidataTitleResolver):
    """Resolves a flag image from a country-code top level domain (e.g. '.de')."""
    
    def get_flag(self, tld):
        # Call base class get_flag method
        return super(TLDResolver, self).get_flag(tld)
        
    def normalize(self, tld):
        tld = tld.lower()
        # add dot if missing
        if tld[0] != '.':
            tld = '.{0}'.format(tld)
        
        return tld