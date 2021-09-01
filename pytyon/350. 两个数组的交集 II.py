import sys
from collections import defaultdict
from collections import Counter
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dicts = {}
        res = []
        for i in nums1:
            if i in dicts:
                dicts[i] += 1
            else:
                dicts[i] = 1

        for i in nums2:
            if i in dicts:
                if dicts[i] > 0:
                    res.append(i)
                    dicts[i] -= 1

        return res

                
        
             
        
if __name__ == "__main__":
    solution = Solution()
    nums1 = "hello"
    m = "111"

    nums2 = [1,2,3]    
    n = 3

    result = solution.reverseVowels(nums1)

    #print(solution.ls)

    print(nums1, result)