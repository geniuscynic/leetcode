import sys
from collections import defaultdict
from collections import Counter

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l2:
            return l1
        
        if not l1:
            return l2
            
        res = ListNode()
        if l1.val <= l2.val:
                res.val = l1.val
                l1 = l1.next
        else:
            res.val = l2.val
            l2 = l2.next

        node = [res]

        while l1 and l2:
            temp = node.pop()
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next

            node.append(temp.next)

        temp = node.pop()
        if l1:
            temp.next = l1
        elif l2:
            temp.next = l2
            
        return res

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l2:
            return l1
        
        if not l1:
            return l2
            
        res = ListNode()
        prev = res

        while l1 and l2:
            
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next

           prev = prev.next

        
        if l1:
            prev.next = l1
        elif l2:
            prev.next = l2
            
        return res.next


                


if __name__ == "__main__":
    solution = Solution()
    nums1 = "()[]{}"

    m = [1,2,3,4]

    nums2 = [1,2,3]    
    n = 3

    result = solution.isValid(nums1)

    #print(solution.ls)

    print(nums1, result)