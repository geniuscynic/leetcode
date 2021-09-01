class Solution:
    def searchInsert(self, nums, target):
        index= 0

        for i in range(len(nums)):
            if(nums[i] >= target):
                return i
            
           
        return len(nums)

    def searchInsert_1(self, nums, target):
        left,right = 0, len(nums)-1

        
        while(left <= right):
            if(nums[left] >=target):
                return left
            elif(nums[right] < target):
                return right + 1
            elif (nums[right] == target):
                return right
            elif left == right:
                return left
            else:
                left +=1
                right -=1
            
        

        return left 



if __name__ == "__main__":
    solution = Solution()
    t1 =  [1]
    t2 = 0

    result = solution.searchInsert_1(t1, t2)

    print(t1, result)