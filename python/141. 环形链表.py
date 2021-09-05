import sys
from collections import defaultdict
from collections import Counter

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        dicts = {}
        while head:
            if head not in dicts:
                dicts[head] = head
                head = head.next
            else:
                return False

        return True


    def hasCycle_1(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        fast = head.next
        slow = head
        while slow and fast:
            if fast == slow:
                return True

            slow = slow.next

            if fast.next:
                fast = fast.next.next
            else:
                return False


        return False
            


if __name__ == "__main__":
    solution = Solution()
    nums1 = "()[]{}"

    m = [1,2,3,4]

    nums2 = [1,2,3]    
    n = 3

    result = solution.isValid(nums1)

    #print(solution.ls)

    print(nums1, result)