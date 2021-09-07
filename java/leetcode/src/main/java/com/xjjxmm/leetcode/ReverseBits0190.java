package com.xjjxmm.leetcode;

public class ReverseBits0190 extends ILeetCode {
    public int reverseBits(int n) {
        int res = 0;

        while (n != 0) {
            if((n & 1) == 1) {
                res += 1;
            }

            n = n >> 1;
            res = res << 1;
        }

        return res;
    }

    @Override
    public void run() {
       int nums = 3;

        print(reverseBits(nums));

    }
}
