import sys
class Solution:
    def maxProfit(self, prices):
        p = 0
        q = 0
        temp = 0
        
        for i in range(1, len(prices)):
            if(prices[i] > prices[q] ):
                q = i
            else:
                temp += prices[q] - prices[p]
                p = i
                q = i


            
        if(q == len(prices) - 1):
            temp += prices[q] - prices[p]
                
        
        return temp
        

if __name__ == "__main__":
    solution = Solution()
    nums1 = [7,1,5,3,6,4]
    m = 3
    nums2 = [1,2,3]    
    n = 3

    result = solution.maxProfit(nums1)

    #print(solution.ls)

    print(nums1, result)