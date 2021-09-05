import sys
from collections import defaultdict
from collections import Counter
from collections import deque

class KthLargest:

    def __init__(self, k, nums):

        _size = len(nums)

        if _size < k:
            nums.append(-sys.maxsize-1)

        nums.sort()

       

        self._nums = deque(nums[len(nums) - k : ])
        self._size = len(self._nums)
        self._k = k

        


    def add(self, val):
        if not self._nums:
            self._nums.append(val)
            return val
        
        #if len(self._nums) < self._k:
        print(self._nums,val)

        if val <= self._nums[0]:
            return self._nums[0]
        elif val >=  self._nums[-1]:
            self._nums.popleft()
            self._nums.append(val)
            return self._nums[0]
        else:
            self._nums.popleft()
            temp = []

            #print(self._nums,val)
            while self._nums:
                res = self._nums.popleft()

                if res < val:
                    temp.append(res)
                else:
                    self._nums.appendleft(res)
                    self._nums.appendleft(val)
                    while temp:
                        self._nums.appendleft(temp.pop())

                    #print(self._nums,val)
                    return self._nums[0]

            


        
       


if __name__ == "__main__":
    solution = KthLargest(3, [5, -1])
    print(solution.add(2))
    print(solution.add(1))
    print(solution.add(-1))
    print(solution.add(3))
    print(solution.add(4))
   
    nums1 = [0,1,2,3,4,5,6,7,8]
    m = 2

    nums2 = 0
    n = 1

    #result = solution.sortByBits(nums1)

    #print(solution.ls)

    #print( result)