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

    def helper(self, root: Node):
        if not root:
            return 0

        res = [self.helper(node) for node in root.children]
        
        #for node in root.children:
            #res = max(self.helper(node), res)
            
        return max(res) + 1
        
    def maxDepth(self, root: 'Node') -> int:
        return self.helper(help)




def coverttoTree():
    ls =deque([1,2,3,4, 5])

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
    
   
    result = solution.diameterOfBinaryTree(nums1)

    #print(solution.ls)

    print(result)