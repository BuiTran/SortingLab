'''
Created on Oct 24, 2015

@author: TranBui
'''
from sort.SortBase import SortBase
import math
class CountingSort(SortBase):
    '''
    CountingSort
    Linear time sort with restrictions (all elements in list must be less than a number)
    Not in-place
    Stable Sort
    '''


    def __init__(self, list):
        '''
        Constructor
        '''
        self.list = list
    
    def __findMax(self):
        self.max = self.list[0]
        for i in range(len(self.list)):
            if self.max < self.list[i]:
                self.max = self.list[i]
        self.max = self.max + 1
    
    def __findMin(self):
        self.min = self.list[0]
        for i in range(len(self.list)):
            if self.min > self.list[i]:
                self.min = self.list[i]
        
    def sort(self):
        self.__findMin()
        #This will ensure that counting sort will also works for negative numbers
        for i in range(len(self.list)):
            self.list[i] = self.list[i] + abs(self.min)
        self.__findMax()
        c = []
        result = []
        for i in range(self.max):
            c.append(0)
            
        for i in range(len(self.list)): 
            c[self.list[i]] += 1
            result.append(0)
        for i in range(1,self.max):
            c[i] = c[i] + c[i-1]
        i = len(self.list)-1
        while(i >= 0):
            result[c[self.list[i]]-1] = self.list[i]
            c[self.list[i]] -= 1
            i -= 1
    #subtract the abs(min) from all the elements
        for i in range(len(result)):
            result[i] = result[i] - (abs(self.min))
        return result
            
        