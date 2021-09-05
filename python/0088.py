class Solution:
    def merge(self, nums1, m, nums2, n):

        i = m - 1
        j = n - 1
            
        while(i >=0 and j >=0):
            if( nums1[i] >= nums2[j]):
                nums1[i + j + 1] = nums1[i]
                i -=1
            else:
                nums1[i + j + 1] = nums2[j]
                j -=1
            
        while j >=0:
            nums1[j] = nums2[j]
            j-=1

if __name__ == "__main__":
    solution = Solution()
    nums1 = [4,5,6,0,0,0]
    m = 3
    nums2 = [1,2,3]    
    n = 3

    result = solution.merge(nums1,m,nums2,n)

    #print(solution.ls)

    print(nums1, result)