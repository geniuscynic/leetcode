import sys
class Solution:
    def maximumProduct(self, nums):
        nums.sort()

        return max(nums[0] * nums[1] * nums[nums.length - 1], nums[nums.length - 1] * nums[nums.length - 2] * nums[nums.length - 3])


                          

if __name__ == "__main__":
    solution = Solution()
    nums1 = [1,0,0,0,0,0,1]
    m = 2
    nums2 = [1,2,3]    
    n = 3

    result = solution.canPlaceFlowers(nums1, m)

    #print(solution.ls)

    print(nums1, result)