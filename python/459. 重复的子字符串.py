import sys
from collections import defaultdict
from collections import Counter
import re
class Solution:
    def repeatedSubstringPattern(self, s):

        line = "abcabcabc"
        # .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
        matchObj = re.match( r'(.*?)', line)

        if matchObj:
            print ("matchObj.group() : ", matchObj.group())
            print ("matchObj.group(1) : ", matchObj.group(1))
            #print ("matchObj.group(2) : ", matchObj.group(2))
           
        else:
            print ("No match!!")


        lens = len(s)

        if lens % 2 == 1:
            return False

        m = lens // 2
        if s[:m] == s[m:]:
            return True

        return False
            
if __name__ == "__main__":
    solution = Solution()
    nums1 = "abab"
    m = "1"

    nums2 = [1,2,3]    
    n = 3

    result = solution.repeatedSubstringPattern(nums1)

    #print(solution.ls)

    print(nums1, result)