import sys
from collections import defaultdict
from collections import Counter

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse(self, x: int) -> int:
       res = 0

        mins = -2147483648
        maxs = 2147483647
        while(x != 0):
            temp = x % 10 if x > 0 else x % -10

            #print(temp)
            if res  > maxs // 10 or (res == maxs // 10 and  temp > 7):
                return 0

            if res < int(mins / 10) or (res == mins and temp < -8):
                return 0 

            res = res * 10 + temp

            x = x // 10 if x > 0 else int(x / 10)

        return res


                


if __name__ == "__main__":
    solution = Solution()
    nums1 = -123

    m = [1,2,3,4]

    nums2 = [1,2,3]    
    n = 3

    result = solution.reverse(nums1)

    #print(solution.ls)

    print(nums1, result)