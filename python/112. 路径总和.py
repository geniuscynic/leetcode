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
        if not root:
            return False

        res = sum - root.val

        if not root.left and not root.right:
            if res == 0:
                return True
            else:
                return False


        left = self.helper(root.left, res)
        if left:
            return True

        return self.helper(root.right, res)


    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        return self.helper(root, sum)

        


if __name__ == "__main__":
    solution = Solution()
    nums1 = [-10,-3,0,5,9]
    m = 3
    nums2 = [1,2,3]    
    n = 3
    
   

    result = solution.sortedArrayToBST(nums1)

    #print(solution.ls)

    print(nums1, result)