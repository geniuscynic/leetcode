package com.xjjxmm.leetcode;

public class RotateArray189 extends ILeetCode {
    public void rotate(int[] nums, int k) {
        k = k % nums.length;

        int[] res = new int[nums.length];

        for (int i=0; i < res.length; i++) {
            res[i] = nums[res.length - k + i];
        }

        System.arraycopy(res, 0, nums, 0, nums.length);

    }

    @Override
    public void run() {
        int[] nums = new int[]{1,3,5,6};

       rotate(nums, 2);

        print(nums);
    }
}
