import sys
class Solution:
    def dominantIndex(self, nums):
        f1,f2 = 0, 0
        lens = len(nums)

        k = 0
        for i in range(0, lens):
            if(f1 < nums[i]):
                f2 = f1
                f1 = nums[i]

                k = i
            elif(f2 < nums[i]):
                f2 = nums[i]
               

        

        if f2 == 0 or f1//f2 >=2:
            return k
        else:
            return -1


            

        

                          

if __name__ == "__main__":
    solution = Solution()
    nums1 = [0,2,0,3]
    m = 4
    nums2 = [1,2,3]    
    n = 3

    result = solution.dominantIndex(nums1)

    #print(solution.ls)

    print(nums1, result)