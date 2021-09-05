import sys
from collections import defaultdict
from collections import Counter
import math
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        res = set()

        if num == 1:
            return False
            
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                res.add(i)
                res.add(num // i)

        res.add(1)


        return sum(res) == num



if __name__ == "__main__":
    solution = Solution()
    nums1 = "--a-a-a-a--"

    m = 2
    nums2 = [1,2,3]    
    n = 3

    result = solution.licenseKeyFormatting(nums1, m)

    #print(solution.ls)

    print(result)