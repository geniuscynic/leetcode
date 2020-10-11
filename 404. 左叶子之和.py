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
    def helper(self, root: TreeNode, parentNode):
        if not root:
            return 0

        if not root.left and not root.right and parentNode.left and parentNode.left == root:
            
            return root.val

        return self.helper(root.left, root) + self.helper(root.right, root)
        

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        return self.helper(root, root)

    def isleaf(self, root: TreeNode):
        if not root.left and not root.right:
            return True

        return False

    def sumOfLeftLeaves_1(self, root: TreeNode) -> int:
        if not root:
            return 0

        #if not root.left and not root.right:
            #return root.val

        res = 0

        if root.left:
            res += root.left.val if self.isleaf(root.left) else self.sumOfLeftLeaves_1(root.left)

        if root.right and not self.isleaf(root.right):
            res += self.sumOfLeftLeaves_1(root.right)

        return res




def coverttoTree():
    ls =deque([-6,8,-4,8,-5,-1,None,-9,9,8,8,None,None,-5,6,None,None,None,-4,None,4,None,None,8,8,None,None,None,5,None,None,None,None,None,-9])

    temp = TreeNode(ls.popleft())
    res = deque()
    res.append(temp)

    while ls:
        left = ls.popleft()
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
    nums1 = coverttoTree()
    m = TreeNode(2)
    nums2 = TreeNode(4)  
    n = 3
    
   
    result = solution.sumOfLeftLeaves_1(nums1)

    #print(solution.ls)

    print(result)