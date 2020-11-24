import sys
from collections import defaultdict
from collections import Counter
from collections import deque

class Solution:
    def sortString(self, s: str) -> str:
        slist = list(s)
        res = []
        index = []

        slist.sort()

        for i in range(len(slist)):
            if slist[i] not in res:
                res.append(slist[i])
                index.append(i)
                
        
        for i in index:
        slist.remove()

        
       


if __name__ == "__main__":
    solution = Solution()
    nums1 = [0,1,2,3,4,5,6,7,8]
    m = 2

    nums2 = 0
    n = 1

    result = solution.sortByBits(nums1)

    #print(solution.ls)

    print( result)