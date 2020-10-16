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
        self.ans = 0
        self.ls = []

    def helper(self, root: TreeNode):
        if not root:
            return 0

        left = self.helper(root.left)

        if root.left:
            print('left', root.left.val, left)

        if left == -1:
            return left

        right = self.helper(root.right)

        if root.right:
            print('right', root.right.val, right)  

        if right == -1:
            return right

        if abs(left - right) > 1:
            return -1

        #print(left, right)
        return max(left, right) + 1
        

    def isBalanced(self, root: TreeNode) -> bool:
        return self.helper(root) != -1


    
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
    nums1 = coverttoTree([1,2,3,4,None,None,5,6,None,None,7])
    m = coverttoTree([1,2,3,None,4,None,5])
    nums2 = TreeNode(4)  
    n = 3
    
    result = solution.isBalanced(nums1)

    #print(solution.ls)

    print(result)

    #"1(2(4)))(3)"
    #"1(2(4))(3)"
    #"1(2((4))(3))(3)