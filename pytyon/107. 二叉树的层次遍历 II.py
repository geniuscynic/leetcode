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
    def helper(self, p: TreeNode, count: int):
        if p == None:
            return count
       
        count += 1
       
        return max(self.helper(p.left, count), self.helper(p.right, count))

    def levelOrderBottom(self, root):
        p1 = deque()
        p1.append([root])

        ls = []
        #p.append([root.val])
        
        while(p1):
            node = p1.popleft()

            temp = []
            res = []
            for n in node:
                if n.left:
                    temp.append(n.left)

                if n.right:
                    temp.append(n.right)

                res.append(n.val)

            if temp:
                p1.append(temp)
                
            ls.append(res)

            #p2.append([root.val])

        ls.reverse()

        return ls


if __name__ == "__main__":
    solution = Solution()
    nums1 = [4,5,6,0,0,0]
    m = 3
    nums2 = [1,2,3]    
    n = 3
    
    p1 = deque()
    p1.append([])
    p1.append(['aa','bb'])
    while []:
        print("aaa")
        p1.popleft()


    #result = solution.merge(nums1,m,nums2,n)

    #print(solution.ls)

    #print(nums1, result)