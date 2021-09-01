import sys
from collections import defaultdict
from collections import Counter
class Solution:
    def isValid(self, s):
        ls = []
        for i in s:
            if i in "([{":
               ls.append(i)
            else:
                #print(i)
                if(len(ls) == 0):
                    return False

                temp = ls.pop()
                if temp == "("  and i == ")":
                    continue

                if temp == "["  and i == "]":
                    continue

                if temp == "{"  and i == "}":
                    continue
            
                #print(temp, i)
                return False

        if len(ls) > 0:
            
            return False

        return True


if __name__ == "__main__":
    solution = Solution()
    nums1 = "()[]{}"

    m = [1,2,3,4]

    nums2 = [1,2,3]    
    n = 3

    result = solution.isValid(nums1)

    #print(solution.ls)

    print(nums1, result)