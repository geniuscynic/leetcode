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

    def helper(self, root: TreeNode, val: int):
        if not root:
            return None

        if root.val == val:
            return root

        if root.val > val:
            return self.helper(root.left, val)

        return self.helper(root.right, val)

        
        
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        return self.helper(root,val)

       

 
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