import sys
from collections import defaultdict
from collections import Counter
import math
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        len1, len2 = len(a), len(b)

        if len1 == len2:
            if a == b:
                return -1
            else:
                return len1

        
        return max(len1, len2)
        
    
        



if __name__ == "__main__":
    solution = Solution()
    nums1 = "--a-a-a-a--"

    m = 2
    nums2 = [1,2,3]    
    n = 3

    result = solution.licenseKeyFormatting(nums1, m)

    #print(solution.ls)

    print(result)