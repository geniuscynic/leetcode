import sys
from collections import defaultdict
from collections import Counter
class Solution:
    def longestCommonPrefix(self, strs):
        strs.sort(key =  lambda x: len(x))

        lens = len(strs)
        if lens == 0:
            return ""

        if lens == 1:
            return strs[0]


        f = strs[0]

        f_end = len(f)

        #if f_end > 1:
        for i in range(f_end):
            for j in reversed(range(i+1, f_end+1)):
                    temp = f[i:j]
                    #print(temp)
                    count = 0
                    for k in range(1, lens):
                        if temp not in strs[k]:
                            break

                        count = k

                    if count == lens - 1:
                        return temp
        # else:
        #     count = 0
        #     for k in range(1, lens):
        #         if f not in strs[k]:
        #             break

        #         count = k

        #         if count == lens - 1:
        #             return f


        
        return ""


    def longestCommonPrefix_1(self, strs):
        
        lens = len(strs)
        if lens == 0:
            return ""

        if lens == 1:
            return strs[0]


        f = strs[0]

        f_end = len(f)

        start = 0
        currentIndex = f_end // 2 + 1

        #print(start, currentIndex)
        while start != currentIndex and currentIndex <= f_end:
            for i in range(f_end):
                temp = f[:currentIndex]  
                count = 0
                for k in range(1, lens):
                    if temp not in strs[k]:
                        break

                        count = k

                if count == lens - 1:
                    currentIndex += (f_end - currentIndex) // 2 + 1
                else:
                    start = currentIndex
                    currentIndex -= (currentIndex - start) // 2 + 1

                print(start, currentIndex)
                
            
        # else:
        #     count = 0
        #     for k in range(1, lens):
        #         if f not in strs[k]:
        #             break

        #         count = k

        #         if count == lens - 1:
        #             return f


        
        return ""


if __name__ == "__main__":
    solution = Solution()
    nums1 = ["c","c"]

    m = [1,2,3,4]

    nums2 = [1,2,3]    
    n = 3

    result = solution.longestCommonPrefix_1(nums1)

    #print(solution.ls)

    print(nums1, result)