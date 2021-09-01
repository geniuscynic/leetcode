import sys
from collections import defaultdict
from collections import Counter
import re
class Solution:
    def mostCommonWord(self, paragraph, banned):
        ban = "(" + "|".join(banned) + ")\W"

        paragraph = paragraph.lower()
        res = re.sub(ban, " ", paragraph)
      
        res = re.split("[\s\W]+", res)
        print(res)

        maxs = 0
        s = ""
        dicts = {}
        for i in res:
            if i == "":
                continue
            
            if i in dicts:
                dicts[i] += 1
            else:
                dicts[i] = 1

            if dicts[i] > maxs:
                maxs = dicts[i]
                s = i

        return s
      
            
            
if __name__ == "__main__":
    solution = Solution()
    nums1 = "Bob. hIt, baLl"
    m = ["bob", "hit"]

    nums2 = [1,2,3]    
    n = 3

    result = solution.mostCommonWord(nums1, m)

    #print(solution.ls)

    print(result)