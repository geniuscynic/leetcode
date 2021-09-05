import sys
from collections import defaultdict
from collections import Counter
class Solution:
    dicts = {}

    def divingBoard(self, shorter, longer, k):
        

        if k == 0:
            return []

        if shorter == longer:
            return [shorter * k]

        res = [0] * (k + 1)

        for i in range(k+1):
            res[i] = (shorter * (k - i) + longer * i)

        #ls = sorted(list(res))
        return res



        




        


if __name__ == "__main__":
    solution = Solution()
    shorter = 1
    longer = 2
    k = 3

    nums2 = [1,2,3]    
    n = 3

    result = solution.divingBoard(shorter, longer, k)

    print(result)

    #print(A, B, C)