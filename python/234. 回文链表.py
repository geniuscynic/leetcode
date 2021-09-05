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

    
        
    def isPalindrome(self, head: ListNode) -> bool:

        prev, cur = None, head

        fast = head

        while cur:
            if not fast:
               
                break

            if not fast.next:
                cur = cur.next
                break

            #if not fast.next.next:
                #break

            fast = fast.next.next

            temp = cur.next

            cur.next = prev

            prev = cur

            cur = temp

            
        while prev and cur:
            if prev.val != cur.val:
                return False

            prev = prev.next
            cur = cur.next

        if prev != cur:
            return False

        return True

        #printlistnode(prev)
        #printlistnode(cur)



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
    nums1 = covertlistnode([1,2,3,3,2, 1,2])

    m = [1,2,3,4]

    nums2 = [1,2,3]    
    n = 3

    result = solution.isPalindrome(nums1)

    print(result)

    #printlistnode(result)