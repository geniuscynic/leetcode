import sys
class Solution:
    def validMountainArray(self, A):
        lens = len(A)

        if lens < 3:
            return False

        sorted=1
        index = 0
        for i in range(lens-1):
            if sorted == 1 and  A[i] >= A[i+1]:
                sorted = 2
                if i ==0:
                    return False

            if sorted == 2 and A[i] <= A[i+1]:
                return False

        if sorted ==1:
            return False

        if index == 0:
            return False

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