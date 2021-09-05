import sys
class Solution:
    def countCharacters(self, words, chars):
        
        dicts = {}
        counts = 0
        for c in chars:
            dicts.setdefault(c, 0)
            dicts[c] += 1

        for word in words:
            temp = dicts.copy()
            counts += len(word)
            for j in word:
                if j not in temp:
                    counts -= len(word)
                    break

                temp[j] -= 1

                if(temp[j] < 0):
                    counts -= len(word)
                    break

        return counts


if __name__ == "__main__":
    solution = Solution()
    nums1 = ["cat","bt","hat","tree"]
    m = "atach"

    nums2 = [1,2,3]    
    n = 3

    result = solution.countCharacters(nums1, m)

    #print(solution.ls)

    print(nums1, result)