import sys
class Solution:
    def flipAndInvertImage(self, A):
        rows = len(A)
        cols = len(A[0])

        for i in range(rows):
            for j in range(cols // 2):
                temp = A[i][j]
               
                A[i][j] = 1 if A[i][cols - 1- j] == 0 else 0

                A[i][cols - 1- j] = 1 if temp ==0 else 0

                #print(A[i])

            if cols % 2 == 1:
                A[i][cols // 2] = 1 if A[i][cols // 2] ==0 else 0

               

        return A


        

            

if __name__ == "__main__":
    solution = Solution()
    nums1 = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    m = 4
    nums2 = [1,2,3]    
    n = 3

    result = solution.flipAndInvertImage(nums1)

    #print(solution.ls)

    print(nums1, result)