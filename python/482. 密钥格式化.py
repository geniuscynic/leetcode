import sys
from collections import defaultdict
from collections import Counter
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        lens = len(S)

        ls = []

        res = 0
        for i in reversed(range(lens)):
            s = S[i]

            if s == "-":
                continue

            if s.islower():
                s = s.upper()

            res += 1
            ls.append(s)

            if res == K:
                res = 0
                ls.append("-")

        print(ls)
        ls.reverse()
        
        return "".join(ls).strip("-")

if __name__ == "__main__":
    solution = Solution()
    nums1 = "--a-a-a-a--"

    m = 2
    nums2 = [1,2,3]    
    n = 3

    result = solution.licenseKeyFormatting(nums1, m)

    #print(solution.ls)

    print(result)