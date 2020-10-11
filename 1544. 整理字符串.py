import sys

class Solution:
    def makeGood(self, s):
        stack = []

        for ss in s:
            if not stack:
                stack.append(ss)
                continue

            if abs(ord(stack[-1]) - ord(ss)) == 32:
                stack.pop()
                continue

            stack.append(ss)

        return "".join(stack)

        
            



                          

if __name__ == "__main__":
    solution = Solution()
    nums1 = "leEeetcode"
    m = 4
    nums2 = [1,2,3]    
    n = 3

    result = solution.makeGood(nums1)

    #print(solution.ls)

    print(nums1, result)