"""Part of the flag-loader project.

Copyright: (C) 2014 Michael Bemmerl
License: MIT License (see LICENSE.txt)

Exported classes: ISO31661Resolver
"""

from .WikidataTitleResolver import WikidataTitleResolver


class ISO31661Resolver(WikidataTitleResolver):
    """Resolves an ISO 3166-1 alpha-2 code (e.g. 'DE') to a flag image."""
    
    def get_flag(self, code):
        code = 'ISO 3166-2:{0}'.format(code)
        
        # Call base class get_flag method
        return super(ISO31661Resolver, self).get_flag(code)
        
    def normalize(self, code):
        # Codes are all upper-case.
        return code.upper()
