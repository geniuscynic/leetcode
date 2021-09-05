import sys
from collections import defaultdict
from collections import Counter
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        lens = len(t)
        start = 0
        counts = 0
        for t2 in s:
            for i in range(start, lens):
                if t2 == t[i]:
                    start = i + 1
                    counts += 1
                    break

        if counts == len(s):
            return True

        return False
        


                
        
             
        
if __name__ == "__main__":
    solution = Solution()
    nums1 = "hello"
    m = "111"

    nums2 = [1,2,3]    
    n = 3

    result = solution.reverseVowels(nums1)

    #print(solution.ls)

    print(nums1, result)