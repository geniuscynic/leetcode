package com.xjjxmm.leetcode;

import java.util.Arrays;
import java.util.HashMap;

public class HouseRobber0198 extends ILeetCode {
    public int rob(int[] nums) {
        int[] memo = new int[nums.length];
        Arrays.fill(memo, -1);
        return rob(nums, nums.length - 1, memo);
    }

    public int rob(int[] nums, int end, int[] memo) {
        if(end < 0) {
            return 0;
        }
        if(end==0) {
            return nums[0];
        }

        if(memo[end] > -1) {
            return memo[end];
        }

        int r1 = rob(nums, end - 1 , memo);
        int r2 = rob(nums, end - 2, memo) + nums[end];

        memo[end] = Math.max(r1, r2);
        return memo[end];
    }

    @Override
    public void run() {
        int[] nums = new int[] {2,7,9,3,1};
        int k = 2;

        int res = rob(nums);

        print(res);
    }
}
