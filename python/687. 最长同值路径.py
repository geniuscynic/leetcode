import sys

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def helper(self, root):
        if root == None:
            return 0

        leftPath = rightPath = 0
        if root.left != None and root.val == root.left.val:
            leftPath = 1 + self.helper(root.left)

        if root.right != None and root.val == root.right.val:
            rightPath = 1 + self.helper(root.right)

        return max(leftPath, rightPath)

        

    def longestUnivaluePath(self, root):
        if root == None:
            return 0

        root_path = 0
        if root.left != None and root.left.val == root.val:
            root_path = 1 + root_path + self.helper(root.left)

        if root.right != None and root.right.val == root.val:
            root_path = 1 + root_path + self.helper(root.right)

        return max(self.longestUnivaluePath(root.left), root_path, self.longestUnivaluePath(root.right))
             


        
        

            
            

        



                          

if __name__ == "__main__":
    solution = Solution()
    nums1 = [1,12,-5,-6,50,3]
    m = 4
    nums2 = [1,2,3]    
    n = 3

    result = solution.findMaxAverage_1(nums1, m)

    #print(solution.ls)

    print(nums1, result)