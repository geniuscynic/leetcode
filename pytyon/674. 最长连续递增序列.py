import sys
class Solution:
    def findLengthOfLCIS(self, nums):
        counts = 0
        index = 0

        lens = len(nums)

        for i in range(1, lens):
            if  nums[i - 1] >= nums[i]:

                counts= max(counts, i - index)

                index = i

           
        counts= max(counts, lens - index)
 
        return counts
                          

if __name__ == "__main__":
    solution = Solution()
    nums1 = [1,3,5,7]
    m = 4
    nums2 = [1,2,3]    
    n = 3

    result = solution.findLengthOfLCIS(nums1)

    #print(solution.ls)

    print(nums1, result)