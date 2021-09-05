import sys
from collections import defaultdict
from collections import Counter
from collections import deque

class Solution:

    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()

        res = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i-1] != res:
                return False

        return True 
                
                

            
       


if __name__ == "__main__":
    solution = Solution()
    nums1 = 2
    m = 3

    nums2 = 1
    n = 2

    result = solution.allCellsDistOrder_1(nums1, m, nums2, n)

    #print(solution.ls)

    print( result)