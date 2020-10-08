import sys



class Solution:
    def calPoints(self, ops):
        stack = []
        res = 0
        for i in ops:
            
            if i == "+":
                l1 = stack[-1]
                l2 = stack[-2]

                temp = l1 +l2

                #stack.append(l2)
                #stack.append(l1)
                stack.append(temp)
                res += temp
            elif i == "D":
                temp = stack[-1] * 2
                stack.append(temp)
                res += temp
            elif i == "C":
                l = stack.pop()
                res -= l
            else:
                res += int(i)
                stack.append(int(i))

                #print(i)

            #print(res)
                


        return res
                



                          

if __name__ == "__main__":
    solution = Solution()
    nums1 = ["5","2","C","D","+"]
    m = 4
    nums2 = [1,2,3]    
    n = 3

    result = solution.calPoints(nums1)

    #print(solution.ls)

    print(nums1, result)