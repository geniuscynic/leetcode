import sys
from collections import defaultdict
from collections import Counter
import math
class Solution:
    def validPalindrome(self, s: str) -> bool:
        lens = len(s)

        p, q = 0, lens -1
       
        while p < q:
            if s[p] == s[q]:
                p += 1
                q -= 1
            else:
                break
               

        if p >= q:
            return True

        t1, t2 = p, q-1

        while t1 < t2:
            if s[t1] != s[t2]:
                break

            t1 += 1
            t2 -= 1

        if t1 >= t2:
            return True

        t1, t2 = p + 1, q

        while t1 < t2:
            if s[t1] != s[t2]:
                return False

            t1 += 1
            t2 -= 1

        return True




if __name__ == "__main__":
    solution = Solution()
    nums1 = "deeee"
    m = 1
    nums2 = [1,2,3]    
    n = 3

    result = solution.validPalindrome(nums1)

    #print(solution.ls)

    print(result)