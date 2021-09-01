import sys
from collections import defaultdict
from collections import Counter

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.ls = []


    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        temp = ListNode(0)
        temp.next = head

        res = temp
        while temp and temp.next:
            if temp.next.val == val:
                temp.next = temp.next.next

            temp = temp.next

        return res.next

            

            

            
        

        






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

    result = solution.reversePrint(nums1)

    print(result)

    #printlistnode(result)