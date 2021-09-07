package com.xjjxmm.leetcode;

import java.util.Arrays;

public class HouseRobberII0213 extends ILeetCode {
    public int rob(int[] nums) {
        if(nums.length == 1) {
            return nums[0];
        }

        int[] memo1 = new int[nums.length];
        int[] memo2 = new int[nums.length];

        Arrays.fill(memo1, -1);
        Arrays.fill(memo2, -1);
        return Math.max(
                rob(nums, 0, nums.length - 2, memo1),
                rob(nums, 1, nums.length - 1, memo2));
    }

    public int rob(int[] nums, int start, int end, int[] memo) {
        if(start > end) {
            return 0;
        }

        if(end < 0) {
            return 0;
        }
        if(end==0) {
            return nums[0];
        }

        if(memo[end] > -1) {
            return memo[end];
        }

        int r1 = rob(nums, start, end - 1 , memo);
        int r2 = rob(nums, start,end - 2, memo) + nums[end];

        memo[end] = Math.max(r1, r2);
        return memo[end];
    }

    @Override
    public void run() {
        int[] nums = new int[] {2,1};
        int k = 2;

        int res = rob(nums);

        print(res);
    }
}
