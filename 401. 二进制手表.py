import sys
from collections import defaultdict
from collections import Counter
class Solution:
    def helper(self, num: int):
        res = 0

        while(num != 0):
            num = num & (num - 1)

            res += 1

        return res

        
    def readBinaryWatch(self, num: int):
        dicts = {}

        ls = []
        for i in range(12):
            if i not in dicts:
                dicts[i] = self.helper(i)

            
            for j in range(60):
                if j not in dicts:
                    dicts[j] = self.helper(j)

               

                if dicts[i] + dicts[j] == num:
                    ls.append("{}:{:02d}".format( i, j))

        
        return ls


if __name__ == "__main__":
    solution = Solution()
    nums1 = 1
    m = "111"

    nums2 = [1,2,3]    
    n = 3

    result = solution.readBinaryWatch(nums1)

    #print(solution.ls)

    print(nums1, result)