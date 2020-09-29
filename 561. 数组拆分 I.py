import sys
class Solution:
    
    def arrayPairSum(self, nums):
        nums.sort()

        res = 0
        for i in range(0, len(nums), 2):
            res += nums[i]

        return res
                        

if __name__ == "__main__":
    solution = Solution()
    nums1 = [1,4,3,2]
    m = 4
    nums2 = [1,2,3]    
    n = 3

    result = solution.arrayPairSum(nums1)

    #print(solution.ls)

    print(nums1, result)