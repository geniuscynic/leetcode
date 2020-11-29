import sys
from collections import defaultdict
from collections import Counter
from collections import deque

class Solution:
    def counts(self, num):
        res = 0
        while num > 0:
            temp = num & 1
            if temp == 1:
                res += 1

            num = num >> 1
        print(num, res)
        return res

    def sortByBits(self, arr):
        arr.sort(key = lambda x: (self.counts(x), x))

        return arr

        
       


if __name__ == "__main__":
    solution = Solution()
    nums1 = [0,1,2,3,4,5,6,7,8]
    m = 2

    nums2 = 0
    n = 1

    result = solution.sortByBits(nums1)

    #print(solution.ls)

    print( result)