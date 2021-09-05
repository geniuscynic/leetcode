package com.xjjxmm.leetcode;

public class FibonacciNumber0509 extends ILeetCode {
    public int Fib(int n) {
        if(n == 0) {
            return 0;
        }

        int x = 0;
        int y = 1;

        for(int i = 1; i < n; i++) {
            int temp = y;
            y  = x + y;

            x = temp;
        }


        return y;

    }

    @Override
    public void run() {
       int nums = 4;

        print(Fib(nums));

    }
}
