import sys
from collections import defaultdict
from collections import Counter
import math
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        minx = m
        miny = n
        for op in ops:
            minx = min(minx, op[0])
            miny = min(miny, op[1])


        return minx * miny

        
        



if __name__ == "__main__":
    solution = Solution()
    nums1 = [1,1, 2, 2]

    m = 2
    nums2 = [1,2,3]    
    n = 3

    result = solution.findLHS(nums1)

    #print(solution.ls)

    print(result)