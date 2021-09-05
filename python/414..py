import sys
class Solution:
        def thirdMax(self, nums):
            #ls = []
            #lens = nums[0]

            f1 = -sys.maxsize - 1
            f2 = -sys.maxsize - 1
            f3 = -sys.maxsize - 1
            for j in nums:
                #j = nums[i]

                if j > f3:
                    f1 = f2
                    f2 = f3
                    f3 = j
                elif j == f3:
                    continue
                elif j > f2:
                    f1 = f2
                    f2 = j
                elif j == f2:
                    continue
                elif j> f1:
                    f1 = j
               

            if f1 == -sys.maxsize -1:
                return f3
            else:
                return f1
    
if __name__ == "__main__":
    solution = Solution()
    nums1 = [3, 2, 1]
    m = 1
    nums2 = [1,2,3]    
    n = 3

    result = solution.thirdMax(nums1)

    #print(solution.ls)

    print(nums1, result)