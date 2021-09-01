import sys
class Solution:
    def distanceBetweenBusStops(self, distance, start, destination):
        lens = len(distance)
        totals = sum(distance)


        s1,s2 =  start, destination

        if start > destination:
            s1 =  destination
            s2 = start

        t1 = sum(distance[s1:s2])

        return min(t1, totals - t1)


    def distanceBetweenBusStops_1(self, distance, start, destination):
        lens = len(distance)
        totals = 0
        t1 = 0
        s1,s2 =  start, destination

        if start > destination:
            s1 =  destination
            s2 = start

        
        for i in range(lens):
            

            if i >= s1 and i < s2:
                t1 += distance[i]
            else:
                totals += distance[i]


        return min(t1, totals)





if __name__ == "__main__":
    solution = Solution()
    nums1 = [3,6,7,2,9,10,7,16,11]

    m = [1,2,3,4]

    nums2 = [1,2,3]    
    n = 3

    result = solution.distanceBetweenBusStops_1(nums1, 6, 2)

    #print(solution.ls)

    print(nums1, result)