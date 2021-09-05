import sys
class Solution:
    def sortedSquares(self, A):
        return sorted(list(map(lambda x: x**2, A)))

        return True

        
       

if __name__ == "__main__":
    solution = Solution()
    nums1 = [9,8,7,6,5,4,3,2,1,0]
    m = 4
    nums2 = [1,2,3]    
    n = 3

    result = solution.validMountainArray(nums1)

    #print(solution.ls)

    print(nums1, result)