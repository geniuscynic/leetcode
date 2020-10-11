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
    def helper(self, nums):
        if len(nums) == 0:
            return None

        lens = len(nums) // 2

        #print(lens, nums)
        treeNode = TreeNode(nums[lens])
        if(lens == 0):
            return treeNode

        #print("left",nums[:lens])
        treeNode.left = self.helper(nums[:lens])

        #print("right",nums[lens+1:])
        treeNode.right = self.helper(nums[lens+1:])

        return treeNode



    def sortedArrayToBST(self, nums):
        return self.helper(nums)


if __name__ == "__main__":
    solution = Solution()
    nums1 = [-10,-3,0,5,9]
    m = 3
    nums2 = [1,2,3]    
    n = 3
    
   

    result = solution.sortedArrayToBST(nums1)

    #print(solution.ls)

    print(nums1, result)