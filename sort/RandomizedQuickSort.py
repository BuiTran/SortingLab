'''
Created on Oct 24, 2015

@author: TranBui
'''
from sort.SortBase import SortBase
import random
import math
class RandomizedQuickSort(SortBase):
    '''
    Randomized Quick Sort
    Expected run time: O(n lg n)
    Worst case: O(n^2)
    In-place
    Not stable
    Enhanced version of normal quicksort.
    '''

    def __init__(self, list):
        '''
        Constructor
        '''
        self.list = list
        
    def partition(self,p,r):
        #choose a random number between p and r, then switch list[x] with list[r]
        x = math.floor(random.random() * (r-p))+ p+1; 
        temp = self.list[x]
        self.list[x] = self.list[r]
        self.list[r] = temp
        #now set the pivot to be r
        pivot = r;
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