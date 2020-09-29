import sys
class Solution:
    def findDisappearedNumbers(self, nums):
        ls = []
        dicts = {}
        for j in nums:
            dicts[j] = 1

        for i in range(len(nums)):
            if i + 1 not in dicts:
                ls.append(i+1)

        return ls

if __name__ == "__main__":
    solution = Solution()
    nums1 = [4,3,2,7,8,2,3,1]
    m = 1
    nums2 = [1,2,3]    
    n = 3

    result = solution.findDisappearedNumbers(nums1)

    #print(solution.ls)

    print(nums1, result)