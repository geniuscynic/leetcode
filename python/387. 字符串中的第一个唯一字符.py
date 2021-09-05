import sys
from collections import defaultdict
from collections import Counter
class Solution:
    def firstUniqChar(self, s):
        lens = len(s)
        index = 0
        dicts = {}

        for i in range(lens):
            tmp = s[i] 
            if tmp not in dicts:
                dicts[tmp] = 1
                continue
            else:
                dicts[tmp] += 1

            if tmp == s[index]:
                index += 1
                #print(dicts)
                while index < lens and s[index] in dicts  and dicts[s[index]] > 1:
                    index += 1
                
                if index >= lens:
                    return -1



        return index if index != lens else -1


    
    def firstUniqChar_1(self, s):
        lens = len(s)
        index = 0
        dicts = Counter(s)

        for i in range(lens):
            tmp = s[i] 
            if dicts[tmp] == 1:
                return i



        return -1
            


        
if __name__ == "__main__":
    solution = Solution()
    nums1 = "aadadaad"
    m = "111"

    nums2 = [1,2,3]    
    n = 3

    result = solution.firstUniqChar(nums1)

    #print(solution.ls)

    print(nums1, result)