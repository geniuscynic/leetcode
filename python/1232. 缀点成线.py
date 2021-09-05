import sys
from collections import defaultdict
from collections import Counter
class Solution:
    def checkStraightLine(self, coordinates):
        c1 = coordinates[0]
        c2 = coordinates[1]

        flag = False

        if c1[0] == c2[0]:
            flag = True
        else:
            a = (c1[1] - c2[1]) / (c1[0] - c2[0])
            b = c1[1] - a * c1[0]

        
        print(a, b)
        for i in range(2, len(coordinates)):
            if flag:
                if coordinates[i][0] != c1[0]:
                    return False
            else:
                if coordinates[i][1] != a * coordinates[i][0] + b:
                    return False

        return True


if __name__ == "__main__":
    solution = Solution()
    nums1 = [[2,1],[4,2],[6,3]]

    m = [1,2,3,4]

    nums2 = [1,2,3]    
    n = 3

    result = solution.checkStraightLine(nums1)

    #print(solution.ls)

    print(nums1, result)