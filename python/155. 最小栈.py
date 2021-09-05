import sys
from collections import defaultdict
from collections import Counter
class MinStack:
    
    def __init__(self):
        self.ls = []
        self.minstack = [math.inf]


    def push(self, x: int) -> None:
        self.ls.append(x)
        self.minstack.append(min(x, self.minstack[-1]))

    def pop(self) -> None:
        self.ls.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.ls[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
        
            

    


                

        
if __name__ == "__main__":
    solution = Solution()
    nums1 = [1,2, 3]
    m = "111"

    nums2 = [1,2,3]    
    n = 3

    result = solution.subsets(nums1)

    #print(solution.ls)

    print(nums1, result)