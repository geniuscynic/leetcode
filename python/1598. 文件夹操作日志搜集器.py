import sys

class Solution:
    def minOperations(self, logs):
        stack = []

        for l in logs:
            if l == "../":
                if stack:
                    stack.pop()
                continue

            if l == "./":
                continue

            stack.append(l)

        
        return len(stack)
            



                          

if __name__ == "__main__":
    solution = Solution()
    nums1 = ["d1/","d2/","../","d21/","./"]
    m = 4
    nums2 = [1,2,3]    
    n = 3

    result = solution.minOperations(nums1)

    #print(solution.ls)

    print(nums1, result)