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

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def __init__(self):
        self.ans = -1

    def helper(self, root: TreeNode, ls):
        if not root:
            return None

        if not root.left and not root.right:
            ls.append(root.val)

        self.helper(root.left, ls)
        self.helper(root.right, ls)
        
        
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        ls1 = []
        ls2 = []

        self.helper(root1, ls1)
        self.helper(root2, ls2)

        if len(ls1) != len(ls2):
            return False

        while ls1:
            if ls1.pop() !=ls2.pop():
                return

        return True

     def helper_1(self, root: TreeNode):
        if not root:
            return None

        if not root.left and not root.right:
            yield root.val

        yield self.helper(root.left, ls)
        yield self.helper(root.right, ls)

       

 
def coverttoTree(t):
    ls =deque(t)

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
    nums1 = coverttoTree([1,2,3, 4])
    m = coverttoTree([1,1,3,1,1,3,4,3,1,1,1,3,8,4,8,3,3,1,6,2,1])
    nums2 = TreeNode(4)  
    n = 3
    
    result = solution.findSecondMinimumValue(m)

    #print(solution.ls)

    print(result)

    #"1(2(4)))(3)"
    #"1(2(4))(3)"
    #"1(2((4))(3))(3)