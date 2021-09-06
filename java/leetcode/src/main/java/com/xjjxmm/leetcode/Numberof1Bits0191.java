package com.xjjxmm.leetcode;

public class Numberof1Bits0191 extends ILeetCode {
    public int hammingWeight(int n) {
            int count = 0;
            while (n != 0) {
                n = n  & (n-1);

                count++;
            }

            return  count;
    }

    @Override
    public void run() {
       int nums = 3;

        print(hammingWeight (nums));

    }
}
