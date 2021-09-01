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
    
    def helper(self, root, p, q, p1, p2):
        
        if not root:
            return

        if p1 and p2 and p1[-1] == p2[-1]:
            return


        print(root.val)
        if root.val == p.val:
            p1.append(root.val)
            if p2:
                return
            
            
        if root.val == q.val:
            p2.append(root.val)
            if p1:
                return
            
            
        self.helper(root.left, p, q, p1, p2)
        self.helper(root.right, p, q, p1, p2)

        if p1:
            if root.left and root.left.val == p1[-1]:
                p1.append(root.val)

            if root.right and root.right.val == p1[-1]:
                p1.append(root.val)


        if p2:
            if root.left and root.left.val == p2[-1]:
                p2.append(root.val)

            if root.right and root.right.val == p2[-1]:
                p2.append(root.val)

        
        # if res.val == p.val:
        #     p1.append(res)
        # elif p:
        #     p1.append(root)

        #self.helper(root.right, p, q, p1, p2)
        
    def lowestCommonAncestor(self, root, p, q):
        p1 = []
        p2 = []

        self.helper(root, p, q,p1, p2)

        print(p1, p2)

        el = p1.pop()
        temp = el
        while p2:
            t2 = p2.pop()
            if el == t2:
                temp = el

                if p1:
                    el = p1.pop()
                else:
                    break
                

        print(p1, p2, temp)

    def lowestCommonAncestor_1(self, root, p, q):
        if root.val == p.val or root.val==q.val:
            return root
            
        if root.val > p.val and root.val < q.val:
            return root
        
        if root.val < p.val and root.val > q.val:
            return root

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor_1(root.left, p, q)

        return self.lowestCommonAncestor_1(root.right, p, q)

        
    
def coverttoTree():
    ls =deque([6,2,8,0,4,7,9,None,None,3,5])

    temp = TreeNode(ls.popleft())
    res = deque()
    res.append(temp)

    while ls:
        left = ls.popleft()
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
    
   

    result = solution.lowestCommonAncestor_1(nums1, m, nums2).val

    #print(solution.ls)

    print(result)