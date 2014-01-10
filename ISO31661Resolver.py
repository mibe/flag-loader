
from Wikidata import Wikidata
from WikidataTitleResolver import WikidataTitleResolver

class ISO31661Resolver(WikidataTitleResolver):
    def get_flag(self, code):
        code = 'ISO 3166-2:{0}'.format(code)
        
        # Call base class get_flag method
        return super(ISO31661Resolver, self).get_flag(code)
        
    def normalize(self, code):
        return code.upper()
