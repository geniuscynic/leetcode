import sys
from collections import defaultdict
from collections import Counter
import re
class Solution:
    def reverseWords(self, s):
        ls = s.split()

        
        for i in range(len(ls)):
            ls[i] = ls[i][::-1]


        return " ".join(ls)

            
            
            
if __name__ == "__main__":
    solution = Solution()
    nums1 = "Let's take LeetCode contest"
    m = 2

    nums2 = [1,2,3]    
    n = 3

    result = solution.reverseWords(nums1)

    #print(solution.ls)

    print(nums1, result)