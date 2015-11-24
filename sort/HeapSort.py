'''
Created on Oct 24, 2015

@author: TranBui
'''
from sort.SortBase import SortBase
import math
class HeapSort(SortBase):
    '''
    HeapSort
    Expected run-time: O(n lg n)
    Worst-case run-time: O(n lg n)
    Best-case run-time: O(n lg n)
    In-place
    Not stable
    High overhead, but have guaranteed run-time when n >>
    '''

    def __init__(self,list):
        self.list = list
    
    def maxHeapify(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index
        if (left < len(self.list) and self.list[left] > self.list[index]):
            largest = left
        else:
            largest = index
        if (right < len(self.list) and self.list[right] > self.list[largest]):
            largest = right
        if (largest != index):
            temp = self.list[largest]
            self.list[largest] = self.list[index]
            self.list[index] = temp
            self.maxHeapify(largest)
    
    def buildMaxHeap(self):
        start = math.floor(len(self.list)/2)
        for i in range(start,-1,-1):
            self.maxHeapify(i);
        
    def sort(self):
        result = []
        self.buildMaxHeap()
        start = len(self.list)-1
        end = 0
        i = start
        while (i >= end):
            result.append(self.list[0])
            temp = self.list[i]
            self.list[i] = self.list[0]
            self.list[0] = temp
            del self.list[i]
            i -= 1
            self.maxHeapify(0)
        return result
            