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
   
    def helper(self, root: TreeNode, sum: int):
        

    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        ls = deque([root])

        res = TreeNode(root.val)

        ls2 = deque([res])
        while ls:
            node = ls.popleft()
            node2 = ls2.popleft()

            if node.right:
                node2.left = TreeNode(node.right.val)
                ls.append(node.right)
                ls2.append(node2.left)

            if node.left:
                node2.right = TreeNode(node.left.val)
                ls.append(node.left)
                ls2.append(node2.right)

        return res

    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
            
        ls = deque([root])

        #res = TreeNode(root.val)

        #ls2 = deque([res])
        while ls:
            node = ls.popleft()
            
            node.left, node.right = node.right, node.left
            if node.right:
                ls.append(node.right)
               

            if node.left:
                ls.append(node.left)
                
        return root





        


if __name__ == "__main__":
    solution = Solution()
    nums1 = [-10,-3,0,5,9]
    m = 3
    nums2 = [1,2,3]    
    n = 3
    
   

    result = solution.sortedArrayToBST(nums1)

    #print(solution.ls)

    print(nums1, result)