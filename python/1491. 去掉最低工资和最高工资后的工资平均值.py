import sys
from collections import defaultdict
from collections import Counter
from collections import deque

class Solution:

    def average(self, salary: List[int]) -> float:
        salary.sort()


        return sum(salary[1:-1]) / (len(salary) - 2)
        
       


if __name__ == "__main__":
    solution = Solution()
    nums1 = 2
    m = 3

    nums2 = 1
    n = 2

    result = solution.allCellsDistOrder_1(nums1, m, nums2, n)

    #print(solution.ls)

    print( result)