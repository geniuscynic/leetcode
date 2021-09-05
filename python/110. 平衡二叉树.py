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
        self.isBalanced = True

    def helper(self, root: TreeNode):
        if self.isBalanced:
            return 0

        if not root:
            return 0

        left = self.helper(root.left) + 1
        right = self.helper(root.right) + 1

        if abs(left - right) > 1:
            self.isBalanced
            return 0

        return max(left, right)
        

    def isBalanced(self, root: TreeNode) -> bool:
        self.helper(root)

        return self.isBalanced


if __name__ == "__main__":
    solution = Solution()
    nums1 = [-10,-3,0,5,9]
    m = 3
    nums2 = [1,2,3]    
    n = 3
    
   

    result = solution.sortedArrayToBST(nums1)

    #print(solution.ls)

    print(nums1, result)