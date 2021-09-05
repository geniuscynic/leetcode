import sys
from collections import defaultdict
from collections import Counter
class Solution:
    def countAndSay(self, n):
        strs = "1"
        for i in range(2, n + 1):
            temp = ""
            first = ""
            couter = 0
            lens = len(strs)
            for j in range(lens):
                if first == "":
                    first = strs[j]
                    couter +=1
                    continue

                if strs[j] == first:
                    couter+=1
                else:
                    temp += "{}{}".format(couter, first)

                    first = strs[j]
                    couter = 1

                
            temp += "{}{}".format(couter, first)

            first = ""
            couter = 0

            print(temp)

            strs=temp
            temp=""

        return strs

    def countAndSay_1(self, n):
        strs = "1"
        for _ in range(n - 1):
            i, temp = 0, ''
            for j, c in enumerate(strs):
                if c != strs[i]:
                    temp += "{}{}".format(j - i, strs[i])
                    i = j

                
                
            strs = temp + "{}{}".format(len(strs) - i, strs[-1])
            print(strs)

          
        return strs

                


if __name__ == "__main__":
    solution = Solution()
    nums1 = 6
    m = "issi"

    nums2 = [1,2,3]    
    n = 3

    result = solution.countAndSay_1(nums1)

    #print(solution.ls)

    print(nums1, result)