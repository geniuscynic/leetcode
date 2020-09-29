import sys
class Solution:
    def sortArrayByParityII(self, A):
        

        lens= len(A)

        for i in range(lens):
            if i % 2 == 0 and A[i] % 2 == 0:
                continue

            if i % 2== 1 and A[i] % 2 ==1:
                continue

            for j in range(i + 1, lens, 2):
                if i % 2 == 0 and A[j] % 2 == 1:
                    continue

                if i % 2== 1 and A[j] % 2 ==0:
                    continue

                temp = A[i]
                A[i] = A[j]
                A[j] = temp

                break

        return A
       

if __name__ == "__main__":
    solution = Solution()
    nums1 = [4,2,5,7]
    m = 4
    nums2 = [1,2,3]    
    n = 3

    result = solution.sortArrayByParityII(nums1)

    #print(solution.ls)

    print(nums1, result)