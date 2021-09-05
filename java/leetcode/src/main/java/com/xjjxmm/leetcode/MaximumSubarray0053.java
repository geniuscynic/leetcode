package com.xjjxmm.leetcode;

import com.xjjxmm.Main;

public class MaximumSubarray0053 extends ILeetCode {
    public int maxSubArray(int[] nums) {
        int p = 0, q = 0;
        int res = Integer.MIN_VALUE;


        int sum = 0;
        while (q < nums.length) {
            sum += nums[q];
            res = Math.max(sum, res);
            if(sum < 0) {
                //p = q;
                sum = 0;
            }

            q++;

        }



        return res;

    }

    @Override
    public void run() {
       int nums[] = new int[] {-2};

        print(maxSubArray(nums));

    }
}
