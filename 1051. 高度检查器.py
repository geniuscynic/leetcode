import sys
class Solution:
    def heightChecker(self, heights):
        ls = sorted(heights)

        counts = 0
        for i in len(ls):
            if ls[i] != heights[i]:
                counts += 1

        return counts



if __name__ == "__main__":
    solution = Solution()
    nums1 = [1,-1,1,-1]
    m = 34

    nums2 = [1,2,3]    
    n = 3

    result = solution.canThreePartsEqualSum(nums1)

    #print(solution.ls)

    print(nums1, result)