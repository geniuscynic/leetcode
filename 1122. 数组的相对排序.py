import sys
class Solution:

   def mysowr(self, x, arr2, lens):
        

        if x in arr2:
           return arr2.index(x)
        else:
            return x + lens

   def relativeSortArray(self, arr1, arr2):
       lens = len(arr1)
       arr1.sort(key= lambda x: self.mysowr(x, arr2, lens))

       return arr1



if __name__ == "__main__":
    solution = Solution()
    nums1 = [2,3,1,3,2,4,6,7,9,2,19]
    m = [2,1,4,3,9,6]

    nums2 = [1,2,3]    
    n = 3

    result = solution.relativeSortArray(nums1, m)

    #print(solution.ls)

    print(nums1, result)