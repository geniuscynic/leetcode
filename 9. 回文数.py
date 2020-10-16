import sys
from collections import defaultdict
from collections import Counter

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        y = x
        res = 0
        while(x != 0):
            temp = x % 10

            res = res * 10 + temp

            x = x // 10

        return True if y == res else False
    


                


if __name__ == "__main__":
    solution = Solution()
    nums1 = 121

    m = [1,2,3,4]

    nums2 = [1,2,3]    
    n = 3

    result = solution.isPalindrome(nums1)

    #print(solution.ls)

    print(nums1, result)