import sys
from collections import defaultdict
from collections import Counter
class Solution:
    def reverseVowels(self, s):
        lens = len(s)

        sets = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

    
        ls = []
        for i in range(lens):
            temp = s[i]
            if temp in sets:
                ls.append(i)

        lens2 = len(ls)

        res = list(s)
        for i in range(lens2 // 2):
            i1 = ls[i]
            i2 = ls[lens2 - 1 - i]

            res[i1], res[i2] = res[i2], res[i1]

        print(ls)
        return "".join(res)
        
             
        
if __name__ == "__main__":
    solution = Solution()
    nums1 = "hello"
    m = "111"

    nums2 = [1,2,3]    
    n = 3

    result = solution.reverseVowels(nums1)

    #print(solution.ls)

    print(nums1, result)