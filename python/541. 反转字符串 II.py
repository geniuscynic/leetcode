import sys
from collections import defaultdict
from collections import Counter
import re
class Solution:
    def reverseStr(self, s, k):
        lens = len(s)

        ls = []
        for i in range(0, lens, 2 * k):
            ls += list(reversed(s[i:i + k ]))
            ls += list(s[i+ k : i + 2 * k ])

        return "".join(ls)




            
            
            
if __name__ == "__main__":
    solution = Solution()
    nums1 = "abcdefg"
    m = 2

    nums2 = [1,2,3]    
    n = 3

    result = solution.reverseStr(nums1, m)

    #print(solution.ls)

    print(nums1, result)