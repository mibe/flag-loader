#!/usr/bin/python

# https://commons.wikimedia.org/w/api.php?action=query&titles=Image:Commons-logo.svg&prop=imageinfo&iiprop=url&iiurlwidth=150&format=json

from simplemediawiki import MediaWiki
import json

class WikimediaCommons(object):
    client = None

    def __init__(self, SSL=None):
        scheme = 'http'
        if SSL is True:
            scheme += 's'

        self.client = MediaWiki(scheme + '://commons.wikimedia.org/w/api.php')

    def call_api(self, title, namespace='Image', thumbwidth=None):
        """ Call the Commons API """
        title = '{0}:{1}'.format(namespace, title)
        params = {'action': 'query', 'titles': title, 'prop': 'imageinfo', 'iiprop': 'url'}
        if thumbwidth is not None:
            params['iiurlwidth'] = thumbwidth

        result = self.client.call(params)
        pages = result['query']['pages']
        id = pages.keys()[0]

        if id is -1:
            return None
        else:
            return pages[id]

    def get_image_url(self, name):
        """ Retrieve the URL to the raw image """
        result = self.call_api(name)
        image = result['imageinfo'][0]

        return image['url']

    def get_thumb_image_url(self, name, width):
        """ Retrieve the URL to the thumbnail image """
        result = self.call_api(name, thumbwidth=width)
        image = result['imageinfo'][0]

        return image['thumburl']
        
