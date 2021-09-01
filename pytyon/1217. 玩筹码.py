import sys
from collections import defaultdict
from collections import Counter
class Solution:
    def minCostToMoveChips(self, position):
        l1, l2 = 0, 0

        for i in position:
            if i % 2 == 0:
                l1 += 1
            else:
                l2 += 1
        

        #print(max(min_map.values()))
        

        return min(l1, l2)


if __name__ == "__main__":
    solution = Solution()
    nums1 = [1,2,3]

    m = [1,2,3,4]

    nums2 = [1,2,3]    
    n = 3

    result = solution.minCostToMoveChips(nums1)

    #print(solution.ls)

    print(nums1, result)