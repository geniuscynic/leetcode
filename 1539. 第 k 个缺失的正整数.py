import sys
from collections import defaultdict
from collections import Counter
from collections import deque

class Solution:
    def findKthPositive(self, arr, k):
        res = 0

        p = 1
        q = 0
        while res < k and q < len(arr):
            
            if arr[q] > p:
                p += 1
                res += 1
            else:
                p += 1
                q += 1

        print(res, p, q)

        if q < len(arr):
            return p
        else:
            return p + k - res
            


if __name__ == "__main__":
    solution = Solution()
   
   
    nums1 = [1,2]
    m = 1

    nums2 = 0
    n = 1

    result = solution.findKthPositive(nums1, m)

    #print(solution)

    print( result)