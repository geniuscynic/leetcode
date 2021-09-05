import sys
from collections import defaultdict
from collections import Counter
class Solution:
    def reverseString(self, s):
        lens = len(s)

        for i in range(lens // 2):
            temp =s[i]
            s[i] = s[lens - i - 1]
            s[lens - i - 1] = temp
        
             ["A"," ","m","a","n",","," ","a"," ","p","l","a","n",","," ","a"," ","c","a","n","a","l",":"," ","P","a","n","a","m","a"]
             ["a","m","a","n","a","P"," ",":","l","a","n","a","c"," ","a",",","n","a","l","p"," ","a"," ",",","n","a","m"," ","A"]
             ["a","m","a","n","a","P"," ",":","l","a","n","a","c"," ","a"," ",",","n","a","l","p"," ","a"," ",",","n","a","m"," ","A"]   

        
if __name__ == "__main__":
    solution = Solution()
    nums1 = "ab2a"
    m = "111"

    nums2 = [1,2,3]    
    n = 3

    result = solution.isPalindrome_1(nums1)

    #print(solution.ls)

    print(nums1, result)