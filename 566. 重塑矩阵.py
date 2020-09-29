import sys
class Solution:
    def matrixReshape(self, nums, r, c):
        row = len(nums)
        col = len(nums[0])

        if row * col != r * c:
            return nums

        if row == r:
            return nums
            
        res = []
        ls=[]
        for i in range(row):
            for j in range(col):
                k = (i * col) + (j + 1) 
                
                ls.append(nums[i][j])


                if k % c == 0:
                    res.append(ls)
                    ls = []
                
                print(k, res)

        return res
                        

if __name__ == "__main__":
    solution = Solution()
    nums1 = [[1,2,3],[4,5,6],[7,8,9]]


    m = 3
    nums2 = [1,2,3]    
    n = 3

    result = solution.matrixReshape(nums1, m, n)

    #print(solution.ls)

    print(nums1, result)