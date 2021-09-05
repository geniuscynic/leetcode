import sys
class Solution:
    def majorityElement(self, nums) :
        dicts = {}
        
        index =-1
        res = 0

        for i in nums:
            if i in dicts:
                dicts[i] +=1
            else:
                dicts[i] = 1

            if dicts[i] > res:
                index = i
                res = dicts[i]

        return index


    def majorityElement_1(self, nums) :
       
        vote = 0
        target = 0

        for i in nums:
            if vote ==0:
                target = i
                vote +=1
            elif target== i:
                vote +=1
            else:
                vote -=1


        return target
    
if __name__ == "__main__":
    solution = Solution()
    nums1 = [3,3,4]
    m = -1
    nums2 = [1,2,3]    
    n = 3

    result = solution.majorityElement_1(nums1)

    #print(solution.ls)

    print(nums1, result)