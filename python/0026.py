class Solution:
    def removeDuplicates(self, nums):
        
        dicts = {}

        index = 0


        for i in range(0,len(nums)):
            n= nums[i]


            if nums[i] not in dicts:
                
                dicts[n] = i

                if i != index:
                    nums[index] = n

                index +=1
                
             

        return index

    def removeDuplicates_2(self, nums):
        
            index = 1

            for i in range(1,len(nums)):
            
                if nums[i] != nums[i-1]:
                    if(index !=i):
                        nums[index] = nums[i]
                    index += 1                
                

            return index


if __name__ == "__main__":
    solution = Solution()
    t1 =  [-1,0,0,0,0,3,3]

    result = solution.removeDuplicates_2(t1)

    print(t1, result)