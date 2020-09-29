import sys
class Solution:
        def moveZeroes(self, nums):
            lens = len(nums)
            p = 0
            q = lens - 1

            while p < q:
                if nums[p] != 0:
                    p += 1
                    continue

                for i in range(p + 1, q + 1):
                    nums[i - 1] = nums[i]
                
                nums[q] = 0
                q -= 1

        def moveZeroes_1(self, nums):
            lens = len(nums)
            
            zero = 0
            #index = -1

            for i in range(lens):
                if nums[i] == 0:
                    zero += 1
                    #index = i
                    continue


                if zero > 0:
                    nums[i - zero] = nums[i]

            for i in range(zero):
                nums[lens - 1 - i] = 0
            

                


                #print(i, j, nums, prev, next)

          
            
    
if __name__ == "__main__":
    solution = Solution()
    nums1 = [0,1,0,3,12]
    m = 2
    nums2 = [1,2,3]    
    n = 3

    result = solution.moveZeroes_1(nums1)

    #print(solution.ls)

    print(nums1, result)