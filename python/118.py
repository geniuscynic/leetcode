class Solution:
    def generate(self, numRows):
        ls = []
        for i in range(numRows):
            temp = [1 for x in range(i + 1)]

            for j in range(1, i//2 + 1):
                left = 0
                #if(j - 1 >=0):
                left = ls[i - 1][j - 1]

                #right = 0
                #if(j <= i - 1):
                    #print(i, j)
                right =  ls[i - 1][j] 
                
                
                temp[j] = left + right
                temp[i - j] = temp[j]
        
            ls.append(temp)
            #print(ls)


        return ls

if __name__ == "__main__":
    solution = Solution()
    nums1 = 5
    m = 3
    nums2 = [1,2,3]    
    n = 3

    result = solution.generate(nums1)

    #print(solution.ls)

    print(nums1, result)