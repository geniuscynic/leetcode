import sys
from collections import defaultdict
from collections import Counter

delete p1 from  Person p1, Person p2
where p1.Email = p2.Email
and p1.id > p2.id
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        while n != 0:
            #print(n & 1)
            if n & 1 == 1:
                res += 1
            n = n >> 1

            #print(res, n)
        return res
                


if __name__ == "__main__":
    solution = Solution()
    nums1 = 3

    m = [1,2,3,4]

    nums2 = [1,2,3]    
    n = 3

    result = solution.hammingWeight(nums1)

    #print(solution.ls)

    print(nums1, result)