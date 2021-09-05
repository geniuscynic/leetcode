import sys
from collections import defaultdict
from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dicts = {}

        for i in s:
            if i in dicts:
                dicts[i] += 1
            else:
                dicts[i] = 1

        for i in t:
            if i in dicts:

                if dicts[i] == 0:
                    return i

                dicts[i] -= 1

            else:
                return i

        return ''


    def findTheDifference(self, s: str, t: str) -> str:
        return chr(sum(map(ord, t)) - sum(map(ord, s)))



                
        
             
        
if __name__ == "__main__":
    solution = Solution()
    nums1 = "hello"
    m = "111"

    nums2 = [1,2,3]    
    n = 3

    result = solution.reverseVowels(nums1)

    #print(solution.ls)

    print(nums1, result)