import sys
class Solution:
    def isMonotonic(self, A):
        rows = len(A)
        
        asc = 0
        for i in range(1, rows):
            if asc==0:
                if(A[i-1]<A[i]):
                    asc = 1
                    continue

                if(A[i - 1] > A[i]):
                    asc = 2
                    continue

            if asc == 1 and A[i-1]>A[i]:
                return False

            if asc == 2  and A[i-1]<A[i]:
                return False

        return True

if __name__ == "__main__":
    solution = Solution()
    nums1 = [[1,2,3],[4,5,6]]
    m = 4
    nums2 = [1,2,3]    
    n = 3

    result = solution.transpose(nums1)

    #print(solution.ls)

    print(nums1, result)