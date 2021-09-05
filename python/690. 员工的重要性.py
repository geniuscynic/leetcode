import sys
from collections import defaultdict
from collections import Counter
import math
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees, id: int) -> int:
        dicts = {}

        for employ in employees:
            dicts[employ.id] = employ

        res = dicts[id].importance

        ls = []
        ls += dicts[id].subordinates
        while ls:
            id = ls.pop()

            res += dicts[id].importance
            ls += dicts[id].subordinates

        return ls




if __name__ == "__main__":
    solution = Solution()
    nums1 = "deeee"
    m = 1
    nums2 = [1,2,3]    
    n = 3

    result = solution.validPalindrome(nums1)

    #print(solution.ls)

    print(result)