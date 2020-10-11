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
    def helper(self, root: TreeNode, path, paths):
        if root:
                path += str(root.val)
                if not root.left and not root.right:  # 当前节点是叶子节点
                    paths.append(path)  # 把路径加入到答案中
                else:
                    path += '->'  # 当前节点不是叶子节点，继续递归遍历
                    self.helper(root.left, path, paths)
                    self.helper(root.right, path, paths)


        
    def binaryTreePaths(self, root: TreeNode):
        path = []
        print(self.helper(root, '', path))
        print(path)
        # ls = [root]

        # res = []
        # temp = []
        # while ls:
        #     node = ls.pop()
        #     temp.append(node.val)

            
        #     if node.right:
        #         ls.append(node.right)

        #     if node.left:
        #         ls.append(node.left)

        #     if not node.left and not node.right:
        #         res.append(temp)


        #         t2 = temp[:]

        #         print(node.val, t2)
        #         while t2 and t2.pop() != node.val:
        #             pass

        #         temp = t2


        #return res



        
    
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
    
   
    result = solution.binaryTreePaths(nums1)

    #print(solution.ls)

    print(result)