import sys
from collections import defaultdict
from collections import Counter
class Solution:
    def countSegments(self, s):
        counts = 0
        
        lens = len(s)
        for i in range(1,lens):
            if s[i-1] != " " and s[i] == " ":
                counts += 1


        if lens > 0 and s[-1] != " ":
            counts += 1

        return counts
            
if __name__ == "__main__":
    solution = Solution()
    nums1 = "99  wwww"
    m = "1"

    nums2 = [1,2,3]    
    n = 3

    result = solution.countSegments(nums1)

    #print(solution.ls)

    print(nums1, result)