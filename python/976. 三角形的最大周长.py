import sys
from collections import defaultdict
from collections import Counter
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        
        A.sort(reverse = True)

        for i in range(2, len(A)):
            if(A[i] + A[i - 1] > A[i - 2]):
                return sum(A[i-2:i+1])

        return 0
        


if __name__ == "__main__":
    solution = Solution()
    nums1 = 2
    m = 3

    nums2 = [1,2,3]    
    n = 3

    result = solution.numWaterBottles(nums1, m)

    #print(solution.ls)

    print( result)