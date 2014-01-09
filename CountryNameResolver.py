
from Wikidata import Wikidata
from WikidataItemResolver import WikidataItemResolver

class CountryNameResolver(WikidataItemResolver):
    def get_flag(self, name):
        wd = Wikidata()

        entities = wd.get_entities_from_title(name)

        # Check if the country name was found...
        if not entities:
            return None

        # Call base class get_flag method
        # (uses the Wikidata item identifier retrieved above)
        return super(CountryNameResolver, self).get_flag(entities[0])
