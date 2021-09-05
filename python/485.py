import sys
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        index = -1
        counts = 0

        for i in range(len(nums) + 1):
            if i ==  len(nums) or nums[i] == 0:
                c = i - index - 1
                counts = max(c, counts)
                index = i

        return counts

if __name__ == "__main__":
    solution = Solution()
    nums1 = [1,1,0,1,1,1]
    m = 1
    nums2 = [1,2,3]    
    n = 3

    result = solution.findMaxConsecutiveOnes(nums1)

    #print(solution.ls)

    print(nums1, result)