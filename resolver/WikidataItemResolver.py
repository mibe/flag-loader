"""Part of the flag-loader project.

Copyright: (C) 2014 Michael Bemmerl
License: MIT License (see LICENSE.txt)

Exported classes: WikidataItemResolver
"""

from Wikidata import Wikidata
from BaseResolver import BaseResolver

class WikidataItemResolver(BaseResolver):
    """Retrieves the flag image claim from a Wikidata item.
    
        
    This class is for internal use only and should not be called directly.
    """
    
    def get_flag(self, item):
        # Items start with a 'Q' (see Wikidata glossary)
        if item[0] != 'Q':
            return None

        wd = Wikidata()
        flag = wd.get_claims_from_entity(item, property=Wikidata.PROPERTY_FLAG_IMAGE)

        # Has the country a flag image property?
        if flag is None:
            return None

        # Yes it has, get the image name from the data
        flag = flag[Wikidata.PROPERTY_FLAG_IMAGE][0]['value']
        
        return flag
    