'''
Created on Oct 27, 2015

@author: TranBui
'''
import unittest

from sort.InsertionSort import InsertionSort
from sort.BubbleSort import BubbleSort
from sort.MergeSort import MergeSort
from sort.HeapSort import HeapSort
from sort.QuickSort import QuickSort
from sort.RandomizedQuickSort import RandomizedQuickSort
from sort.CountingSort import CountingSort
from sort.RadixSort import RadixSort
from sort.ShellSort import ShellSort


class Test(unittest.TestCase):


    def testBubbleSort(self):
        x = [-20,-45,995,912,126,1246,624]
        bubbleSort = BubbleSort();
        bubbleSort.sort(x)
        self.assertEqual(x,[-45.0, -20.0, 126, 624, 912, 995, 1246])
    
    def testInsertionSort(self):
        x = [-20,-45,995,912,126,1246,624]
        insertionSort = InsertionSort();
        insertionSort.sort(x)
        self.assertEqual(x,[-45.0, -20.0, 126, 624, 912, 995, 1246])
        
    def testHeapSort(self):
        x = [-20,-45,995,912,126,1246,624]
        heapSort = HeapSort(x)
        x = heapSort.sort()
        #This will sort from highest>lowest
        self.assertEqual(x,[1246, 995, 912, 624, 126, -20, -45])
    def testMergeSort(self):
        x = [-20,-45,995,912,126,1246,624]
        mergeSort = MergeSort(x)
        mergeSort.sort()
        self.assertEqual(x,[-45.0, -20.0, 126, 624, 912, 995, 1246])
    def testQuickSort(self):
        x = [-20,-45,995,912,126,1246,624,1000,2000]
        quickSort = QuickSort(x)
        quickSort.start()
        self.assertEqual(x,[-45.0, -20.0, 126, 624, 912, 995,1000, 1246,2000])
    def testRandomizedQuickSort(self):
        x = [-20,-45,995,912,126,1246,624]
        randomizedQuickSort = RandomizedQuickSort(x)
        randomizedQuickSort.start()
        self.assertEqual(x,[-45.0, -20.0, 126, 624, 912, 995, 1246])
    def testCountingSort(self):
        x = [-20,-45,995,912,126,1246,624]
        countingSort = CountingSort(x)
        x = countingSort.sort()
        self.assertEqual(x,[-45.0, -20.0, 126, 624, 912, 995, 1246])
    def testRadixSort(self):
        x = [-20,-45,995,912,126,1246,624]
        radixSort = RadixSort(x)
        x = radixSort.sort()
        self.assertEqual(x,[-45.0, -20.0, 126, 624, 912, 995, 1246])
    def testShellSort(self):
        x = [-20,-45,995,912,126,1246,624]
        shellSort = ShellSort(x)
        shellSort.sort()
        self.assertEqual(x,[-45.0, -20.0, 126, 624, 912, 995, 1246])
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testBubbleSort']
    unittest.main()