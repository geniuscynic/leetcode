import sys
from collections import defaultdict
from collections import Counter
class MyQueue:

    def __init__(self):
        self.ls1 = []
        self.ls2 = []


    def push(self, x: int):
        self.ls1.append(x)

        self.ls2.clear()


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """


    def peek(self) -> int:
        """
        Get the front element.
        """


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """


        




        


if __name__ == "__main__":
    solution = Solution()
    shorter = 1
    longer = 2
    k = 3

    nums2 = [1,2,3]    
    n = 3

    result = solution.divingBoard(shorter, longer, k)

    print(result)

    #print(A, B, C)