import sys
class Solution:
    def maxSubArray(self, nums):
        result = -sys.maxsize -1 
        temp = 0

        for i in nums:
            
            temp += i

            result = max(temp, result)

            if(temp <0):
                temp=0
               
          
            
        return result

        



if __name__ == "__main__":
    solution = Solution()
    t1 =  [-2,3,1,3]
    t2 = 6

    result = solution.maxSubArray(t1)

    #print(solution.ls)

    print(t1, result)