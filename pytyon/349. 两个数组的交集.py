import sys
from collections import defaultdict
from collections import Counter
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = set(nums1)
        
        res = set()

        for i in nums2:
            if i in n1:
                res.add(i)

        return list(res)
        
             
        
if __name__ == "__main__":
    solution = Solution()
    nums1 = "hello"
    m = "111"

    nums2 = [1,2,3]    
    n = 3

    result = solution.reverseVowels(nums1)

    #print(solution.ls)

    print(nums1, result)