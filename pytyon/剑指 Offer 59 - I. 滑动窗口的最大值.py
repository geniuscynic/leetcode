import sys
from collections import defaultdict
from collections import Counter
class Solution:
    def maxSlidingWindow(self, nums, k):
        lens = len(nums)

        i = 0

        ls= []
        maxs = - sys.maxsize - 1
        index = -1

        if k == 0:
            return []
        while i < lens- k + 1:
            if index < i:
                maxs = - sys.maxsize - 1
                for j in range(k):
                    if nums[j + i] > maxs:
                        maxs = nums[i + j]
                        index = j
            else:
                if nums[i+k-1] > maxs:
                    maxs = nums[i + j]
                    index = i + k - 1

            i += 1
            
            ls.append(maxs)

        return ls

        



if __name__ == "__main__":
    solution = Solution()
    nums1 =  [1,-1]

    m = 1

    nums2 = [1,2,3]    
    n = 3

    result = solution.maxSlidingWindow(nums1, m)

    #print(solution.ls)

    print(nums1, result)