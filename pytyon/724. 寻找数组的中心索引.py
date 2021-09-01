import sys
class Solution:
    def pivotIndex(self, nums):
        total = sum(nums)

        lens = len(nums)

        res = 0
        for i in range(lens):
            if res * 2 == total - nums[i]:
                return i

            res += nums[i]

        return -1
        

                          

if __name__ == "__main__":
    solution = Solution()
    nums1 = [-1,-1,-1,0,1,1]
    m = 4
    nums2 = [1,2,3]    
    n = 3

    result = solution.pivotIndex(nums1)

    #print(solution.ls)

    print(nums1, result)