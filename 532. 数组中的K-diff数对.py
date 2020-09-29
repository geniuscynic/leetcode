import sys
class Solution:
    
    def findPairs(self, nums, k):
        dicts = {}
        counts = 0

        for i in nums:
            if i in dicts:
                dicts[i] += 1

                if k ==0 and dicts[i] == 2:
                    counts += 1
            else:
                dicts[i] = 1

                
                if k > 0:
                    if (i + k) in dicts:
                        counts += 1

                    if (i - k) in dicts:
                        counts += 1

                        

        return counts

                
                

            

            




if __name__ == "__main__":
    solution = Solution()
    nums1 = [-1,0,0,1,0,0,-1]
    m = 1
    nums2 = [1,2,3]    
    n = 3

    result = solution.findPairs(nums1, m)

    #print(solution.ls)

    print(nums1, result)