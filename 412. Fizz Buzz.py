import sys
from collections import defaultdict
from collections import Counter
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ls = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                ls.append("FizzBuzz")

            elif i % 3 == 0:
                ls.append("Fizz")

            elif i % 5 == 0:
                ls.append("Buzz")

            else:
                ls.append(str(i))

        return ls



if __name__ == "__main__":
    solution = Solution()
    nums1 = "abccccdd"
    m = "111"

    nums2 = [1,2,3]    
    n = 3

    result = solution.longestPalindrome(nums1)

    #print(solution.ls)

    print(nums1, result)