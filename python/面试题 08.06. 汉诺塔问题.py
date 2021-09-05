import sys
from collections import defaultdict
from collections import Counter
class Solution:
    dicts = {}

    def helper(self, n, A, B, C):
        if n == 1:
            C.append(A.pop())
            return

        
        self.helper(n - 1, A, C, B)
        C.append(A.pop())
        self.helper(n - 1, B, A, C)

        

    def hanota(self, A, B, C):
        self.helper(len(A), A, B, C)


        




        


if __name__ == "__main__":
    solution = Solution()
    A = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    B = []
    C = []
    m = [1,2,3,4]

    nums2 = [1,2,3]    
    n = 3

    result = solution.hanota(A, B, C)

    #print(solution.ls)

    print(A, B, C)