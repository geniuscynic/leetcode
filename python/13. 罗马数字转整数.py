import sys
from collections import defaultdict
from collections import Counter
class Solution:
    def romanToInt(self, s):
        dicts = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,
        }


        lens = len(s)

        res = 0
        
        i =0
        while i < lens:
            if s[i] in 'IXC' and s[i:i+2] in dicts:
                res += dicts[s[i:i+2]]
                i += 1

            else:
                res += dicts[s[i]]

            i += 1

            #print(i, res)
            
        return res



if __name__ == "__main__":
    solution = Solution()
    nums1 = "MCMXCIV"

    m = [1,2,3,4]

    nums2 = [1,2,3]    
    n = 3

    result = solution.romanToInt(nums1)

    #print(solution.ls)

    print(nums1, result)