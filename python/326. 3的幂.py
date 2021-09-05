import sys
from collections import defaultdict
from collections import Counter

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True

        if n == 3:
            return True

        if n % 3 != 0:
            return False

        res = 0

        while n !=0:
            res += n % 10

            n = n // 10

        return True if res % 9 == 0 else False


if __name__ == "__main__":
    solution = Solution()
    nums1 = 49979

    m = [1,2,3,1]

    nums2 = [1,2,3]    
    n = 3

    result = solution.countPrimes(nums1)

    #print(solution.ls)

    print(result)