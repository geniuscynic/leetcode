import sys
from collections import defaultdict
from collections import Counter
from collections import deque
from random import randint
import timeit

class Solution:
    #生成随机数列
    def generateRandomArray(self, n, min, max):
        return [randint(min, max) for x in range(n)]

    #生成基本有序的数列
    def generateNearlyOrderedArray(self, n, swapTimes):
        arr = []
        for i in range(n):
            arr.append(i)
        for j in range(swapTimes):
            posx = randint(0, n-1)
            posy = randint(0, n-1)
            arr[posx], arr[posy] = arr[posy], arr[posx]
        return arr

    #判断数列是否有序（算法是否正确）
    def isSorted(self, alist):
        for i in range(0, len(alist)-1):
            if alist[i] > alist[i+1]:
                print(alist)
                return False
        return True

    #测试算法性能（耗费时间）
    # func表示要检测的算法函数，alist为传入的数列
    def testSort(self, func, alist):
       
        alist =  func(alist)
        assert self.isSorted(alist), "排序算法错误\n"

   


    #冒泡排序（Bubble Sort）
    def bubbleSort(self, alist):
        lens = len(alist)
        for i in range(lens):
            for j in range(1, lens - i):
                if(alist[j-1] > alist[j]):
                    alist[j - 1], alist[j] = alist[j], alist[j - 1]
        
        return alist

    #选择排序
    def selectionSort(self, alist):
        lens = len(alist)
        
        for i in range(lens):
            minindex = i

            for j in range(i, lens):
                if(alist[j] < alist[minindex]):
                    minindex = j

            alist[i], alist[minindex] = alist[minindex],alist[i]
        
        return 
        

    #插入排序
    def insertionSort(self, alist):
        lens = len(alist)
        
        print(alist)

        for i in range(lens-1):
            current = alist[i + 1]
            preIndex = i
            for j in reversed(range(i)):
                preIndex -= 1

                if current < alist[j]:
                    alist[j + 1] = alist[j]
                else:
                    break

            #if(preIndex != i - 1):
            alist[preIndex + 1] = current
            print(alist)


        return alist

   

def testTime(func, alist):
        func(alist)
        t1 = timeit.Timer('func(alist)', 'from __main__ import testTime')
        print('某种排序算法：', t1.timeit(number=1))



def testBubbleSort():
    solution.testSort(solution.bubbleSort, arrlist1[:])
    solution.testSort(solution.bubbleSort, arrlist2[:])

    t1 = timeit.Timer('solution.bubbleSort(arrlist1[:])', 'from __main__ import solution, arrlist1')
    print('冒泡排序算法：', t1.timeit(1000))

    t2 = timeit.Timer('solution.bubbleSort(arrlist2[:])', 'from __main__ import solution, arrlist2')
    print('冒泡排序算法：', t2.timeit(1000))


def testSelectionSort():
    solution.testSort(solution.selectionSort, arrlist1[:])
    solution.testSort(solution.selectionSort, arrlist2[:])

    t1 = timeit.Timer('solution.selectionSort(arrlist1[:])', 'from __main__ import solution, arrlist1')
    print('选择排序算法：', t1.timeit(1000))

    t2 = timeit.Timer('solution.selectionSort(arrlist2[:])', 'from __main__ import solution, arrlist2')
    print('选择排序算法：', t2.timeit(1000))

def testInsertionSort():
    solution.testSort(solution.insertionSort, [10, 6,9, 8,7 ])
    #solution.testSort(solution.insertionSort, arrlist2[:])

    #t1 = timeit.Timer('solution.insertionSort(arrlist1[:])', 'from __main__ import solution, arrlist1')
    #print('选择排序算法：', t1.timeit(1000))

    #t2 = timeit.Timer('solution.insertionSort(arrlist2[:])', 'from __main__ import solution, arrlist2')
    #print('选择排序算法：', t2.timeit(1000))


if __name__ == "__main__":
    solution = Solution()
    nums1 = 10
    mins = 1
    maxs = 100
    swapTimes = 10

    nums2 = 1
    n = 2

    arrlist1 = solution.generateRandomArray(nums1, mins, maxs)
    arrlist2 = solution.generateNearlyOrderedArray(nums1, swapTimes)

    #testBubbleSort()
    #testSelectionSort()
    testInsertionSort()


    #print(arrlist1)

    #testTime(solution.bubbleSort, arrlist1)
    #testTime(solution.bubbleSort, arrlist2)
    #print(solution.ls)

    #print( result1, result2)




