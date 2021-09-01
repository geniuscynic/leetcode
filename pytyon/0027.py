class Solution:
    def removeElement(self, nums, val):
        index= 0

        for i in range(len(nums)):
            if(nums[i] != val):

                if(index!= i):
                    nums[index] = nums[i]

                index  += 1
           
        return index



if __name__ == "__main__":
    solution = Solution()
    t1 =  [0,1,2,2,3,0,4,2]
    t2 = 2

    result = solution.removeElement(t1, 2)

    print(t1, result)