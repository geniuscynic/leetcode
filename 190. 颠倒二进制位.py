import sys
from collections import defaultdict
from collections import Counter


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for _ in range(32):
            #print(n & 1)
            res = (res << 1) + (n & 1)

            n = n >> 1

            #print(res, n)
        return res
                


if __name__ == "__main__":
    solution = Solution()
    nums1 = 1

    m = [1,2,3,4]

    nums2 = [1,2,3]    
    n = 3

    result = solution.reverseBits(nums1)

    #print(solution.ls)

    print(nums1, result)