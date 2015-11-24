'''
Created on Oct 24, 2015

@author: TranBui
'''
from sort.CountingSort import CountingSort
import math
class RadixSort(object):
    '''
    classdocs
    '''

    def __init__(self, list):
            '''
            Constructor
            '''
            self.list = list
    
    def __findMax(self, list):
        if (list == []):
            return None
        else:
            max = list[0]
            for i in range(len(list)):
                if max < list[i]:
                    max = list[i]
            max = max + 1
            return max
    
    def sort(self):
        #find the largest number
        negativeList = []
        positiveList = []
        for i in range(len(self.list)):
            if self.list[i] < 0:
                negativeList.append(self.list[i])
            else:
                positiveList.append(self.list[i])
        #Get the fabs of the negativeList
        for i in range(len(negativeList)):
            negativeList[i] = math.fabs(negativeList[i])
            
        maxNeg = self.__findMax(negativeList)
        maxPos = self.__findMax(positiveList)
        #Now we will sort those 2 lists separately
        #Sorting the positive list
        if (maxPos is not None):
            exp = 1
            b = []
            for i in range(len(positiveList)):
                b.append(0)
            while (math.floor(maxPos/exp) > 0):
                b = []
                for i in range(len(positiveList)):
                    b.append(0)
                c = []
                for i in range(10):
                    c.append(0)
                for i in range(len(positiveList)):
                    c[(math.floor(positiveList[i]/exp)) % 10] += 1
                for i in range(1,10):
                    c[i] = c[i] + c[i-1]
                for i in range(len(positiveList)-1,-1,-1):           
                    b[c[(math.floor(positiveList[i]/exp)) % 10]-1] = positiveList[i]
                    c[(math.floor(positiveList[i]/exp)) % 10] -= 1
                    #print(b[c[(math.floor(positiveList[i]/exp)) % 10]-1])
                for i in range(len(positiveList)):
                    positiveList[i] = b[i]
                
                exp *= 10
            print(positiveList)
        #Sorting the negative list
        if (maxNeg is not None):
            exp = 1
            b = []
            for i in range(len(negativeList)):
                b.append(0)
            while (math.floor(maxNeg/exp) > 0):
                c = []
                for i in range(10):
                    c.append(0)
                for i in range(len(negativeList)):
                    c[(math.floor(negativeList[i]/exp)) % 10] += 1
                    b[i] = 0
                for i in range(1,10):
                    c[i] = c[i] + c[i-1]
                for i in range(len(negativeList)-1,-1,-1):
                    b[c[(math.floor(negativeList[i]/exp)) % 10]-1] = negativeList[i]
                    c[(math.floor(negativeList[i]/exp)) % 10] -= 1
                for i in range(len(negativeList)):
                    negativeList[i] = b[i]
                exp *= 10
        for i in range(len(negativeList)):
            negativeList[i] *= -1
        result = []
        for i in range(len(negativeList)-1,-1,-1):
            result.append(negativeList[i])
        result.extend(positiveList)
        return result
    