import sys
class Solution:
    def numPairsDivisibleBy60(self, time):
        dicts = {}
        res = 0
        for t in time:
            temp = t % 60
            i = 60 - temp

            if i == 60:
                res += dicts[0]
            else:
                res += dicts[i]

            dicts.setdefault( temp, 0)
            dicts[temp] += 1

        return res

if __name__ == "__main__":
    solution = Solution()
    nums1 = [30,20,150,100,40]
    m = 34

    nums2 = [1,2,3]    
    n = 3

    result = solution.numPairsDivisibleBy60(nums1)

    #print(solution.ls)

    print(nums1, result)