'''
Created on Oct 24, 2015

@author: TranNguyen
'''
from sort.SortBase import SortBase

class BubbleSort(SortBase):
    '''
    BubbleSort
    
    Average runtime: O(n^2)
    Worst-case runtime: O(n^2)
    In-place
    Easy to implement, otherwise it's bad in general
    '''
    def __init__(self):
        pass

    def sort(self,list):
        self.list = list
        for i in range(0,len(self.list)-1):
            for j in range(i,len(self.list)):
                if self.list[j] < self.list[i]:
                    temp = self.list[i]
                    self.list[i] = self.list[j]
                    self.list[j] = temp
          