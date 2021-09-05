import sys
class RecentCounter:

    def __init__(self):
        self.ls = collections.deque()

    def ping(self, t: int) -> int:
       
        self.ls.append(t)
        
        temp = t - 3000

        
        while self.ls.index(0) < temp:
            self.ls.popleft()


        return len(self.ls)





        

        
       

if __name__ == "__main__":
    solution = Solution()
    nums1 = [9,8,7,6,5,4,3,2,1,0]
    m = 4
    nums2 = [1,2,3]    
    n = 3

    result = solution.validMountainArray(nums1)

    #print(solution.ls)

    print(nums1, result)