import sys
from collections import defaultdict
from collections import Counter
import re
class Solution:
    def toLowerCase(self, str):
        res = ''
        for i in str:
            if 65 <= ord(i) <= 90:
                res += chr(ord(i)+32)
            else:
                res += i
        return res

            
            
            
if __name__ == "__main__":
    solution = Solution()
    nums1 = "Let's take LeetCode contest"
    m = 2

    nums2 = [1,2,3]    
    n = 3

    result = solution.reverseWords(nums1)

    #print(solution.ls)

    print(nums1, result)