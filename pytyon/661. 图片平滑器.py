import sys
class Solution:
    def imageSmoother(self, M):
        R, C = len(M), len(M[0])
        ans = [[0] * C for _ in M]

        for r in range(R):
            for c in range(C):
                count = 0
                for nr in (r-1, r, r+1):
                    for nc in (c-1, c, c+1):
                        if 0 <= nr < R and 0 <= nc < C:
                            ans[r][c] += M[nr][nc]
                            count += 1
                ans[r][c] //= count

        return ans

            
            

        



                          

if __name__ == "__main__":
    solution = Solution()
    nums1 = [1,12,-5,-6,50,3]
    m = 4
    nums2 = [1,2,3]    
    n = 3

    result = solution.findMaxAverage_1(nums1, m)

    #print(solution.ls)

    print(nums1, result)