import sys

class Solution:
    def removeOuterParentheses(self, S):
        stack = []

        res = ""
        for s in S:
            if s == "(":
                if len(stack) > 0:
                    res += "("

                stack.append(s)
                
            else:
                stack.pop()

                if len(stack) > 0:
                    res += ")"

        return res
                    

            



                          

if __name__ == "__main__":
    solution = Solution()
    nums1 = ["5","2","C","D","+"]
    m = 4
    nums2 = [1,2,3]    
    n = 3

    result = solution.calPoints(nums1)

    #print(solution.ls)

    print(nums1, result)