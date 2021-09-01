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
    def helper(self, root: TreeNode, dicts):
        if not root:
            return

        
        if root.val in dicts:
            dicts[root.val] += 1
        else:
            dicts[root.val] = 1

        self.helper(root.left, dicts)
        self.helper(root.right, dicts)

        

    def findMode(self, root: TreeNode):
        ls = [root]

        res = []
        current = 0
        currentCunt = 0
        maxsCount = 0
        while ls:
            node = ls.pop()
            if node == None:
                continue
            
            if maxsCount == 0:
                current = node.val
                maxsCount = 1

            
            if current == node.val:
                currentCunt += 1
            
            print(current, node.val, res, currentCunt)
            if current != node.val:
                if maxsCount < currentCunt:
                    res.clear()
                    res.append(current)
                    maxsCount = currentCunt

                elif maxsCount == currentCunt:
                    res.append(current)

                currentCunt = 1

            if not ls and current != node.val:
                if maxsCount < currentCunt:
                    res.clear()
                    res.append(current)
                    maxsCount = currentCunt

                elif maxsCount == currentCunt:
                    res.append(node.val)

                currentCunt = 1

            if not ls and current == node.val:
                if maxsCount < currentCunt:
                    res.clear()
                    res.append(current)
                    maxsCount = currentCunt

                elif maxsCount == currentCunt:
                    res.append(node.val)

                currentCunt = 1

            

            

                
            current = node.val

            
            if node.right:
                #print("right", node.right.val)
                ls.append(node.right)
            else:
                ls.append(None)

            if node.left:
                #print("left", node.left.val)
                ls.append(node.left)
            else:
                ls.append(None)



    

        return res
        




def coverttoTree():
    ls =deque([1,None, 2])

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
    
   
    result = solution.findMode(nums1)

    #print(solution.ls)

    print(result)