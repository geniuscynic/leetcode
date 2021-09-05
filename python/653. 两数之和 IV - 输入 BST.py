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
        self.ans = 1

    def helper(self,  root: TreeNode, ls):
        if not root:
            return

        self.helper(root.left, ls)

        ls.append(root.val)

        self.helper(root.right, ls)



    def findTarget(self, root: TreeNode, k: int) -> bool:
        ls = []

        self.helper(root, ls)

        while ls:
            res = k - ls.pop()

            if res in ls:
                return True
    
        return False

    def helper(self,  root: TreeNode, k, ls):
        if not root:
            return False

        if k - root.val in ls:
            return True

        ls.add(root.val)
        return self.helper(root.left, k, ls) or self.helper(root.right,k,  ls)



    def findTarget(self, root: TreeNode, k: int) -> bool:
        ls = set()

        return self.helper(root, k, ls)
        
    
        
            

        
            
        

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
    m = coverttoTree([1,None,1,None,1,None,1,None,1,None,1,2])
    nums2 = TreeNode(4)  
    n = 3
    
   
    result = solution.tree2str(nums1)

    #print(solution.ls)

    print(result)

    #"1(2(4)))(3)"
    #"1(2(4))(3)"
    #"1(2((4))(3))(3)