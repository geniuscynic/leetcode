import sys
from collections import defaultdict
from collections import Counter
import math
class Solution:
    def findErrorNums(self, nums):
        lens = len(nums)

        res = 0

        missval = 0
        for i in range(lens):
            temp = nums[i]

            t = abs(temp)
           
            res += i + 1 - t

            if nums[t - 1] < 0:
                missval = t
            else:
                nums[t - 1] = -nums[t - 1]

        
        return [missval, res + missval]



if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 2 , 2, 4]
    m = 1
    nums2 = [1,2,3]    
    n = 3

    result = solution.findErrorNums(nums1)

    #print(solution.ls)

    print(result)