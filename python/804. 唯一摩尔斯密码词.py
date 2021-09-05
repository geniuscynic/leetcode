import sys
from collections import defaultdict
from collections import Counter
import re
class Solution:
    def uniqueMorseRepresentations(self, words):
        ls = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        res = set()
        for w in words:
            temp = ""
            for s in w:
                temp += ls[ord(s) - 97]

            res.add(temp)

        return len(res)
      
            
            
if __name__ == "__main__":
    solution = Solution()
    nums1 = ["gin", "zen", "gig", "msg"]
    m = 2

    nums2 = [1,2,3]    
    n = 3

    result = solution.uniqueMorseRepresentations(nums1)

    #print(solution.ls)

    print(nums1, result)