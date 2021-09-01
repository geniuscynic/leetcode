import sys
from collections import defaultdict
from collections import Counter

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def helper(self, n, ls):

        for i in ls:
            if n == i:
                return True

            if n % i == 0:
                return False

        left = ls[-1]

        if left > n:
            return True

        for i in range(left + 1, n // 2):
            if n % i == 0:
                return False

        ls.append(n)

        return True

    def countPrimes(self, n: int) -> int:

        ls = [2,3,5,7]
        res = 0
        for i in range(2, n):
            if self.helper(i, ls):
                res +=1

        #print(ls)
        return res


if __name__ == "__main__":
    solution = Solution()
    nums1 = 49979

    m = [1,2,3,1]

    nums2 = [1,2,3]    
    n = 3

    result = solution.countPrimes(nums1)

    #print(solution.ls)

    print(result)