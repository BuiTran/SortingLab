'''
Created on Oct 24, 2015

@author: TranBui
'''
from sort.SortBase import SortBase



class InsertionSort(SortBase):
    '''
    InsertionSort
    
    Average runtime: O(n^2)
    Worst-case runtime: O(n^2)
    In-place
    Not stable
    Work best with short list (small amount of elements: 10~)
    Easy to implement
    
    '''
 
    def sort(self, list):
        self.list = list
        for i in range(1,len(self.list)):
            j = i;
            while ((j > 0) and (self.list[j-1]>self.list[j])):
                temp = self.list[j-1];
                self.list[j-1] = self.list[j];
                self.list[j] = temp;
                j=j-1;
            
                   
            
        