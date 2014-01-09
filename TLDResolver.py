
from Wikidata import Wikidata
from WikidataItemResolver import WikidataItemResolver

class TLDResolver(WikidataItemResolver):
    def get_flag(self, tld):
        wd = Wikidata()

        entities = wd.get_entities_from_title(tld)

        # Check if the TLD was found...
        if not entities:
            return None
        
        # Then get the country claim
        country = wd.get_claims_from_entity(entities[0], property=Wikidata.PROPERTY_COUNTRY)
        
        if country is None:
            return None
        
        # Value comes in pure integer form and needs some formatting.
        country = u'Q{0}'.format(country[Wikidata.PROPERTY_COUNTRY][0]['value']['numeric-id'])

        # Call base class get_flag method
        return super(TLDResolver, self).get_flag(country)
