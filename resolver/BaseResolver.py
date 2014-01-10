
from abc import ABCMeta, abstractmethod

class BaseResolver(object):
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def get_flag(self, data):
        pass
    
    @abstractmethod
    def normalize(self, data):
        pass