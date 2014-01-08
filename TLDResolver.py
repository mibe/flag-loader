
from Wikidata import Wikidata

class TLDResolver(object):
    def get_flag(self, tld):
        wd = Wikidata()

        entities = wd.get_entities_from_title(tld)

        # Check if the TLD was found...
        if not entities:
            return None
            
        country = wd.get_claims_from_entity(entities[0], property=Wikidata.PROPERTY_COUNTRY)
        
        if country is None:
            return None
            
        country = u'Q{0}'.format(country[Wikidata.PROPERTY_COUNTRY][0]['value']['numeric-id'])

        flag = wd.get_claims_from_entity(country, property=Wikidata.PROPERTY_FLAG_IMAGE)

        # Has the country a flag image property?
        if flag is None:
            return None

        # Yes it has, get the image name from the data
        flag = flag[Wikidata.PROPERTY_FLAG_IMAGE][0]['value']
        
        return flag
