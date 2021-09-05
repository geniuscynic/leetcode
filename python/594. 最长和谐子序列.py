import sys
from collections import defaultdict
from collections import Counter
import math
class Solution:
    def findLHS(self, nums):
        nums.sort()

        lens = len(nums)
        res = 0
       
        minsindex = 0
        for i in range(1,lens):
            if nums[i] - nums[minsindex] == 1:
                if i < lens - 1 and nums[i + 1] == nums[i]:
                    continue
                else:
                    res = max(res, i - minsindex + 1)
                    
            elif nums[i] - nums[minsindex] > 1:
                minsindex += 1
                while nums[i] - nums[minsindex] > 1:
                    minsindex += 1
                

               
        #print(minsindex)
        #res = max(res, len(nums) -  minsindex)

        return res

        
        



if __name__ == "__main__":
    solution = Solution()
    nums1 = [1,1, 2, 2]

    m = 2
    nums2 = [1,2,3]    
    n = 3

    result = solution.findLHS(nums1)

    #print(solution.ls)

    print(result)