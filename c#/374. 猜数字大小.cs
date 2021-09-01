using System;

namespace leetcode
{
    public class GuessGame {
        public int guess(int num) {
            var picker = 1702766719;

            if(num < picker) {
                return 1;
            }
            else if (num == picker) {
                return 0;
            }
            return -1;
        }
    }

    public class Solution374 : GuessGame {
       
        public int GuessNumber(int n) {
            var left = 1;
            var right = n;

            while(left < right) {
                var middle = left + (right - left)/ 2;

                Console.WriteLine($"{left}, {right}, {middle}");

                var temp = guess(middle); 
                if (temp == 0) {
                    return middle;
                } 
                else if (temp == -1) {
                    right = middle;
                }
                else {
                    if  (left == middle) {
                        left ++;
                    }
                    else {
                        left = middle;
                    }
                }
            }

            return left;
        }
    }
}