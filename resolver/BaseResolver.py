"""Part of the flag-loader project.

Copyright: (C) 2014 Michael Bemmerl
License: MIT License (see LICENSE.txt)

Exported classes: BaseResolver
"""

from abc import ABCMeta, abstractmethod


class BaseResolver(object, metaclass=ABCMeta):
    """Abstract base class for all resolvers."""
    
    @abstractmethod
    def get_flag(self, data):
        pass
    
    @abstractmethod
    def normalize(self, data):
        pass
