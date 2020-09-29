import sys
class Solution:
    def findUnsortedSubarray(self, nums):
        lens = len(nums)
        
        start, end =  0, - 1
        mins = nums[end]
        maxs = nums[0]
        for i in range(lens):
            if nums[i] >= maxs:
                maxs = nums[i]
            else:
                end = i


            #print("a", nums[lens - i - 1], mins)
            if nums[lens - i - 1] <= mins:
                mins =  nums[lens - i - 1]
            else:
                start = lens - i - 1


            print("b",start, end)
            
           

        #print(q)
        return end - start + 1
        


            

                        

if __name__ == "__main__":
    solution = Solution()
    nums1 = [1,2,3,3,3]


    m = 3
    nums2 = [1,2,3]    
    n = 3

    result = solution.findUnsortedSubarray(nums1)

    #print(solution.ls)

    print(nums1, result)