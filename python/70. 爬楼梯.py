import sys
from collections import defaultdict
from collections import Counter

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def helper(self, n):
        if n== 1:
            return 1

        if n==0:
            return 1

        return self.helper(n - 1) + self.helper(n - 2)
    def climbStairs(self, n: int) -> int:
        x, y = 1, 1

        for _ in range(2, n+1):
            res = x + y

            y,x = res, y

        return y

                


if __name__ == "__main__":
    solution = Solution()
    nums1 = 3

    m = [1,2,3,4]

    nums2 = [1,2,3]    
    n = 3

    result = solution.climbStairs(nums1)

    #print(solution.ls)

    print(result)