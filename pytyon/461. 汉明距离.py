import sys
from collections import defaultdict
from collections import Counter
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        n = x ^ y

        res = 0
        while n !=0:
            if n & 1:
                res += 1

            n = n >> 1

        return res






if __name__ == "__main__":
    solution = Solution()
    nums1 = [10,9,8,7]

    m = [5,6,7,8]

    nums2 = [1,2,3]    
    n = 3

    result = solution.findContentChildren(nums1, m)

    #print(solution.ls)

    print(nums1, result)