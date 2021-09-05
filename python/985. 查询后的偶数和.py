import sys
class Solution:
    def sumEvenAfterQueries(self, A, queries):
        res = sum(x for x in A if x % 2 == 0)
        

        ls = []
        for x, k in queries:
           
            if A[k] % 2 == 0: S -= A[k]
            A[k] += x
            if A[k] % 2 == 0: S += A[k]
            ls.append(S)


            # res -= temp
            # A[index] = temp +value

            # if value % 2 == 0 and temp % 2 == 0:
            #     res += value
            # elif value % 2 == 0 and temp % 2 == 1:
            #     pass
            # elif value % 2 == 1 and temp % 2 == 0:
            #     res -=temp
            # elif value % 2 == 1 and temp % 2 == 1:
            #     res += value + temp

            # ls.append(res)
            # A[index] = temp +value


            

        return ls

        
       

if __name__ == "__main__":
    solution = Solution()
    nums1 = [1,2,3,4]
    m = [[1,0],[-3,1],[-4,0],[2,3]]

    nums2 = [1,2,3]    
    n = 3

    result = solution.sumEvenAfterQueries(nums1, m)

    #print(solution.ls)

    print(nums1, result)