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
    def maxhelper2(self, root: TreeNode):
        if not root:
            return 0

        if root.right:
            return self.maxhelper2(root.right)

        return root.val


    def minhelper2(self, root: TreeNode):
        if not root:
            return 0

        if root.left:
            return self.minhelper2(root.left)

        return root.val

    def helper(self, root: TreeNode):
        if not root:
            return sys.maxsize

        
            
        current = root.val

        left = right = sys.maxsize

        if root.left:
            left = min(current - root.left.val, self.helper(root.left), current - self.maxhelper2(root.left))
            
        if root.right:
            right = min(root.right.val - current, self.helper(root.right), self.minhelper2(root.right) - current)

           
        
        return min(left, right)

    def __init__(self):
        self.res = float('inf')
        self.pre = float('-inf')

    def helper_1(self, root: TreeNode):
        if not root:
            return None

       
        self.helper_1(root.left)

        print(root.val, self.pre)
        
        current = root.val
        self.res = min(self.res, current - self.pre)
        self.pre = current

        self.helper_1(root.right)

        


        

    def getMinimumDifference(self, root: TreeNode) -> int:
        self.helper_1(root)
        




def coverttoTree():
    ls =deque([0,2,3,2236,1277,2776,519])

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
    
   
    result = solution.getMinimumDifference(nums1)

    #print(solution.ls)

    print(result)