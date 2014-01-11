"""Part of the flag-loader project.

Copyright: (C) 2014 Michael Bemmerl
License: MIT License (see LICENSE.txt)

Exported classes: WikidataTitleResolver
"""

from Wikidata import Wikidata
from WikidataItemResolver import WikidataItemResolver


class WikidataTitleResolver(WikidataItemResolver):
    """Resolves a title to an valid Wikidata country entity.
    
    Example: The title '.de' would result in the Wikidata entity 'Q37251'.
    
    The country claim is then fetched from this entry, which is then fed into
    the WikidataItemResolver to finally get the flag image name.
    
    This class is for internal use only and should not be called directly.
    """
    
    def get_flag(self, title):
        wd = Wikidata()

        # Find all entities witch match the title
        entities = wd.get_entities_from_title(title)

        # Check if the title was found...
        if not entities:
            return None
        
        # Then get the country claim from the first entity
        country = wd.get_claims_from_entity(entities[0], property=Wikidata.PROPERTY_COUNTRY)

        # No country claim...
        if country is None:
            return None
        
        # Value comes in pure integer form and needs some formatting.
        country = u'Q{0}'.format(country[Wikidata.PROPERTY_COUNTRY][0]['value']['numeric-id'])

        # Call base class get_flag method
        return super(WikidataTitleResolver, self).get_flag(country)
