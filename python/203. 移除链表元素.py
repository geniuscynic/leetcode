import sys
from collections import defaultdict
from collections import Counter

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head

        while head and head.val == val:
            head = head.next

        temp = head

        while temp:
            if temp.next and temp.next.val == val:
                temp.next = temp.next.next
                continue

            temp = temp.next

        return head
            


if __name__ == "__main__":
    solution = Solution()
    nums1 = "()[]{}"

    m = [1,2,3,4]

    nums2 = [1,2,3]    
    n = 3

    result = solution.isValid(nums1)

    #print(solution.ls)

    print(nums1, result)