import sys
from collections import defaultdict
from collections import Counter

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def helper(self, nums, size):
        if size < 0:
            return 0

        if size == 0:
            return nums[size]

        if size == 1:
            return max(nums[:2])

        c1 = self.helper(nums, size -1)
        c2 = self.helper(nums, size -2) + nums[size]
        
        return max(c1, c2)

    def rob(self, nums) -> int:

        return self.helper(nums, len(nums) - 1)


    def rob1(self, nums) -> int:
        n2, n1 = 0, 0
        
        for i in range(len(nums)):
            temp1 = n2 + nums[i]
            temp2 = n1

            
            n2, n1 = n1, max(temp1, temp2)
            #res+= n1

            #print(i, n2, n1, res)

        return n1
                


if __name__ == "__main__":
    solution = Solution()
    nums1 = [2]

    m = [1,2,3,1]

    nums2 = [1,2,3]    
    n = 3

    result = solution.rob1(nums1)

    #print(solution.ls)

    print(result)