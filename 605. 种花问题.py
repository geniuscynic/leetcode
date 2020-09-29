import sys
class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        lens = len(flowerbed)


       if n ==0:
            return True
            
        if lens == 1:
            if flowerbed[0] == 1:
                return False

            if n > 1:
                return False

            return True

        for i in range(lens):
            if flowerbed[i] == 0:
                if i == 0 and flowerbed[i + 1] == 0:
                    n -=1
                    flowerbed[i] = 1
                    continue

                
                if i < lens- 1 and flowerbed[i-1]== 0 and flowerbed[i + 1] == 0:
                    n -=1
                    flowerbed[i] = 1
                    continue

                if i == lens- 1 and flowerbed[i-1]== 0:
                    n -=1
                    flowerbed[i] = 1
                    continue

               

        return True if n <=0 else False

                          

if __name__ == "__main__":
    solution = Solution()
    nums1 = [1,0,0,0,0,0,1]
    m = 2
    nums2 = [1,2,3]    
    n = 3

    result = solution.canPlaceFlowers(nums1, m)

    #print(solution.ls)

    print(nums1, result)