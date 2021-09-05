import sys
class Solution:
    def checkPossibility(self, nums):
        counts = 0
       
        lens = len(nums)

      

        for i in range(1, lens):
            
            if  nums[i - 1] > nums[i]:
                counts += 1

                if(i-2>=0 and nums[i-2] > nums[i]):
                    nums[i] = nums[i-1]


            if counts > 1:
                return False

               
                
                


        return True
                          

if __name__ == "__main__":
    solution = Solution()
    nums1 = [ 1, 3, 2]
    m = 4
    nums2 = [1,2,3]    
    n = 3

    result = solution.checkPossibility(nums1)

    #print(solution.ls)

    print(nums1, result)