import sys
from collections import defaultdict
from collections import Counter
class Solution:
    def findComplement(self, num: int) -> int:
        res = 0

        temp = num

        while temp != 0:
            temp = temp >> 1
            res += 1

        
        return ((1 << 3) - 1) ^ num




if __name__ == "__main__":
    solution = Solution()
    nums1 = 5
    m = [5,6,7,8]

    nums2 = [1,2,3]    
    n = 3

    result = solution.findComplement(nums1)

    #print(solution.ls)

    print(nums1, result)