
from Wikidata import Wikidata
from WikidataTitleResolver import WikidataTitleResolver

class TLDResolver(WikidataTitleResolver):
    def get_flag(self, tld):
        # Call base class get_flag method
        return super(TLDResolver, self).get_flag(tld)
