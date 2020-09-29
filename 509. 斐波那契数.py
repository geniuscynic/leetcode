import sys
class Solution:
    dicts = {}
    def fib(self, N):
        if(N == 0):
            return 0

        if(N == 1):
            return 1

        if N in self.dicts:
            return dicts[N]

        self.dicts[N] = self.fib(N - 1) + self.fib(N - 2) 
        return self.dicts[N]


if __name__ == "__main__":
    solution = Solution()
    nums1 = 2
    m = 1
    nums2 = [1,2,3]    
    n = 3

    result = solution.fib(nums1)

    #print(solution.ls)

    print(nums1, result)