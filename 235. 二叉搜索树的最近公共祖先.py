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

class Solution:
    
    def helper(self, root: TreeNode, p: TreeNode, q: TreeNode, p1, p2):
        
        if not root:
            return None

        if root == p or root = q:
            return root

       

        res = self.helper(root.left, p, q, p1, p2)

        if res == p:
            p1.append(res)
        elif p:
            p1.append(root)

        self.helper(root.right, p, q, p1, p2)
        
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p1 = deque()
        p2 = deque()
        
    
def coverttoTree():
    ls =deque([6,2,8,0,4,7,9,null,null,3,5])

    temp = TreeNode(ls.popleft())
    res = deque([temp])

    while ls:
        left = ls.popleft()
        right = ls.popleft()

        node = res.popleft()
        if left:
            node.left = TreeNode(left)

        if right:
            node.right = TreeNode(right)

        res.append([node.left, node.right])


if __name__ == "__main__":
    solution = Solution()
    nums1 = coverttoTree()
    nums1.left 
    m = 3
    nums2 = [1,2,3]    
    n = 3
    
   

    #result = solution.sortedArrayToBST(nums1)

    #print(solution.ls)

    #print(nums1, result)