import sys
from collections import defaultdict
from collections import Counter

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.ls = ListNode(0)

    def heler(self, head: ListNode):
        if not head:
            return
        
        self.heler(head.next)

        #printlistnode(ls)

        self.ls.next = head
        self.ls = self.ls.next


        #printlistnode(ls)
        
    def reverseList(self, head: ListNode) -> ListNode:
        temp = self.ls

        self.heler(head)
        self.ls.next = None
        #self.ls = None

        return temp.next


    def reverseList_1(self, head: ListNode) -> ListNode:
        
        prev, curr = None, head
       
        while curr:

            temp = curr.next
            
            curr.next = prev
            
            prev = curr

            curr = temp


        return prev



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
    nums1 = covertlistnode([1,2,3,4,5])

    m = [1,2,3,4]

    nums2 = [1,2,3]    
    n = 3

    result = solution.reverseList_1(nums1)

    #print(solution.ls)

    printlistnode(result)