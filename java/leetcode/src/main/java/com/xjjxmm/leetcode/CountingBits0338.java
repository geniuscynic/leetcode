package com.xjjxmm.leetcode;

public class CountingBits0338 extends ILeetCode {
    public int[] countBits(int n) {

        int[] res = new int[n+1];

        for (int i = 0; i <= n; i++) {
            res[i] = (i & 1) + res[i >> 1];


        }

        return res;
    }

    public int toBin(int n) {
        int total = 0;

        while (n > 0) {
            if (n % 2 == 1) {
                total++;
            }
            n = n / 2;


        }

        return total;
    }

    @Override
    public void run() {
        int nums = 5;

        print(countBits(nums));

    }
}
