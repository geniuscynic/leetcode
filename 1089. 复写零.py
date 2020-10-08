import sys
class Solution:
    def duplicateZeros(self, arr):
        lens = len(arr)
        
        index = -1
        prev = 0
        for i in range(0, lens):

            if arr[i] == 0:

                temp = arr[i]
                arr[i] = prev
                prev = temp

                index = i
                continue
               

            if index != -1:
                temp = arr[i]
                arr[i] = prev
                prev = temp
                
                
            print(arr, prev)



if __name__ == "__main__":
    solution = Solution()
    nums1 = [1,0,2,3,0,4,5,0]
    m = 34

    nums2 = [1,2,3]    
    n = 3

    result = solution.duplicateZeros(nums1)

    #print(solution.ls)

    print(nums1, result)