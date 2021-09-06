package com.xjjxmm.leetcode;

import java.util.Arrays;
import java.util.HashMap;

public class MinCostClimbingStairs0746 extends ILeetCode {


    public int minCostClimbingStairs(int[] cost) {
       int left = 0;
       int res = 0;

       int n = cost.length;
       while (left < n - 2) {
           if(cost[left + 2] + cost[left] > cost[left + 1]) {
               res += cost[left + 1];
               left += 2;
           }
           else {
               res+= cost[left + 2] + cost[left];
               left+=3;
           }
       }

       if(left == n - 2) {
           res += Math.min(cost[n-1], cost[n-2]);
       }

//       if(left == n - 3) {
//           res += Math.min(cost[n-1], cost[n-2]);
//       }
//       else {
//           res += cost[n-2];
//       }

       return res;
    }

        public int minCostClimbingStairs2(int[] cost) {
            int[] memo = new int[cost.length];
            Arrays.fill(memo, -1);
            return minCostClimbingStairs(cost, memo.length - 1, memo);
        }

        public int minCostClimbingStairs(int[] cost, int n, int[] memo) {


           if(n == 0) {
                memo[0] = cost[0];
            }

            if(n == 1) {
                memo[1] = cost[1];
            }

            if(memo[n] > 0) {
                return memo[n];
            }

            int t1 = minCostClimbingStairs(cost, n - 1, memo);
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
