import sys
from collections import defaultdict
from collections import Counter
import math
class Solution:
    def constructRectangle(self, area: int) -> List[int]:

        temp = int(math.sqrt(area)) + 1
        for i in reversed( range(1, temp)):
            if area % i == 0:
                return [i, area//i]

if __name__ == "__main__":
    solution = Solution()
    nums1 = "--a-a-a-a--"

    m = 2
    nums2 = [1,2,3]    
    n = 3

    result = solution.licenseKeyFormatting(nums1, m)

    #print(solution.ls)

    print(result)