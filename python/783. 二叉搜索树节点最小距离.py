import sys
from collections import defaultdict
from collections import Counter
import re

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.ans = float('inf')
        self.prev = sys.maxsize

    def helper(self,root):
        if root == None:
            return

        self.helper(root.left)

        if self.prev == sys.maxsize:
            self.prev = root.val
        else:
            self.ans = min(root.val - self.prev, self.ans)
            self.prev = root.val

        self.helper(root.right)

    def minDiffInBST(self, root):
        self.helper(root)
    
        return self.ans
    

            
            
            
if __name__ == "__main__":
    solution = Solution()
    nums1 = "Let's take LeetCode contest"
    m = 2

    nums2 = [1,2,3]    
    n = 3

    result = solution.reverseWords(nums1)

    #print(solution.ls)

    print(nums1, result)