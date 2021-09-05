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

    def helper(self, root: TreeNode, t2: TreeNode):
        if not root  and not t2:
            return

        root.val += t2.val

        if root.left and t2.left:
            self.helper(root.left, t2.left)
        elif not root.left and  t2.left:
            root.left = t2.left


        if root.right and t2.right:
            self.helper(root.right, t2.right)
        elif not root.right and  t2.right:
            root.right = t2.right

    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        self.helper(t1, t2)

        return t1
        

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
    m = coverttoTree([1,None,1,None,1,None,1,None,1,None,1,2])
    nums2 = TreeNode(4)  
    n = 3
    
   
    result = solution.tree2str(nums1)

    #print(solution.ls)

    print(result)

    #"1(2(4)))(3)"
    #"1(2(4))(3)"
    #"1(2((4))(3))(3)