import sys
from collections import defaultdict
from collections import Counter
class Solution:
    def addBinary(self, a: str, b: str):
        la, lb = len(a), len(b)

        if la < lb:
            tmp = a
            a = b
            b = tmp

            tmp = la
            la = lb
            lb = tmp

        res = ""
        needAdd = 0
        index = la - lb

        #print(a, b)
        for i in reversed(range(lb)):
            a1 = int(a[i + lb])
            b1 = int(b[i])

            
            tmp = a1 + b1 + needAdd
            if tmp >1:
                tmp -= 2
                needAdd = 1
            else:
                needAdd = 0

            res = str(tmp) + res

            #print(a1, b1, res)
            

        print(res, needAdd)
        if needAdd >= 1:
            for i in reversed(range(lb, la)):
                a1 = int(a[i - lb])
               
                tmp = a1 + needAdd
                if tmp >1:
                    tmp -= 2
                    needAdd = 1
                else:
                    needAdd = 0
                    index = i - lb
                    break

                res = str(tmp) + res
        
        print(res, needAdd, index)
                


        if index < la - lb:
            res = a[:index] + res

        #print(res, needAdd)
        if needAdd >= 1:
            res = "1" + res

        return res

    def addBinary_1(self, a: str, b: str):
        la, lb = len(a), len(b)

        if la < lb:
            tmp = a
            a = b
            b = tmp

            tmp = la
            la = lb
            lb = tmp
            
        lsa, lsb = list(a), list(b)

        #la, lb = len(a), len(b)
        #print(lsa, lsb)

        needAdd = 0
        res = []
        while la > 0:
            a1,b1 = 0, 0
            
            
            a1 = int(lsa.pop())

            if lb > 0:
                b1 = int(lsb.pop())

            #print(lsa, lsb)

            la -= 1
            lb -= 1

            tmp = a1 + b1 + needAdd
            if tmp >1:
                tmp -= 2
                needAdd = 1
            else:
                needAdd = 0

            res.append(str(tmp))

            print(res, lb,  needAdd, lsa)
            if needAdd == 0 and lb <= 0:
                lsa.reverse()
                res += lsa
                break

            if needAdd > 0 and la == 0:
                res.append("1")

        res.reverse()

        
        return "".join(res)


    def addBinary_2(self, a: str, b: str):
        la, lb = len(a), len(b)

        lsa, lsb = list(a), list(b)

        #la, lb = len(a), len(b)
        #print(lsa, lsb)

        needAdd = 0
        res = []
        while la > 0 and  lb > 0:
            a1,b1 = 0, 0
            
            
            a1 = lsa.pop() - '0'
            b1 = lsb.pop() - '0'

            #print(lsa, lsb)

            la -= 1
            lb -= 1

            tmp = a1 + b1 + needAdd
            needAdd = tmp // 2
            res.append(str(tmp % 2))

           
        while la > 0:
            a1 = lsa.pop() - '0'
            tmp = a1 + needAdd
            needAdd = tmp // 2
            res.append(str(tmp % 2))

            la - = 1

        while lb > 0:
            b1 = lsb.pop() - '0'
            tmp = b1 + needAdd
            needAdd = tmp // 2
            res.append(str(tmp % 2))

            lb - = 1

        
        if needAdd > 0:
            res.append('1')

        

        res.reverse()

        
        return "".join(res)
                

        
if __name__ == "__main__":
    solution = Solution()
    nums1 = "1"
    m = "111"

    nums2 = [1,2,3]    
    n = 3

    result = solution.addBinary_1(nums1, m)

    #print(solution.ls)

    print(nums1, result)