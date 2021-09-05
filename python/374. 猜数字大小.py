import sys
from collections import defaultdict
from collections import Counter
class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n

        while left < right:
            middle = (left + right) // 2

            if guess(middle) == -1:
                right = middle
            elif guess(middle) == 1:
                if left == middle:
                    return left
            
                left = middle

            elif:
                return middle


        return left



                
        
             
        
if __name__ == "__main__":
    solution = Solution()
    nums1 = "hello"
    m = "111"

    nums2 = [1,2,3]    
    n = 3

    result = solution.reverseVowels(nums1)

    #print(solution.ls)

    print(nums1, result)