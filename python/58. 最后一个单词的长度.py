import sys
from collections import defaultdict
from collections import Counter
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res =  s.split(" ")
        res.reverse()
        
        for i in res:
            if i != "":
                return len(i)

        return 0

                


if __name__ == "__main__":
    solution = Solution()
    nums1 = "aa vvv"
    m = "issi"

    nums2 = [1,2,3]    
    n = 3

    result = solution.lengthOfLastWord(nums1)

    #print(solution.ls)

    print(nums1, result)