import sys
class Solution:
        def containsNearbyDuplicate(self, nums, k):
            dicts = {}

            for i in range(len(nums)):
                j = nums[i]

                
                if j in dicts and i - dicts[j] <=k:
                    return True
                    
                

                dicts[j] = i


            return False
           
          
                #print(i, j, nums, prev, next)

          
            
    
if __name__ == "__main__":
    solution = Solution()
    nums1 = [1,2,3,1,2,3]
    m = 2
    nums2 = [1,2,3]    
    n = 3

    result = solution.containsNearbyDuplicate(nums1, m)

    #print(solution.ls)

    print(nums1, result)