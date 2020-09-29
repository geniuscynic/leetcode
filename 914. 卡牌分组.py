import sys
class Solution:
    def hasGroupsSizeX(self, deck):
        dicts= {}

        if len(deck) < 2:
            return False
            
        for i in deck:
            if i not in dicts:
                dicts[i] = 1
            else:
                dicts[i] += 1

        
        ls =  sorted(list(dicts.values()))

       
        for i in range(len(ls)):
            if ls[i] < 2:
                return False

            if(ls[i] % ls[0] != 0):
                return False
          

        return True
            
       

if __name__ == "__main__":
    solution = Solution()
    nums1 = [1,1,2,2,2,2]
    m = 4
    nums2 = [1,2,3]    
    n = 3

    result = solution.hasGroupsSizeX(nums1)

    #print(solution.ls)

    print(nums1, result)