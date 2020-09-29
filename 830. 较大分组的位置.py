import sys
class Solution:
    def largeGroupPositions(self, s):
        lens = len(s)

        index = 0
        x = s[0]

        ls = []
        for i in range(1, lens):
            if s[i] == x:
                pass
            else:
                if(i - index) >= 3:
                    ls += [[index, i - 1]]
                
                
                index = i
                x = s[i]


        if(lens - index) >= 3:
            ls += [[index, i]]

        return ls

            

if __name__ == "__main__":
    solution = Solution()
    nums1 = "aaa"
    m = 4
    nums2 = [1,2,3]    
    n = 3

    result = solution.largeGroupPositions(nums1)

    #print(solution.ls)

    print(nums1, result)