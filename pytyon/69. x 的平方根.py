import sys
from collections import defaultdict
from collections import Counter
from collections import deque

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mySqrt(self, x: int) -> int:

        low = 0
        higth = x
        

        while low != higth:
            
            middle = (low + higth) // 2
            if low == middle:
                break

            temp = middle ** 2

            print(low, higth, middle, temp)
            if temp == x:
                return middle
            elif temp > x:
                higth = middle
            elif temp < x:
                low = middle

        return low


if __name__ == "__main__":
    solution = Solution()
    nums1 = 1

    m = [1,2,3,4]

    nums2 = [1,2,3]    
    n = 3

    result = solution.mySqrt(nums1)

    #print(solution.ls)

    print(nums1, result)