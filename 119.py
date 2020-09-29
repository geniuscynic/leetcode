class Solution:
    def generate(self, numRows):
        
        temp = [1]

        for i in range(1, numRows):
            temp.insert(0,0)

            for j in range(i):
                print(i, j, temp)
                temp[j] = temp[j] + temp[j + 1]
            
        
            
            #print(ls)


        return temp

if __name__ == "__main__":
    solution = Solution()
    nums1 = 4
    m = 3
    nums2 = [1,2,3]    
    n = 3

    result = solution.generate(nums1)

    #print(solution.ls)

    print(nums1, result)