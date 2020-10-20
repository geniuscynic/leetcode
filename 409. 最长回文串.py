import sys
from collections import defaultdict
from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        dicts = Counter(s)

        res = 0
        hasOdd = 0
        for v in dicts.values():
            if v % 2 == 0:
                res += v
            else:
                res += v - 1
                hasOdd = 1

        return res + hasOdd

if __name__ == "__main__":
    solution = Solution()
    nums1 = "abccccdd"
    m = "111"

    nums2 = [1,2,3]    
    n = 3

    result = solution.longestPalindrome(nums1)

    #print(solution.ls)

    print(nums1, result)