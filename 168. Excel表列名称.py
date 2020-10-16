import sys
from collections import defaultdict
from collections import Counter
from collections import deque

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ""
        while(n != 0):
            n -= 1
            temp = n % 26
           
            res += chr(temp + 65)

            n = n // 26


        return res[::-1]
    


                


if __name__ == "__main__":
    solution = Solution()
    nums1 = 121

    m = [1,2,3,4]

    nums2 = [1,2,3]    
    n = 3

    result = solution.isPalindrome(nums1)

    #print(solution.ls)

    print(nums1, result)