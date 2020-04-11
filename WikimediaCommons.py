""" Retrieves various meta-data of an image hosted on Wikimedia Commons.

Part of the flag-loader project.

Copyright: (C) 2014,2016 Michael Bemmerl
License: MIT License (see LICENSE.txt)
"""

# https://commons.wikimedia.org/w/api.php?action=query&titles=Image:Commons-logo.svg&prop=imageinfo&iiprop=url&iiurlwidth=150&format=json

from simplemediawiki import MediaWiki


class WikimediaCommons(object):
    """Talks to the Wikimedia Commons API to retrieve information about an
    image hosted on Wikimedia Commons.
    """
    
    def __init__(self):
        self.client = MediaWiki('https://commons.wikimedia.org/w/api.php')

    def __call_api(self, title, namespace='Image', thumbwidth=None):
        """Call the Commons API.
        
        Arguments:
        title -- Title of the page.
        namespace -- Namespace this title lies in (default 'Image')
        thumbwidth -- Width in pixels required for the thumbnail image URL (default None)
        
        Returns the API response or None when the title was not found.
        """
        title = '{0}:{1}'.format(namespace, title)
        params = {'action': 'query', 'titles': title, 'prop': 'imageinfo', 'iiprop': 'url'}
        if thumbwidth is not None:
            params['iiurlwidth'] = thumbwidth

        result = self.client.call(params)
        pages = result['query']['pages']
        id = list(pages.keys())[0]
        
        if id == -1:
            return None
        else:
            return pages[id]

    def get_image_url(self, name):
        """Retrieve the URL to the raw image.
        
        Arguments:
        name -- Image name
        
        Returns the image URL or None when the image was not found.
        """
        result = self.__call_api(name)
        if result is None:
            return None

        image = result['imageinfo'][0]

        return image['url']

    def get_thumb_image_url(self, name, width):
        """Retrieve the URL to the thumbnail image.
        
        Arguments:
        name -- Image name
        width -- Requested width in pixel
        
        Returns the thumbnail image URL or None when the image was not found.
        """
        result = self.__call_api(name, thumbwidth=width)
        if result is None:
            return None

        image = result['imageinfo'][0]

        return image['thumburl']
