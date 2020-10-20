import sys
from collections import defaultdict
from collections import Counter
class Solution:
    def arrangeCoins(self, n: int) -> int:
        line = 0
       
        while True:
            total = line * (line + 1) / 2 + line

            if total >= n:
                break

            line += 1

        return line

    def arrangeCoins_1(self, n: int) -> int:
        left = 1
        right = n
       
        #if n == 0:
         #   return 0

        while left <= right:

            middle = (left + right) // 2
            
            total = middle * (middle + 1) // 2

            if total > n:
                right = middle + 1
            elif total == n:
                return middle
            elif total < n and total + middle >= n:
                return middle
            else:
                left += 1
            
        return right




if __name__ == "__main__":
    solution = Solution()
    nums1 = 100
    m = "111"

    nums2 = [1,2,3]    
    n = 3

    result = solution.arrangeCoins_1(nums1)

    #print(solution.ls)

    print(nums1, result)