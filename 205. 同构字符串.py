import sys
from collections import defaultdict
from collections import Counter

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        lens = len(s)

        dicts1 = {}
        dicts2 = {}

        for i in range(lens):
            if s[i] in dicts and dicts[s[i]] != t[i]:
                return False

            if t[i] in dicts and dicts[t[i]] != s[i]:
                return False

            dicts[s[i]] = t[i]
            dicts[t[i]] = s[i]

        return True
        


if __name__ == "__main__":
    solution = Solution()
    nums1 = 49979

    m = [1,2,3,1]

    nums2 = [1,2,3]    
    n = 3

    result = solution.countPrimes(nums1)

    #print(solution.ls)

    print(result)