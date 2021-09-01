import sys
from collections import defaultdict
from collections import Counter

select p.FirstName, p.LastName, ad.City, ad.State from Person p
left join Address ad
on p.PersonId = ad.PersonId    

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0

        for i in nums:
            res = res ^ i

        return res
                


if __name__ == "__main__":
    solution = Solution()
    nums1 = "()[]{}"

    m = [1,2,3,4]

    nums2 = [1,2,3]    
    n = 3

    result = solution.isValid(nums1)

    #print(solution.ls)

    print(nums1, result)