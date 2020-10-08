import sys
from collections import defaultdict
from collections import Counter
class Solution:
    def fib(self, n):

        x,y = 0,1
        for i in range(2, n + 1):
            x, y = y, x+y

            y = y % 1000000007


        return y

        


if __name__ == "__main__":
    solution = Solution()
    nums1 = 5

    m = [1,2,3,4]

    nums2 = [1,2,3]    
    n = 3

    result = solution.fib(nums1)

    #print(solution.ls)

    print(nums1, result)