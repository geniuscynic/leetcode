import sys
from collections import defaultdict
from collections import Counter
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles

        while numBottles >= numExchange:
            #print(numBottles)
            res += numBottles // numExchange
            numBottles = numBottles % numExchange + numBottles // numExchange

        return res


if __name__ == "__main__":
    solution = Solution()
    nums1 = 2
    m = 3

    nums2 = [1,2,3]    
    n = 3

    result = solution.numWaterBottles(nums1, m)

    #print(solution.ls)

    print( result)