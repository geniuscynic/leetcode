import sys

class CQueue:

    def __init__(self):
        self.ls1 = []
        self.ls2 = []


    def appendTail(self, value: int):
        if not self.ls1:
            self.ls1.append(value)
            return

        while self.ls1:
            self.ls2.append(self.ls1.pop())

        self.ls2.append(value)

        while self.ls2:
            self.ls1.append(self.ls2.pop())


    def deleteHead(self) -> int:
        if self.ls1:
            return self.ls1.pop()

        return -1
            



                          

if __name__ == "__main__":
    solution = Solution()
    nums1 = ["d1/","d2/","../","d21/","./"]
    m = 4
    nums2 = [1,2,3]    
    n = 3

    result = solution.minOperations(nums1)

    #print(solution.ls)

    print(nums1, result)