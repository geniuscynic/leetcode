# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, p: TreeNode, q: TreeNode):
       
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        elif p.val != q.val:
            return False

       
        return self.helper(p.left, q.right) and self.helper(p.right, q.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        return self.helper(root.left, root.right)
        
        



if __name__ == "__main__":
    solution = Solution()
    nums1 = [4,5,6,0,0,0]
    m = 3
    nums2 = [1,2,3]    
    n = 3

    result = solution.merge(nums1,m,nums2,n)

    #print(solution.ls)

    print(nums1, result)