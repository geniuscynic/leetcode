import sys
from collections import defaultdict
from collections import Counter
import re
class Solution:
    def judgeCircle(self, moves):
        dicts = Counter(moves)

        u = 0 if "U" not in dicts else dicts["U"]
        d = 0 if "D" not in dicts else dicts["D"]

        l = 0 if "L" not in dicts else dicts["L"]
        r = 0 if "R" not in dicts else dicts["R"]

        if u == d and l == r:
            return True

        return False
        


            
            
            
if __name__ == "__main__":
    solution = Solution()
    nums1 = "Let's take LeetCode contest"
    m = 2

    nums2 = [1,2,3]    
    n = 3

    result = solution.reverseWords(nums1)

    #print(solution.ls)

    print(nums1, result)