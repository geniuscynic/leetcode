import sys
from collections import defaultdict
from collections import Counter

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.k = 0
        self.node = None

    def helper(self, head: ListNode):
        if not head:
            return
            
        #print(self.k, head.val)

        

        self.helper(head.next)

        self.k -= 1

        if self.k == 0:
            if not self.node:
                self.node = head

            return

    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        self.k = k

        self.helper(head)

        return self.node



def covertlistnode(ls):
    res = ListNode(0)

    temp = res
    for l in ls:
        temp.next = ListNode(l)
        temp = temp.next

    return res.next

def printlistnode(ls):
    while(ls):
        print(ls.val)

        ls = ls.next

    print("######")

if __name__ == "__main__":
    solution = Solution()
    nums1 = covertlistnode([1,2,3,4,5,6])

    m = [1,2,3,4]

    nums2 = [1,2,3]    
    n = 3

    result = solution.getKthFromEnd(nums1, 2)

    print(result.val)

    #printlistnode(result)