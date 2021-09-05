import sys
class Solution:
    def transpose(self, A):
        rows = len(A)
        cols = len(A[0])

        ls = []
        for j in range(cols):
            temp = []
            for i in range(rows):
                temp.append(A[i][j])

            ls.append(temp)

            
        return ls

if __name__ == "__main__":
    solution = Solution()
    nums1 = [[1,2,3],[4,5,6]]
    m = 4
    nums2 = [1,2,3]    
    n = 3

    result = solution.transpose(nums1)

    #print(solution.ls)

    print(nums1, result)