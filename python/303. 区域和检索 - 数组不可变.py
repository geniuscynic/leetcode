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

class NumArray:

    def __init__(self, nums: List[int]):
        self.ns = nums


    def sumRange(self, i: int, j: int) -> int:
        return sum(self.ns[i:j+1])

                



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