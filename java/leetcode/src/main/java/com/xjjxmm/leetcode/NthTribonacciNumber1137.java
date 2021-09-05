package com.xjjxmm.leetcode;

public class NthTribonacciNumber1137 extends ILeetCode {
    public int tribonacci(int n) {
        if(n == 0) {
            return 0;
        }
        int x = 0;
        int y = 1;
        int z = 1;

        int temp = 0;
        for(int i = 2; i < n; i++) {
            temp = z;
            z  = x + y + z;
            x = y;
            y = temp;
        }


        return z;

    }

    @Override
    public void run() {
       int nums = 25;

        print(tribonacci(nums));

    }
}
