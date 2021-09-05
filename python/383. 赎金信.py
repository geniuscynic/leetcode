import sys
from collections import defaultdict
from collections import Counter
class Solution:
   def canConstruct(self, ransomNote, magazine):
       l1,l2 = len(ransomNote), len(magazine)

       if l1 > l2:
           return False

        dicts =  Counter(magazine)
        for i in ransomNote:
            if i not in dicts:
                return False

            if dicts[i] <= 0:
                return False

            dicts[i] -= 1

        return True

        
if __name__ == "__main__":
    solution = Solution()
    nums1 = "ab2a"
    m = "111"

    nums2 = [1,2,3]    
    n = 3

    result = solution.isPalindrome_1(nums1)

    #print(solution.ls)

    print(nums1, result)