import sys
from collections import defaultdict
from collections import Counter
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        lens = len(nums1)

        ls = []
        ls2 = []
        for i in range(lens):
            ls.append(-1)
            ls2.append(-1)
       

        for i in range(len(nums1)):
            flag = False
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    flag = True
                    continue

                if flag and nums2[j] > nums1[i]:
                    ls[i] = nums2[j]
                    flag = False
                    break

        return ls

    def nextGreaterElement_1(self, nums1, nums2):
        dic, stack = {}, []

        for i in range(len(nums2) - 1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            if stack: dic[nums2[i]] = stack[-1]
            stack.append(nums2[i])
            print(stack)

        return [dic.get(x, -1) for x in nums1]

if __name__ == "__main__":
    solution = Solution()
    nums1 = [4,1,2]
    m = [1,2,4,3]
    nums2 = [1,2,3]    
    n = 3

    result = solution.nextGreaterElement_1(nums1, m)

    #print(solution.ls)

    print(nums1, result)