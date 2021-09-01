import sys
class Solution:
    def stepMaxAverage(self, nums, k, index):
        if k + index > len(nums):
            return -sys.maxsize- 1

        avg1 = sum(nums[index:index + k]) / k
        
        #print(avg1, index)
        return max(avg1, self.stepMaxAverage(nums, k, index +1))

    def findMaxAverage(self, nums, k):
        return self.stepMaxAverage(nums, k, 0)

    def findMaxAverage_1(self, nums, k):
        
        lens = len(nums)

        temp = sum(nums[:k])
        res = temp

        for i in range(k, lens):
            
            temp = temp + nums[i] - nums[i - k]
            
            res = max(res, temp)


        return res / k
        

            
            

        



                          

if __name__ == "__main__":
    solution = Solution()
    nums1 = [1,12,-5,-6,50,3]
    m = 4
    nums2 = [1,2,3]    
    n = 3

    result = solution.findMaxAverage_1(nums1, m)

    #print(solution.ls)

    print(nums1, result)