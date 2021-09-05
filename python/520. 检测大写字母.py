import sys
from collections import defaultdict
from collections import Counter
import re
class Solution:
    def detectCapitalUse(self, word):
        lens = len(word)

        f = word[0]

        isf2upper = False
        for i in range(1,lens):
            w = word[i]
            if f.islower() and w.isupper():
                return False

            if i == 1 and w.isupper():
                isf2upper = True

            if isf2upper and w.islower():
                return False

            if not isf2upper and w.isupper():
                return False

        
        return True
            

            
            
            
if __name__ == "__main__":
    solution = Solution()
    nums1 = "FlaG"
    m = "1"

    nums2 = [1,2,3]    
    n = 3

    result = solution.detectCapitalUse(nums1)

    #print(solution.ls)

    print(nums1, result)