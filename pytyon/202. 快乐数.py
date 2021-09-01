import sys
from collections import defaultdict
from collections import Counter

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def heler(self, n):
        res = 0
        while n != 0:
            res += (n % 10) ** 2

            n = n // 10

        return res 
    def isHappy(self, n: int) -> bool:
        happy = set()
        while n != 1 or :
            n = self.heler(n)

            if n in happy:
                return False

            happy.add(n)


        return n == 1


if __name__ == "__main__":
    solution = Solution()
    nums1 = [2]

    m = [1,2,3,1]

    nums2 = [1,2,3]    
    n = 3

    result = solution.rob1(nums1)

    #print(solution.ls)

    print(result)