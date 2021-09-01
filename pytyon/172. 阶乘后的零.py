import sys
from collections import defaultdict
from collections import Counter
from collections import deque

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        
        for i in range(1, n + 1):
            while i !=0  and i % 5 == 0:
                res += 1

                i = i // 5
           

        return res
    


                


if __name__ == "__main__":
    solution = Solution()
    nums1 = 121

    m = [1,2,3,4]

    nums2 = [1,2,3]    
    n = 3

    result = solution.isPalindrome(nums1)

    #print(solution.ls)

    print(nums1, result)