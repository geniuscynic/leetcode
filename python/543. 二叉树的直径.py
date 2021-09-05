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
    def __init__(self):
        self.ans = 1

    def helper(self, root: TreeNode):
        if not root:
            return 0
        
        left = right = 0
        if root.left:
            left = self.helper(root.left) + 1

        if root.right:
            right = self.helper(root.right) + 1


        print(left, right)
        return max(left, right)

        

   

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        left = right = 0
        if root.left:
            left = self.helper(root.left) + 1
        
        if root.right:
            right = self.helper(root.right) + 1

        return max(left + right, self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))
        

    def helper_1(self, root: TreeNode):
        if not root:
            return 0
        
        left = right = 0
        
        left = self.helper(root.left)
        right = self.helper(root.right)

        self.ans = max(self.ans, left + right + 1)


        return max(left, right) + 1




def coverttoTree():
    ls =deque([1,2,3,4, 5])

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
    nums1 = coverttoTree()
    m = TreeNode(2)
    nums2 = TreeNode(4)  
    n = 3
    
   
    result = solution.diameterOfBinaryTree(nums1)

    #print(solution.ls)

    print(result)