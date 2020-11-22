import sys
from collections import defaultdict
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
            
        return sorted(s) == sorted(t)
       


if __name__ == "__main__":
    solution = Solution()
    nums1 = 2
    m = 3

    nums2 = [1,2,3]    
    n = 3

    result = solution.numWaterBottles(nums1, m)

    #print(solution.ls)

    print( result)