'''
Created on Oct 28, 2015

@author: TranBui
'''
import math
from sort.SortBase import SortBase
class ShellSort(SortBase):
    '''
    ShellSort
    '''


    def __init__(self, list):
        '''
        Constructor
        '''
        self.list = list
        
    def sort(self):
        n = len(self.list)
        h = math.floor(n/2)+1
        while (h != 0):
            print(h)
            for i in range(h,n):
                tmp = self.list[i]
                j = i - h
                while (j>=0 and (self.list[j])> tmp):
                    self.list[j+h] = self.list[j]
                    j = j-h
                self.list[j+h] = tmp
            h = int(h/2)
            print(self.list)  
        