'''
Created on Oct 24, 2015

@author: TranBui
'''
from sort.SortBase import SortBase
import math
from _overlapped import NULL
class MergeSort(SortBase):
    '''
    MergeSort
    
    Expected Runtime: O(n lg n)
    Worst-case Runtime: O(n lg n)
    Best-case Runtime: O(n lg n)
    In-place
    Not stable
    Standard sort
    
    '''
    def __init__(self,list):
        self.list = list
    
    def merge(self,p,q,r):
        L = []
        R = []
        L.extend(self.list[p:q+1])
        R.extend(self.list[q+1:r+1])
        L.append(None)
        R.append(None)
         
         
        i = 0;
        j = 0;
        for k in range(p,r+1):
            if (L[i] is None):
                self.list[k] = R[j]
                j+=1
            elif (R[j] is None):
                self.list[k] = L[i]
                i+=1;
            elif (L[i] <= R[j]):
                self.list[k] = L[i]
                i += 1
            else:
                self.list[k] = R[j]
                j += 1
        
    def mergeSort(self, p, r):
        if (p<r):
            q = math.floor((p+r)/2)
            self.mergeSort(p,q)
            self.mergeSort(q+1,r)
            self.merge(p,q,r);
            
    def sort(self):
        self.mergeSort(0, len(self.list)-1)
          