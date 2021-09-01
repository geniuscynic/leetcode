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
        self.pt = ''
        self.qt = ''

       

    def helper(self, root: TreeNode, p, q, p_path, q_path):
        if not root:
            return

        #print(self.pt, self.qt, p_path, q_path)

        if self.pt != '' and self.qt != '':
            return

        if self.pt == '':
            p_path += str(root.val) + "#"

        if self.qt == '':
            q_path += str(root.val) + "#"

        if root.val == p:
            self.pt = p_path

        if root.val == q:
            self.qt = q_path

        self.helper(root.left, p, q, p_path, q_path)
        self.helper(root.right, p, q, p_path, q_path)

        
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.helper(root, p, q, "", "")
        #print(self.pt, self.qt)
        
        i = 0
        temp = ""

        ls1=self.pt.split("#")
        ls2=self.qt.split("#")

        while True:
            if i >= len(ls1) or i>=len(ls2):
                break

            if ls1[i] == ls2[i]:
                temp = ls1[i]
            else:
                break

            i += 1

        #print(self.pt, self.qt, temp)
        return TreeNode(int(temp))



    def helper_1(self, root: TreeNode, p, q):
            if not root:
                return None

            #print()
            if root.val == p.val or root.val == q.val:
                return root


            left = self.helper_1(root.left, p, q)
            right = self.helper_1(root.right, p, q)

            
            if not left:
                return right

            if not right:
                return left

            return root
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        return self.helper_1(root, p, q)
        #print(self.pt, self.qt)
        
        # i = 0
        # temp = ""

        # ls1=self.pt.split("#")
        # ls2=self.qt.split("#")

        # while True:
        #     if i >= len(ls1) or i>=len(ls2):
        #         break

        #     if ls1[i] == ls2[i]:
        #         temp = ls1[i]
        #     else:
        #         break

        #     i += 1

        # #print(self.pt, self.qt, temp)
        # return TreeNode(int(temp))


    
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
    nums1 = coverttoTree([3,5,1,6,2,0,8,None,None,7,4])
    m = coverttoTree([1,2,3,None,4,None,5])
    nums2 = TreeNode(4)  
    n = 3
    
    result = solution.lowestCommonAncestor(nums1, TreeNode(5), TreeNode(4))

    #print(solution.ls)

    print(result.val)

    #"1(2(4)))(3)"
    #"1(2(4))(3)"
    #"1(2((4))(3))(3)