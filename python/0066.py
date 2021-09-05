class Solution:
    def plusOne(self, digits):

        for i in reversed(range(len(digits))):
            digits[i] +=  1

            if(digits[i] > 9):
                digits[i] = 0
            else:
                return digits

            
        
        digits.insert(0, 1)


        return digits 




if __name__ == "__main__":
    solution = Solution()
    t1 =  [1,2,3]
    t2 = 6

    result = solution.plusOne(t1)

    #print(solution.ls)

    print(t1, result)