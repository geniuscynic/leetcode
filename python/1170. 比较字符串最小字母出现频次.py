import sys
class Solution:
    def coutchart(self, chars):
        lens = len(chars)

        counts = 1
        minchar = chars[0]

        for i in range(1, lens):
            if minchar > chars[i]:
                minchar = chars[i]
                counts = 1
                continue

            if minchar == chars[i]:
                counts += 1

        return counts
            



    def numSmallerByFrequency(self, queries, words):
        ls1 = []
        mins = sys.maxsize
        for q in queries:
            res = self.coutchart(q)

            mins = min(mins, res)
            ls1.append(res)

        print(ls1, mins)
        ls2 = []
        for w in words:
            if len(w) <= mins:
                continue

            res = self.coutchart(w)

            if res <= mins:
                continue

            ls2.append(res)

        
        res = []
        for i in ls1:
            counts = 0
            for j in ls2:
                if i < j:
                    counts += 1

            res.append(counts)




        return res


if __name__ == "__main__":
    solution = Solution()
    nums1 = ["bba","abaaaaaa","aaaaaa","bbabbabaab","aba","aa","baab","bbbbbb","aab","bbabbaabb"]

    m = ["aaabbb","aab","babbab","babbbb","b","bbbbbbbbab","a","bbbbbbbbbb","baaabbaab","aa"]

    nums2 = [1,2,3]    
    n = 3

    result = solution.numSmallerByFrequency(nums1, m)

    #print(solution.ls)

    print(nums1, result)