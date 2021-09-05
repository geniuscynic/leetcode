import sys
from collections import defaultdict
from collections import Counter

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        while n > 1:
            if n % 2 != 0:
                return False

            n = n >> 1

            print(n)

        return True
        


if __name__ == "__main__":
    solution = Solution()
    nums1 = 6

    m = [1,2,3,1]

    nums2 = [1,2,3]    
    n = 3

    result = solution.isPowerOfTwo(nums1)

    #print(solution.ls)

    print(result)