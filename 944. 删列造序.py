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

    def minDeletionSize(self, A) -> int:
        len1, len2 = len(A), len(A[0])

        res = 0
        
        for i in range(len2):
            for a in range(1, len1):
                if A[a - 1][i] > A[a][i]:
                    res += 1
                    break
        return res


    def minDeletionSize_1(self, A):
        ans = 0
        for col in zip(*A):
            print(col)
            if any(col[i] > col[i+1] for i in range(len(col) - 1)):
                ans += 1
        return ans


        

if __name__ == "__main__":
    solution = Solution()
    nums1 = ["cba", "daf", "ghi"]
    m = [[-57,-58],[-72,91],[-55,35],[-20,29],[51,70],[-61,88],[-62,99],[52,17],[-75,-32],[91,-22],[54,33],[-45,-59],[47,-48],[53,-98],[-91,83],[81,12],[-34,-90],[-79,-82],[-15,-86],[-24,66],[-35,35],[3,31],[87,93],[2,-19],[87,-93],[24,-10],[84,-53],[86,87],[-88,-18],[-51,89],[96,66],[-77,-94],[-39,-1],[89,51],[-23,-72],[27,24],[53,-80],[52,-33],[32,4],[78,-55],[-25,18],[-23,47],[79,-5],[-23,-22],[14,-25],[-11,69],[63,36],[35,-99],[-24,82],[-29,-98],[-50,-70],[72,95],[80,80],[-68,-40],[65,70],[-92,78],[-45,-63],[1,34],[81,50],[14,91],[-77,-54],[13,-88],[24,37],[-12,59],[-48,-62],[57,-22],[-8,85],[48,71],[12,1],[-20,36],[-32,-14],[39,46],[-41,75],[13,-23],[98,10],[-88,64],[50,37],[-95,-32],[46,-91],[10,79],[-11,43],[-94,98],[79,42],[51,71],[4,-30],[2,74],[4,10],[61,98],[57,98],[46,43],[-16,72],[53,-69],[54,-96],[22,0],[-7,92],[-69,80],[68,-73],[-24,-92],[-21,82],[32,-1],[-6,16],[15,-29],[70,-66],[-85,80],[50,-3],[6,13],[-30,-98],[-30,59],[-67,40],[17,72],[79,82],[89,-100],[2,79],[-95,-46],[17,68],[-46,81],[-5,-57],[7,58],[-42,68],[19,-95],[-17,-76],[81,-86],[79,78],[-82,-67],[6,0],[35,-16],[98,83],[-81,100],[-11,46],[-21,-38],[-30,-41],[86,18],[-68,6],[80,75],[-96,-44],[-19,66],[21,84],[-56,-64],[39,-15],[0,45],[-81,-54],[-66,-93],[-4,2],[-42,-67],[-15,-33],[1,-32],[-74,-24],[7,18],[-62,84],[19,61],[39,79],[60,-98],[-76,45],[58,-98],[33,26],[-74,-95],[22,30],[-68,-62],[-59,4],[-62,35],[-78,80],[-82,54],[-42,81],[56,-15],[32,-19],[34,93],[57,-100],[-1,-87],[68,-26],[18,86],[-55,-19],[-68,-99],[-9,47],[24,94],[92,97],[5,67],[97,-71],[63,-57],[-52,-14],[-86,-78],[-17,92],[-61,-83],[-84,-10],[20,13],[-68,-47],[7,28],[66,89],[-41,-17],[-14,-46],[-72,-91],[4,52],[-17,-59],[-85,-46],[-94,-23],[-48,-3],[-64,-37],[2,26],[76,88],[-8,-46],[-19,-68]]
    #m = [[2,4]]
    nums2 = TreeNode(4)  
    n = 3
    
   
    result = solution.minDeletionSize_1(nums1)

    #print(solution.ls)

    print(result, 'a' < 'b', nums1, zip(*nums1))