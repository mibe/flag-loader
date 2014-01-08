
from Wikidata import Wikidata

class CountryNameResolver(object):
    def get_flag(self, name):
        wd = Wikidata()

        entities = wd.get_entities_from_title(name)

        # Check if the country name was found...
        if not entities:
            return None

        flag = wd.get_claims_from_entity(entities[0], property=Wikidata.PROPERTY_FLAG_IMAGE)

        # Has the country a flag image property?
        if flag is None:
            return None

        # Yes it has, get the image name from the data
        flag = flag[Wikidata.PROPERTY_FLAG_IMAGE][0]['value']
        
        return flag
