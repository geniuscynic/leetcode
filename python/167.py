import sys
class Solution:
    def twoSum(self, numbers, target):
        lens = len(numbers)
       
        for i in reversed(range(lens)):
            if(numbers[0]> 0 and numbers[i] > target):
                continue

            for j in reversed(range(i)):
               
                if(numbers[i] + numbers[j] < target):
                    break

                if(numbers[i] + numbers[j] == target):
                    return [j +1, i + 1]


        return []

    def twoSum_1(self, numbers, target):
        lens = len(numbers)

        p =0
        q = lens- 1
        
        while p < q:
            if(numbers[p] + numbers[q] > target):
                q -=1

            elif(numbers[p] + numbers[q] < target):
                p +=1

            
            else:
                break


        return [p +1, q+1]




if __name__ == "__main__":
    solution = Solution()
    nums1 = [-1, 0]
    m = -1
    nums2 = [1,2,3]    
    n = 3

    result = solution.twoSum_1(nums1, m)

    #print(solution.ls)

    print(nums1, result)