package com.xjjxmm.leetcode;

import java.util.Arrays;
import java.util.HashMap;

public class MinCostClimbingStairs0746 extends ILeetCode {



        public int minCostClimbingStairs(int[] cost) {
            int[] memo = new int[cost.length];
            Arrays.fill(memo, -1);
            return Math.min(minCostClimbingStairs(cost, memo.length - 1, memo), minCostClimbingStairs(cost, memo.length - 2, memo));
        }

        public int minCostClimbingStairs(int[] cost, int n, int[] memo) {


           if(n == 0) {
                memo[0] = cost[0];
            }

            if(n == 1) {
                memo[1] = cost[1];
            }

            if(memo[n] > -1) {
                return memo[n];
            }

            int t1 = minCostClimbingStairs(cost, n - 1, memo) + cost[n];
            int t2 = minCostClimbingStairs(cost, n - 2, memo) + cost[n];

            memo[n] = Math.min(t1, t2);

            return memo[n];
        }


    @Override
    public void run() {
        int[] num = new int[] { 0,0,1,0 };


        int res = minCostClimbingStairs(num);

        print(res);
    }
}
