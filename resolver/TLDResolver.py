
from Wikidata import Wikidata
from WikidataTitleResolver import WikidataTitleResolver

class TLDResolver(WikidataTitleResolver):
    def get_flag(self, tld):
        # Call base class get_flag method
        return super(TLDResolver, self).get_flag(tld)
        
    def normalize(self, tld):
        tld = tld.lower()
        # add dot if missing
        if tld[0] != '.':
            tld = '.{0}'.format(tld)
        
        return tld