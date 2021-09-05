import sys
class Solution:

    dicts = {}

    def step(self, cost, index):

        if index < 0:
            return 0

        if index == 0:
            self.dicts[index] = 0

        if index == 1:
            self.dicts[index] = 0

        if index in self.dicts:
            return self.dicts[index]


        
        self.dicts[index] = min(self.step(cost, index - 1) + cost[index - 1], self.step(cost, index - 2) + cost[index - 2] )
        #print(self.dicts)

        return self.dicts[index]


    def minCostClimbingStairs(self, cost):
        
        return self.step(cost, len(cost))
        

                          

if __name__ == "__main__":
    solution = Solution()
    nums1 = [0, 0, 1,1]
    m = 4
    nums2 = [1,2,3]    
    n = 3

    result = solution.minCostClimbingStairs(nums1)

    #print(solution.ls)

    print(nums1, result)