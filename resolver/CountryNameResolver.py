"""Part of the flag-loader project.

Copyright: (C) 2014 Michael Bemmerl
License: MIT License (see LICENSE.txt)

Exported classes: CountryNameResolver
"""

from Wikidata import Wikidata
from WikidataItemResolver import WikidataItemResolver

class CountryNameResolver(WikidataItemResolver):
    """Resolves a country name (e.g. 'Germany') to a flag image.
    
    This is done by querying Wikidata for a title with this country name.
    The resulting entity must have a country claim.
    """
    
    def get_flag(self, name):
        wd = Wikidata()

        # Get Wikidata entity for the country name
        entities = wd.get_entities_from_title(name)

        # Check if the country name was found...
        if not entities:
            return None

        # Call base class get_flag method
        # (uses the Wikidata item identifier retrieved above)
        return super(CountryNameResolver, self).get_flag(entities[0])
    
    def normalize(self, name):
        # nothing do to here
        return name