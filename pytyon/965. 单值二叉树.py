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
        self.ans = True
        self.node = None

    def helper(self, root: TreeNode):
        if not root:
            return

        if root.left:
            self.helper(root.left)

        self.helper(root.right)

        return root.val

    def isUnivalTree(self, root: TreeNode) -> bool:

        if not root:
            return True

        deque = deque()
        deque.append(root)

        val = root.val
        while deque:
            node = deque.popleft()

            if val != node.val:
                return False

            if node.left:
                deque.append(node.left)

            if node.right:
                deque.append(node.right)

        return True


    
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
    nums1 = coverttoTree([1,2,3, 4])
    m = coverttoTree([10,5,15,3,7,None,18])
    nums2 = TreeNode(4)  
    n = 3
    
    result = solution.rangeSumBST(m, 7,15)

    #print(solution.ls)

    print(result)

    #"1(2(4)))(3)"
    #"1(2(4))(3)"
    #"1(2((4))(3))(3)