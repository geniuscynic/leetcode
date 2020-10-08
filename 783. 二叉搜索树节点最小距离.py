import sys
from collections import defaultdict
from collections import Counter
import re
class Solution:
    def minDiffInBST(self, root):
        left = right = sys.maxsize

        if root == None:
            return sys.maxsize

        if root.left != None:
            left = root.val - root.left.val


        if root.right != None:
            right = root.right.val - root.val


        return min(left, right, self.minDiffInBST(root.left), self.minDiffInBST(root.right))
    

            
            
            
if __name__ == "__main__":
    solution = Solution()
    nums1 = "Let's take LeetCode contest"
    m = 2

    nums2 = [1,2,3]    
    n = 3

    result = solution.reverseWords(nums1)

    #print(solution.ls)

    print(nums1, result)