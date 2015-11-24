'''
Created on Oct 24, 2015

@author: TranBui
'''

from abc import ABCMeta, abstractmethod

class SortBase(metaclass=ABCMeta):
    '''
    Interface for all sort classes
    '''
    @abstractmethod
    def sort(self,list):
        pass