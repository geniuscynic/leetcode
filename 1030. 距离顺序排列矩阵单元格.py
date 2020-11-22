import sys
from collections import defaultdict
from collections import Counter
from collections import deque

class Solution:

            
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int):
        res = []
        for i in range(R):
            for j in range(C):
                res.append([i, j])

        ret = [[i, j] for i in range(R) for j in range(C)]

        print(res, ret)
        #res.sort(key=lambda x: abs(x[0] - r0) + abs(x[1] - c0))

        return res


    def allCellsDistOrder_1(self, R: int, C: int, r0: int, c0: int):
        res = []
        visit = [] # [[0, 0] for _ in range(R) for _ in range(C)]
        for i in range(R):
            for j in range(C):
                visit.append([0, 0])
        print(visit)
        queue = deque()

        queue.append([r0, c0])

        lens = R * C
        i = 0
        while i < lens and queue:
            print(queue)

            point = queue.popleft()
            
            tr = point[0]
            tc = point[1]

            if tr < 0 or tr >= R:
                continue

            if tc < 0 or tc >= C:
                continue
            
            print(point)
            if visit[tr][tc] == 0:
                res.append(point)
                visit[tr][tc] = 1

                
                #queue += [[tr + 1, tc], [tr - 1, tc], [tr, tc + 1], [tr, tc - 1]]
                queue.append([tr + 1, tc])
                queue.append([tr - 1, tc])
                queue.append([tr, tc + 1])
                queue.append([tr, tc - 1])

                i += 1
                


        return res
                
        
       


if __name__ == "__main__":
    solution = Solution()
    nums1 = 2
    m = 3

    nums2 = 1
    n = 2

    result = solution.allCellsDistOrder_1(nums1, m, nums2, n)

    #print(solution.ls)

    print( result)