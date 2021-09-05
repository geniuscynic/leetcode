import sys
from collections import defaultdict
from collections import Counter
import re
class Solution:
    def checkRecord(self, s):
        ma1 = re.match(".*?L{3,}.*?", s)
        ma2 = re.match(".*?(A+).*?A.*?", s)


        if ma1:
            #print("ma1", ma1.group())
            return False

        if ma2:    
            #print("ma2", ma2.group())
            return False

        return True

    def checkRecord_1(self, s):
        ma1 = re.match(".*(LLL|A.*A).*", s)
        #ma2 = re.match(".*?(A+).*?A.*?", s)


        if ma1:
            print("ma1", ma1.group())
            return False

        

        return True




            
            
            
if __name__ == "__main__":
    solution = Solution()
    nums1 = "PPAALLALA"
    m = 2

    nums2 = [1,2,3]    
    n = 3

    result = solution.checkRecord_1(nums1)

    #print(solution.ls)

    print(nums1, result)