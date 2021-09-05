class Solution:
    def twoSum(self, nums, target):
        lens = len(nums)

       
        for i in range(lens):
            #print(i)
            for j in range(i+1, lens):
                #print(nums[i], nums[j], target)
                if nums[i] + nums[j] == target:
                    #print("aa")
                    return [i, j]

        return []

    def twoSum_2(self, nums, target):
        lens = len(nums)

        dicts = {}

        for i in range(lens):
            another = target - nums[i]
            if(another in dicts):
                return [dicts[another], i]

            dicts[nums[i]] = i

        #print(dicts)
        for k,v in dicts.items():
            another = target - k

            #print(k, another)
            if(k!=another and another in dicts):
                return [v, dicts[another]]
        
        

        return []




if __name__ == "__main__":
    solution = Solution()
    t1 = [3, 2, 4]
    t2 = 6

    result = solution.twoSum_2(t1, t2)

    print(result)