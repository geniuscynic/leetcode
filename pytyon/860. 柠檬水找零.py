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
    def lemonadeChange(self, bills: List[int]) -> bool:
        list5 = []
        list10 = []
        list20 = []

        for bill in bills:
            if bill == 5:
                list5.append(5)
                continue

            if bill == 10:
                if list5 and list5.pop() == 5:
                    list10.append(10)
                    continue
                else:
                    return False

            if bill == 20:
                temp = 20

                if list10 and list5:
                    list10.pop()
                    list5.pop()
                    list20.append(20)
                    continue
                elif len(list5) >= 3:
                    list5.pop()
                    list5.pop()
                    list5.pop()
                    list20.append(20)
                    continue
                else:
                    return False

        return True

        

if __name__ == "__main__":
    solution = Solution()
    nums1 = coverttoTree()
    m = TreeNode(2)
    nums2 = TreeNode(4)  
    n = 3
    
   
    result = solution.binaryTreePaths(nums1)

    #print(solution.ls)

    print(result)