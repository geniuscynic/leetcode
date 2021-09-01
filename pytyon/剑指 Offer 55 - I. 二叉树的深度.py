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
        self.k = 0

    def helper(self, root: TreeNode, deth):
        if not root:
            return deth

        deth += 1

        left = self.helper(root.left, deth)
        right = self.helper(root.right, deth)

        self.ans = max(self.ans, left, right)

        return deth


    def helper(self, root: TreeNode):
        if not root:
            return 0

        
        left = self.helper(root.left)
        right = self.helper(root.right)

        return max(left, right) + 1

        
    def maxDepth(self, root: TreeNode) -> int:
        self.helper(root, 0)

        return self.ans




    
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
    nums1 = coverttoTree([1,0,1,0,1,0,1])
    m = coverttoTree([1,2,3,None,4,None,5])
    nums2 = TreeNode(4)  
    n = 3
    
    result = solution.sumRootToLeaf(nums1)

    #print(solution.ls)

    print(result)

    #"1(2(4)))(3)"
    #"1(2(4))(3)"
    #"1(2((4))(3))(3)