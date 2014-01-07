#!/usr/bin/python

""" Retrieves various data of an entity on Wikidata.

Part of the flag-loader project.

Copyright: (C) 2014 Michael Bemmerl
License: MIT License (see COPYING)
"""

# https://en.wikidata.org/w/api.php?action=wbgetentities&sites=enwiki&titles=.de&format=jsonfm&props=claims
# https://en.wikidata.org/w/api.php?action=wbgetclaims&entity=Q183&property=P41

from simplemediawiki import MediaWiki

class Wikidata(object):
    def __init__(self, SSL=None):
        scheme = 'http'
        if SSL is True:
            scheme += 's'

        self.client = MediaWiki(scheme + '://en.wikidata.org/w/api.php')

    def get_entites_from_title(self, title):
        params = {'action': 'wbgetentities', 'sites': 'enwiki', 'titles': title, 'props': ''}

        call = self.client.call(params)
        entities = call['entities'].keys()
        
        result = list()
        
        try:
            # If the first key is an integer ("-1"), no entities were found.
            int(entities[0])
            return result
        except ValueError:
            # Exception: Not an integer, so it should be something like "Q1234".
            for entity in entities:
                result.append(entity)
            return result
        
    def get_claims_from_entity(self, entity, property=None):
        params = {'action': 'wbgetclaims', 'entity': entity}
        if property is not None:
            params['property'] = property

        call = self.client.call(params)
        
        if u'error' in call:
            return None
            
        claims = call['claims']
        result = dict()
        
        for claim in claims:
            result[claim] = claims[claim][0]['mainsnak']['datavalue']['value']
        
        return result
        
