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
    def wordPattern(self, pattern: str, s: str) -> bool:
        p1 = {}
        
        counts = 1
        res1 = 0
        for s1 in pattern:
            if s1 not in p1:
                res1 = (res1 * 10) + counts
                p1[s1] = counts

                counts += 1
            else:
                res1 = (res1 * 10) + p1[s1]


        counts = 1
        p1.clear()

        res2 = 0
        for s1 in s.split(' '):
            if s1 not in p1:
                res2 = (res2 * 10) + counts
                p1[s1] = counts

                counts += 1
            else:
                res2 = (res2 * 10) + p1[s1]



        return res2 == res1

                



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
    nums1 = "abba"
    m = "dog cat cat dog"
    nums2 = TreeNode(4)  
    n = 3
    
   
    result = solution.wordPattern(nums1, m)

    #print(solution.ls)

    print(result)