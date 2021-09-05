import sys

class MinStack:

    def __init__(self):
        self.ls = []
        self.min = []        

    def push(self, x: int) -> None:
        self.ls.append(x)


    def pop(self) -> None:


    def top(self) -> int:


    def min(self) -> int:


            



                          

if __name__ == "__main__":
    solution = Solution()
    nums1 = ["d1/","d2/","../","d21/","./"]
    m = 4
    nums2 = [1,2,3]    
    n = 3

    result = solution.minOperations(nums1)

    #print(solution.ls)

    print(nums1, result)