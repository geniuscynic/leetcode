import sys
class Solution:
    def commonChars(self, A):
        lens  = len(A)

        A.sort(key=lambda x: len(x))

        dicts = {}
        for i in A[0]:
            if i not in dicts:
                dicts[i] = 1
            else:
                dicts[i] += 1

        c = 0
        ls = []
        for k,v in dicts.items():
            c = v

            for i in range(1, lens):
                res = A[i].count(k)
                c = min(c, res)

                if res <=0:
                    break

            
            if c > 0:
                ls += [k] * c 

        
        return ls
                




        
       

if __name__ == "__main__":
    solution = Solution()
    nums1 = ["cool","lock","cook"]
    m = 34

    nums2 = [1,2,3]    
    n = 3

    result = solution.commonChars(nums1)

    #print(solution.ls)

    print(nums1, result)