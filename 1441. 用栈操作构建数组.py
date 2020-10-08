import sys

class Solution:
    def buildArray(self, target, n):
        ls = [i for i in reversed(range(1, n + 1))]

        res = []
        for i in target:
            while(ls.pop() != i):
                res.append("Push")
                res.append("Pop")
            else:
                res.append("Push")


        return res

            



                          

if __name__ == "__main__":
    solution = Solution()
    nums1 = [2,3,4]
    m = 4
    nums2 = [1,2,3]    
    n = 3

    result = solution.buildArray(nums1, m)

    #print(solution.ls)

    print(nums1, result)