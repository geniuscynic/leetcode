import sys
from collections import defaultdict
from collections import Counter
class Solution:
    def findRepeatNumber(self, nums):
        dicts = {}

        for i in nums:
            if i not in dicts:
                dicts[i] = 1
            else:
                return i


if __name__ == "__main__":
    solution = Solution()
    nums1 = [[2,1],[4,2],[6,3]]

    m = [1,2,3,4]

    nums2 = [1,2,3]    
    n = 3

    result = solution.checkStraightLine(nums1)

    #print(solution.ls)

    print(nums1, result)