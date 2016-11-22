""" Retrieves various data of an entity on Wikidata.

Part of the flag-loader project.

Copyright: (C) 2014,2016 Michael Bemmerl
License: MIT License (see LICENSE.txt)
"""

# https://en.wikidata.org/w/api.php?action=wbgetentities&sites=enwiki&titles=.de&format=jsonfm&props=claims
# https://en.wikidata.org/w/api.php?action=wbgetclaims&entity=Q183&property=P41

from simplemediawiki import MediaWiki


class Wikidata(object):
    """Talks to the Wikidata API to retrieve information about entities and claims."""
    PROPERTY_COUNTRY = 'P17'
    PROPERTY_FLAG_IMAGE = 'P41'
    PROPERTY_APPLIES_TO_TERRITORIAL_JURISDICTION = 'P1001'

    def __init__(self):
        self.client = MediaWiki('https://www.wikidata.org/w/api.php')

    def get_entities_from_title(self, title, sites='enwiki'):
        """Return the entities matching the supplied title in a list.

        Arguments:
        title -- Name of the entity
        sites -- Wikidata site which should be searched for the title (default enwiki)

        Returns an empty list when no matching entity was found.
        """
        params = {'action': 'wbgetentities', 'sites': sites, 'titles': title, 'props': ''}

        call = self.client.call(params)
        entities = call['entities'].keys()
        
        result = list()
        
        if entities[0] != -1:
            for entity in entities:
                result.append(entity)
                
        return result
    
    def get_claims_from_entity(self, entity, property=None):
        """Return the claims of the supplied entity.
        
        Arguments:
        entity -- Entity identifier
        property -- Filter to return only claims which has this property (default None)
        
        Returns a dictionary containing each claim. The value holds a list with the property values.
        Returns None when the entity was not found.
        """
        params = {'action': 'wbgetclaims', 'entity': entity}
        if property is not None:
            params['property'] = property

        call = self.client.call(params)
        
        # If entity was not found or on an empty claims dictionary return
        if u'error' in call or not call['claims']:
            return None
            
        claims = call['claims']
        result = dict()
        
        for property in claims:
            result[property] = list()
            values = claims[property]

            # multiple values are possible (see P31 on Q42)
            for value in values:
                result[property].append(value['mainsnak']['datavalue'])
        
        return result
