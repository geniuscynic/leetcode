import sys
class Solution:
    def maxProfit(self, prices):

        lens = len(prices)

        m = 0
        for i in range(lens):
            for j in range(i, lens):
                m = max(m, prices[j] - prices[i])

                
        return m


    def maxProfit_1(self, prices):

        p = 0
        temp = 0
        
        for i in range(1, len(prices)):
            temp = max(temp, prices[i] - prices[p])

            if(prices[i] < prices[p] ):
                p = i
           
        return temp
        

if __name__ == "__main__":
    solution = Solution()
    nums1 = [7,6,4,3,1]
    m = 3
    nums2 = [1,2,3]    
    n = 3

    result = solution.maxProfit_1(nums1)

    #print(solution.ls)

    print(nums1, result)