import sys
class Solution:
    def minimumAbsDifference(self, arr):
        arr.sort()

        lens  = len(arr)

        ls = []
        distance = sys.maxsize
        for i in range(1, lens):
            if arr[i] - arr[i - 1] < distance:
                ls.clear()
                ls.append([arr[i-1], arr[i]])
                distance = arr[i] - arr[i - 1]
            elif arr[i] - arr[i - 1] == distance:
                ls.append([arr[i-1], arr[i]])


        return ls


if __name__ == "__main__":
    solution = Solution()
    nums1 = [1,3,6,10,15]

    m = [1,2,3,4]

    nums2 = [1,2,3]    
    n = 3

    result = solution.minimumAbsDifference(nums1)

    #print(solution.ls)

    print(nums1, result)