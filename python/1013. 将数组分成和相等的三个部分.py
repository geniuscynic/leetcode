import sys
class Solution:
    def canThreePartsEqualSum(self, A):
        avg = sum(A) / 3

        res = 0

        f1 = 0
        for i in A:
            res += i

            if f1 == 2:
                return True
                
            if res == avg:
                res = 0
                f1 +=1

                

        return False

if __name__ == "__main__":
    solution = Solution()
    nums1 = [1,-1,1,-1]
    m = 34

    nums2 = [1,2,3]    
    n = 3

    result = solution.canThreePartsEqualSum(nums1)

    #print(solution.ls)

    print(nums1, result)