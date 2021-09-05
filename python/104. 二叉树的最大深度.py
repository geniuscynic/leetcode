# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, p: TreeNode, count: int):
        if p == None:
            return count
       
        count += 1
       
        return max(self.helper(p.left, count), self.helper(p.right, count))

    def maxDepth(self, root: TreeNode) -> int:
        return self.helper(root, 0)

        
        
        



if __name__ == "__main__":
    solution = Solution()
    nums1 = [4,5,6,0,0,0]
    m = 3
    nums2 = [1,2,3]    
    n = 3

    result = solution.merge(nums1,m,nums2,n)

    #print(solution.ls)

    print(nums1, result)