import sys



class Solution:
    def backspaceCompare(self, S, T):
        stack1 = []
        for s in S:
            if s == "#":
                stack1.pop()
            else:
                stack1.append(s)

        
        stack2 = []
        for s in T:
            if s == "#":
                stack2.pop()
            else:
                stack2.append(s)

        
        if len(stack1) != len(stack2):
            return False

        while stack1:
            if(stack1.pop() != stack2.pop()):
                return False

        return True
            


                          

if __name__ == "__main__":
    solution = Solution()
    nums1 = ["5","2","C","D","+"]
    m = 4
    nums2 = [1,2,3]    
    n = 3

    result = solution.calPoints(nums1)

    #print(solution.ls)

    print(nums1, result)