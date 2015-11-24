'''
Created on Oct 24, 2015

@author: TranBui
'''

from sort.InsertionSort import InsertionSort
from sort.BubbleSort import BubbleSort
from sort.MergeSort import MergeSort
from sort.HeapSort import HeapSort
from sort.QuickSort import QuickSort
from sort.RandomizedQuickSort import RandomizedQuickSort
from sort.CountingSort import CountingSort
from sort.RadixSort import RadixSort
from sort.ShellSort import ShellSort
import math
import random
from timeit import default_timer as timer

def dBubbleSort(x):
    bubbleSort = BubbleSort();
    bubbleSort.sort(x)  

def dInsertionSort(x):
    
    insertionSort = InsertionSort();
    insertionSort.sort(x)
   
    
def dHeapSort(x):
    
    heapSort = HeapSort(x)
    x = heapSort.sort()
    #This will sort from highest>lowest
    
def dMergeSort(x):
    
    mergeSort = MergeSort(x)
    mergeSort.sort()
    
def dQuickSort(x):
    
    quickSort = QuickSort(x)
    quickSort.start()
    
def dRandomizedQuickSort(x):
    
    randomizedQuickSort = RandomizedQuickSort(x)
    randomizedQuickSort.start()
    
def dCountingSort(x):
    
    countingSort = CountingSort(x)
    x = countingSort.sort()
    
def dRadixSort(x):
    
    radixSort = RadixSort(x)
    x = radixSort.sort()
    
def dShellSort(x):
    
    shellSort = ShellSort(x)
    shellSort.sort()
    

if __name__ == '__main__':
    print("Sorting program")
    n = int(input("Choose n: "))
    print("Sort options: ")
    print("1 for Bubble Sort")
    print("2 for Insertion Sort")
    print("3 for Heap Sort")
    print("4 for Merge Sort")
    print("5 for Quick Sort")
    print("6 for Randomized Quick Sort")
    print("7 for Radix Sort")
    print("8 for Counting Sort")
    print("9 for Shell Sort")
    choice = int(input("Choose the sort option: "))
    #list of n random inputs
    list = []
    for i in range(n):
        list.append(random.randint(1,n))
    
    print("Current list: ")
    
    print(list)
        
    dict = {1: "dBubbleSort(list)", 2:"dInsertionSort(list)", 3:"dHeapSort(list)",4:"dMergeSort(list)",5:"dQuickSort(list)",6:"dRandomizedQuickSort(list)",
            7:"dRadixSort(list)",8:"dCountingSort(list)",9:"dShellSort(list)"}
    start = timer()
    eval(dict[choice])
    end = timer()
    print("List after sort: ")
    print(list)
    print("Elapse time is: " + (end - start).__str__())