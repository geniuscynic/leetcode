import sys
class Solution:
        def containsDuplicate(self, nums):
            dicts = {}

            for i in nums:
                if i in dicts:
                    return True
                else:
                    dicts[i] = 1


            return False
           
          
                #print(i, j, nums, prev, next)

          
            
    
if __name__ == "__main__":
    solution = Solution()
    nums1 = [1,2,3,1]
    m = 2
    nums2 = [1,2,3]    
    n = 3

    result = solution.containsDuplicate(nums1)

    #print(solution.ls)

    print(nums1, result)