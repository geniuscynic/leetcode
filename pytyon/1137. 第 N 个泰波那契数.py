import sys
from collections import defaultdict
from collections import Counter
import re
class Solution:
    dicts = {}
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0

        if n == 1:
            return 1

        if n == 2:
            return 1

        if n in self.dicts:
            return self.dicts[n]

        self.dicts[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)  
        return self.dicts[n]
            

            
            
            
if __name__ == "__main__":
    solution = Solution()
    nums1 = 25
    m = 2

    nums2 = [1,2,3]    
    n = 3

    result = solution.tribonacci(nums1)

    #print(solution.ls)

    print(nums1, result)