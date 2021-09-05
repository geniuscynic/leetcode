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
    def lastStoneWeight(self, stones):
        maxl = max(stones) + 1
        ls = [0 for _ in range(maxl)]

        for i in stones:
            ls[i] += 1

        #print(ls)
        temp = 0
        for i in  reversed(range(1, maxl)):
            if ls[i] == 0:
                continue

            
            #print("1", ls, temp)

            while temp >= i and ls[i] > 0:
                temp = temp - i
                ls[i] -= 1


            #print("2", ls, temp)

            if temp >= i and ls[i] == 0:
                continue

            if temp < i:
                ls[temp] += 1
                temp = 0

            if ls[i] % 2 == 0:
                ls[i] = 0
                continue
            else:
                temp = i
                ls[i] = 0

        #print(ls)
        for i in range(1, maxl):
            if ls[i] > 0:
                return i

        return temp

                


            


        

if __name__ == "__main__":
    solution = Solution()
    nums1 = [2,7,4,1,8,1]
    m = 2
    nums2 = TreeNode(4)  
    n = 3
    
   
    result = solution.lastStoneWeight(nums1)

    #print(solution.ls)

    print(result)