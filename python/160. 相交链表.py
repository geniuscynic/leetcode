import sys
from collections import defaultdict
from collections import Counter

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def helper(self, headA: ListNode, headB: ListNode):
        if not headA or not headB:
            return None

        if headA == headB:
            return headA

        temp = self.helper(headA, headB.next) 
        if not temp:
            temp = self.helper(headA.next, headB)

        return temp

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ls1 = []
        ls2 = []

        while headA:
            ls1.append(headA)
            headA = headA.next

        while headB:
            ls2.append(headB)
            headB = headB.next

        temp == None
        while ls1 and ls2:
            t1 = ls1.pop()
            t2 = ls2.pop()

            if t1 == t2:
                temp = t1
            else:
                return temp

        return temp


    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        l1, l2 = headA, headB

        while l1 != l2:
            if l1:
                l1 = l1.next
            else:
                l1 = headB

            
            if l2:
                l2 = l2.next
            else:
                l2 = headA


        return l1
            


if __name__ == "__main__":
    solution = Solution()
    nums1 = "()[]{}"

    m = [1,2,3,4]

    nums2 = [1,2,3]    
    n = 3

    result = solution.isValid(nums1)

    #print(solution.ls)

    print(nums1, result)