import sys
from collections import defaultdict
from collections import Counter
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def __init__(self):
        self.ans = 1

    def issame(self, s: TreeNode, t: TreeNode):
        if not s and not t:
            print(1)
            return True

        if not s or not t:
            print(2)
            return False

        if s.val != t.val:
            print(3)
            return False

        return self.issame(s.left, t.left) and self.issame(s.right, t.right)

    def helper(self, s: TreeNode, t: TreeNode):
        if not s:
            return False
            
        res = self.issame(s, t)

        if res:
           return True

        return self.helper(s.left, t) or self.helper(s.right, t)
        
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        return self.helper(s, t)


def coverttoTree(t):
    ls =deque(t)

    temp = TreeNode(ls.popleft())
    res = deque()
    res.append(temp)

    while ls:
        left = ls.popleft()
        if ls:
            right = ls.popleft()

        node = res.popleft()
        #print(node.val, left, right)
        if left != None:
            node.left = TreeNode(left)
            res.append(node.left)

        if right != None:
            node.right = TreeNode(right)
            res.append(node.right)


    return temp
        

if __name__ == "__main__":
    solution = Solution()
    nums1 = coverttoTree([1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,2])
    m = coverttoTree([1,None,1,None,1,None,1,None,1,None,1,2])
    nums2 = TreeNode(4)  
    n = 3
    
   
    result = solution.isSubtree(nums1, m)

    #print(solution.ls)

    print(result)