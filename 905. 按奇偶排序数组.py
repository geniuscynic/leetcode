import sys
class Solution:
    def sortArrayByParity(self, A):
        rows = len(A)
        ls = []

        for i in A:
            if i % 2 == 0:
                ls.insert(0, i)
            else:
                ls.append(i)


        return ls

if __name__ == "__main__":
    solution = Solution()
    nums1 = [[1,2,3],[4,5,6]]
    m = 4
    nums2 = [1,2,3]    
    n = 3

    result = solution.transpose(nums1)

    #print(solution.ls)

    print(nums1, result)