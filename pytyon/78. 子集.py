import sys
from collections import defaultdict
from collections import Counter
class Solution:
    ls = []
    def hepper(self, n, nums):
        if n == 1:
            self.ls += nums
            return []

        #if n == 2:
            #return [[nums[0]],[nums[1]],nums]


        #self.ls.append(nums.pop)
        temp = nums.pop()
        ls2 = self.hepper(n - 1,nums)

        for i in ls2:
            ls += [i, temp]

        ls2 += temp


        return 
        
        
            

    def subsets(self, nums):
        lens = len(nums)

        
    
        ls += self.hepper(lens, nums)
        return ls


                

        
if __name__ == "__main__":
    solution = Solution()
    nums1 = [1,2, 3]
    m = "111"

    nums2 = [1,2,3]    
    n = 3

    result = solution.subsets(nums1)

    #print(solution.ls)

    print(nums1, result)