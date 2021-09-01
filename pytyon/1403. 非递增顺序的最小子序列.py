import sys
from collections import defaultdict
from collections import Counter
class Solution:
    def minSubsequence(self, nums):
        #sorted(nums, reverse=True)
        nums.sort(reverse=True)
        total = sum(nums)

        res = 0
        for i in range(len(nums)):
            res += nums[i]

            print(i, ":", res, total - res)
            if res > total - res:
                return nums[:i+1]

        return nums



if __name__ == "__main__":
    solution = Solution()
    nums1 = [4,3,10,9,8]

    m = [1,2,3,4]

    nums2 = [1,2,3]    
    n = 3

    result = solution.minSubsequence(nums1)

    #print(solution.ls)

    print(nums1, result)