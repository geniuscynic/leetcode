import sys
from collections import defaultdict
from collections import Counter
class Solution:
    def isPalindrome(self, s):
        lens = len(s)

        p, q = 0, lens - 1

        while(p < q and q > 0):
            f = ord(s[p])
            if 97 <= f <= 122 or 48 <= f <=57:
                pass
            elif 65 <= f <= 90:
                f += 32
            else:
                p += 1
                continue


            l = ord(s[q])
            if 97 <= l <= 122 or 48 <= l <=57:
                pass
            elif 65 <= l <= 90:
                l += 32
            else:
                q -= 1
                continue

            print(f, l)
            if f != l:
                return False

            p += 1
            q -= 1

        return True


    def isPalindrome_1(self, s):
        lens = len(s)

        p, q = 0, lens - 1

        while(p < q ):
            while p < q and not s[p].isalnum():
                p += 1

            while p < q and not s[q].isalnum():
                q -= 1
            
            if p < q and s[p].lower() != s[q].lower():
                return False


            p += 1
            q -= 1


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