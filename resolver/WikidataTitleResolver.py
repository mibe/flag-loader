"""Part of the flag-loader project.

Copyright: (C) 2014,2016 Michael Bemmerl
License: MIT License (see LICENSE.txt)

Exported classes: WikidataTitleResolver
"""

from Wikidata import Wikidata
from WikidataItemResolver import WikidataItemResolver


class WikidataTitleResolver(WikidataItemResolver):
    """Resolves a title to an valid Wikidata country entity.
    
    Example: The title '.de' would result in the Wikidata entity 'Q37251'.
    
    The country claim is then fetched from this entry, which is then fed into
    the WikidataItemResolver to finally get the flag image name. If the
    country claim is not available on this item, the claim "applies to
    territorial jurisdiction" is used.
    
    This class is for internal use only and should not be called directly.
    """

    def __init__(self):
        self.wd = Wikidata()

    def get_flag(self, title):
        # Find all entities witch match the title
        entities = self.wd.get_entities_from_title(title)

        # Check if the title was found...
        if not entities:
            return None
        
        # Then get the country claim from the first entity
        country = self.get_item_id(entities[0], Wikidata.PROPERTY_COUNTRY)

        # No country claim, so try another (far-fetched) claim
        if country is None:
            country = self.get_item_id(entities[0], Wikidata.PROPERTY_APPLIES_TO_TERRITORIAL_JURISDICTION)
            # No claim either, this is it...
            if country is None:
                return None
        
        # Value comes in pure integer form and needs some formatting.
        country = u'Q{0}'.format(country)

        # Call base class get_flag method
        return super(WikidataTitleResolver, self).get_flag(country)
        
    def get_item_id(self, entity, property):
        result = self.wd.get_claims_from_entity(entity, property)
        
        if result is None:
            return None
            
        return result[property][0]['value']['numeric-id']
