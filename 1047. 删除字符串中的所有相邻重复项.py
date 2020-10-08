import sys

class Solution:
    def removeDuplicates(self, S):
        stack = []

        for s in S:
            if not stack:
                stack.append(s)
            elif stack[-1] != s:
                stack.append(s)
            else:
                stack.pop()
                
        return "".join(stack)
            



                          

if __name__ == "__main__":
    solution = Solution()
    nums1 = "abbaca"
    m = 4
    nums2 = [1,2,3]    
    n = 3

    result = solution.removeDuplicates(nums1)

    #print(solution.ls)

    print(nums1, result)