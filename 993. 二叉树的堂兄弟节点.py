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
        self.ans = True
        self.l1 = None
        self.l2 = None

        self.left = None
        self.right = None

    def helper(self, root: TreeNode, x: int, y: int, level):
        if not root:
            return

        level +=1
        if root.left and (root.left.val == x):
            self.left = root.val
            self.l1= level
        elif root.left and (root.left.val == y):
            self.right = root.val
            self.l2 = level
        
        if root.right and (root.right.val == x):
            self.left = root.val
            self.l1 =level
        elif root.right and (root.right.val == y):
            self.right = root.val
            self.l2 = level

        if self.left != None and self.right != None:
            return 


        self.helper(root.left, x, y, level)
        self.helper(root.right, x, y, level)



    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.helper(root, x, y, 0)

        print(self.l1,self.l2 ,self.left,self.right)
        if self.l1 == self.l2 and self.left !=self.right:
            return True

        return False


    
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
    m = coverttoTree([1,2,3,None,4,None,5])
    nums2 = TreeNode(4)  
    n = 3
    
    result = solution.isCousins(m, 5,4)

    #print(solution.ls)

    print(result)

    #"1(2(4)))(3)"
    #"1(2(4))(3)"
    #"1(2((4))(3))(3)