import sys
class Solution:
        def f1(self, nums):
            lens = len(nums)
            temp = nums[lens - 1]

            for i in reversed(range(1, lens)):
                nums[i] = nums[i-1]

            nums[0] = temp


        def rotate(self, nums, k):
            lens = len(nums)

          
             
            start = 0
            i = 0

            k = k % lens
            while i < lens:
                prev = nums[start]    
                next = (start + k) % lens
                temp = nums[next]
                nums[next] = prev
                prev = temp
               
                print("a", nums, prev, next)
                
                while next != start:
                    next = (next + k) % lens
                    temp = nums[next]
                    nums[next] = prev
                    prev = temp
                    i += 1

                    print("b", nums, prev, next, i)
               
                
                start += 1
                i += 1
           
          
                #print(i, j, nums, prev, next)

          
            
    
if __name__ == "__main__":
    solution = Solution()
    nums1 = [-1,-100,3,99]
    m = 2
    nums2 = [1,2,3]    
    n = 3

    result = solution.rotate(nums1, m)

    #print(solution.ls)

    print(nums1, result)