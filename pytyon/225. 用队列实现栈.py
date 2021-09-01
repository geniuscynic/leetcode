import sys
from collections import defaultdict
from collections import Counter
from collections import deque
class MyStack:

    def __init__(self):
       self.ls1 = deque()
       self.ls2 = deque()

    def push(self, x: int) -> None:
        self.ls2.append(x)

        while self.ls1:
            self.ls2.append(self.ls1.popleft())

        self.ls1, self.ls2 = self.ls2, self.ls1

    def pop(self) -> int:
        temp = self.ls1.

        self.ls.remove(temp)

        return temp        


    def top(self) -> int:
        return self.ls[-1]


    def empty(self) -> bool:
        return len(self.ls) == 0

            

    


                

        
if __name__ == "__main__":
    solution = Solution()
    nums1 = [1,2, 3]
    m = "111"

    nums2 = [1,2,3]    
    n = 3

    result = solution.subsets(nums1)

    #print(solution.ls)

    print(nums1, result)