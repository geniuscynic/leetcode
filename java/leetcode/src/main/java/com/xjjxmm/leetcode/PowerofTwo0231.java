package com.xjjxmm.leetcode;

public class PowerofTwo0231 extends ILeetCode {
    public boolean isPowerOfTwo(int n) {
            if(n <= 0) {
                return false;
            }
            while (n > 1) {
                if( (n & 1) == 1) {
                    return  false;
                }

                n = n >> 1;
            }

            return  true;
    }

    @Override
    public void run() {
       int nums = 12;

        print(isPowerOfTwo(nums));

    }
}
