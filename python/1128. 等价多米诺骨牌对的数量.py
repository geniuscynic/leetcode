import sys
class Solution:
    def numEquivDominoPairs(self, dominoes):
        lens = len(dominoes)

        counts = 0

        dicts = {}
        for i in range(lens):
            k = dominoes[i][0]
            v = dominoes[i][1]

            res = 10 * k + v if k < v else 10 * v + k
            

            if res not in dicts:
                dicts[res] = 1
            else:
                counts += dicts[res]
                dicts[res] += 1

        
            
        return counts


if __name__ == "__main__":
    solution = Solution()
    nums1 = [[2,1],[5,4],[3,7],[6,2],[4,4],[1,8],[9,6],[5,3],[7,4],[1,9],[1,1],[6,6],[9,6],[1,3],[9,7],[4,7],[5,1],[6,5],[1,6],[6,1],[1,8],[7,2],[2,4],[1,6],[3,1],[3,9],[3,7],[9,1],[1,9],[8,9]]
    m = [2,1,4,3,9,6]

    nums2 = [1,2,3]    
    n = 3

    result = solution.numEquivDominoPairs(nums1)

    #print(solution.ls)

    print(nums1, result)