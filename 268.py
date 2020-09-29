import sys
class Solution:
        def missingNumber(self, nums):
            num_set = set(nums)
            n = len(nums) + 1
            for number in range(n):
                if number not in num_set:
                    return number


                

            
           
          
                #print(i, j, nums, prev, next)

          
            
    
if __name__ == "__main__":
    solution = Solution()
    nums1 = [9,6,4,2,3,5,7,0,1]
    m = 2
    nums2 = [1,2,3]    
    n = 3

    result = solution.missingNumber(nums1)

    #print(solution.ls)

    print(nums1, result)