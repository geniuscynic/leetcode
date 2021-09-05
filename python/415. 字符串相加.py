import sys
from collections import defaultdict
from collections import Counter
class Solution:
    def addStrings(self, num1, num2):
        i, j = len(num1) - 1, len(num2) - 1

  
        carry = 0

        ls = []
        while i >= 0 or j >= 0:
            print(ls, i, j, carry)   
            if carry == 0 and i < 0 and j >= 0:
                ls.reverse()
                return num2[0:j+1] + "".join(ls)

            if carry == 0 and j < 0 and i>= 0:
                ls.reverse()
                
                return num1[0:i+1] + "".join(ls)

            a = 0 if i < 0 else int(num1[i])
            b = 0 if j < 0 else int(num2[j])

            i -= 1
            j -= 1

            temp = a + b + carry
            carry = temp // 10
            ls.append(str(temp % 10))


        if carry > 0:
            ls.append('1')

        ls.reverse()
        return "".join(ls)

            
if __name__ == "__main__":
    solution = Solution()
    nums1 = "99"
    m = "1"

    nums2 = [1,2,3]    
    n = 3

    result = solution.addStrings(nums1, m)

    #print(solution.ls)

    print(nums1, result)