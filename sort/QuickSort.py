'''
Created on Oct 24, 2015

@author: TranBui
'''
from sort.SortBase import SortBase

class QuickSort(SortBase):
    '''
    Quicksort
    Expected run time: O(n lg n)
    Worst case: O(n^2)
    In-place
    Not stable
    One of the fastest sort
    '''


    def __init__(self, list):
        '''
        Constructor
        '''
        self.list = list
        
    def partition(self,p,r):
        pivot = r
        i = p - 1;
        for j in range(p,r):
            if (self.list[j] <= self.list[pivot]):
                i += 1
                temp = self.list[j]
                self.list[j] = self.list[i]
                self.list[i] = temp
        
        temp = self.list[pivot]
        self.list[pivot] = self.list[i+1]
        self.list[i+1] = temp
        return i+1
    
    def sort(self,p,r):
        if (p<r):
            q = self.partition(p,r)
            self.sort(p,q-1)
            self.sort(q+1,r)
    
    def start(self):
        self.sort(0,len(self.list)-1)  