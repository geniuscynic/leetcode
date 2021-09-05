import sys
from collections import defaultdict
from collections import Counter
class Solution:
    dicts = {}
    def numWays(self, n):
        if n == 0:
            return 1

        if n==1:
            return 1

        if n==2:
            return 2

        if n in self.dicts:
            return self.dicts[n]

        self.dicts[n] = (self.numWays(n-1) + self.numWays(n-2)) % 1000000007

        return self.dicts[n] 

        


if __name__ == "__main__":
    solution = Solution()
    nums1 = 44

    m = [1,2,3,4]

    nums2 = [1,2,3]    
    n = 3

    result = solution.numWays(nums1)

    #print(solution.ls)

    print(nums1, result)