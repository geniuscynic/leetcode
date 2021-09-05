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
        self.ans = 0
        self.ls = []

    def helper(self, root: TreeNode):
        if not root:
            return

        self.append([root.val])

        self.helper(self.left)

        

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []


        deque1 = deque()
        deque1.append(root)

        deque2 = deque()

        ls = []

        while deque1:
            temp =[]
            while deque1:
                node = deque1.popleft()
                temp.append(node.val)
                deque2.append(node)

            #temp = []
            ls.append(temp)

            while deque2:
                node = deque2.popleft()
                if node.left:
                    deque1.append(node.left)

                if node.right:
                    deque1.append(node.right)

        return ls


    
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
    nums1 = coverttoTree([1,0,1,0,1,0,1])
    m = coverttoTree([1,2,3,None,4,None,5])
    nums2 = TreeNode(4)  
    n = 3
    
    result = solution.sumRootToLeaf(nums1)

    #print(solution.ls)

    print(result)

    #"1(2(4)))(3)"
    #"1(2(4))(3)"
    #"1(2((4))(3))(3)