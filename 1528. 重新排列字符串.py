import sys
from collections import defaultdict
from collections import Counter
from collections import deque

class Solution:

    def restoreString(self, s, indices):
        res = []
        dicts = {}

        for i in range(len(indices)):
            dicts[indices[i]] = s[i]

        print(dicts)

        sorted(dicts.values(), key=dicts.key())
        #indices.sort()
        
        # print(indices)
        # for i in indices:
        #     old = dicts[i]
        #     print(old, s[old])
        #     res.append(s[old])

        # print(res)
        return "".join(res)
                


if __name__ == "__main__":
    solution = Solution()
    nums1 = "codeleet"
    m = [4,5,6,7,0,2,1,3]

    nums2 = 1
    n = 2

    result = solution.restoreString(nums1, m)

    #print(solution.ls)

    print( result)