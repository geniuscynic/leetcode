import sys
from collections import defaultdict
from collections import Counter
import re
class Solution:
    def toGoatLatin(self, S):
        res = ""
        ss = S.split(" ")
        for i in range(len(ss)):
            if ss[i][0].lower() in ['a', 'e', 'i', 'o', 'u']:
                res += ss[i]
            else:
                res += ss[i][1:] + ss[i][0]

            res += "ma" + 'a' * (i+1) + ' '


        return res.strip()
            
               
      
            
            
if __name__ == "__main__":
    solution = Solution()
    nums1 = "The quick brown fox jumped over the lazy dog"
    m = ["bob", "hit"]

    nums2 = [1,2,3]    
    n = 3

    result = solution.toGoatLatin(nums1)

    #print(solution.ls)

    print(result)