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
    def largestSumAfterKNegations(self, A, K):
        A.sort(reverse = True)

        ls = []
        for i in range(K):
            top =  A[-1]

            if top < 0:
                temp = -A.pop()
                ls.append(temp)
                continue
            elif top == 0:
                break
            else:
                K -= i
                if K % 2 == 0:
                    break
                else:
                    if not ls or  top <= ls[-1]:
                        A[-1] = -top
                    else:
                        ls[-1] = -ls[-1]

                break
        
        return sum(A) + sum(ls)

        

if __name__ == "__main__":
    solution = Solution()
    nums1 =  [2,-3,-1,5,-4]
    m = 2
    nums2 = TreeNode(4)  
    n = 3
    
   
    result = solution.largestSumAfterKNegations(nums1, m)

    #print(solution.ls)

    print(result)