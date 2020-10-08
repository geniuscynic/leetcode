import sys
from collections import defaultdict
from collections import Counter
class Solution:
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        
        lens = len(needle)
        for i in range(0, len(haystack)-lens + 1):
            if haystack[i:i + lens] == needle:
                return i

        return -1

if __name__ == "__main__":
    solution = Solution()
    nums1 = "mississippi"
    m = "issi"

    nums2 = [1,2,3]    
    n = 3

    result = solution.strStr(nums1, m)

    #print(solution.ls)

    print(nums1, result)