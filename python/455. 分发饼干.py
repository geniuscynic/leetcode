import sys
from collections import defaultdict
from collections import Counter
class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()

        leng = len(g)
        lens = len(s)

        q = 0
        res = 0
        for i in range(leng):
            for j in range(q, lens):
                q = j + 1
                print(q)
                if s[j] >= g[i]:
                    res += 1
                    break

        
                
        return res
                






if __name__ == "__main__":
    solution = Solution()
    nums1 = [10,9,8,7]

    m = [5,6,7,8]

    nums2 = [1,2,3]    
    n = 3

    result = solution.findContentChildren(nums1, m)

    #print(solution.ls)

    print(nums1, result)