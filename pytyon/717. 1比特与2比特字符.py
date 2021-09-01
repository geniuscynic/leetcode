import sys
class Solution:
    def isOneBitCharacter(self, bits):

        lens = len(bits)

        if bits[-1] == 1:
            return False
        
        i= 0
        index= -1
        while i < lens:
            if bits[i] == 1:
                i += 1
                index = i 


            i += 1   

            
        if index == lens - 1:
            return False

        return True

                          

if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 0, 0]
    m = 4
    nums2 = [1,2,3]    
    n = 3

    result = solution.findLengthOfLCIS(nums1)

    #print(solution.ls)

    print(nums1, result)