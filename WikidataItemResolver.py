
from Wikidata import Wikidata
from BaseResolver import BaseResolver

class WikidataItemResolver(BaseResolver):
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
    