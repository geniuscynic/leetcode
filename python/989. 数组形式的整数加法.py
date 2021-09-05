import sys
class Solution:
    def addToArrayForm(self, A, K):
        lens  = len(A)

        res = 0
        for i in range(lens):
            res += A[i] * (10 ** (lens - i -1))

        res += K
            
        res = list(map(int, str(res)))
        return res

        
       

if __name__ == "__main__":
    solution = Solution()
    nums1 = [1,2,0,0]
    m = 34

    nums2 = [1,2,3]    
    n = 3

    result = solution.addToArrayForm(nums1, m)

    #print(solution.ls)

    print(nums1, result)