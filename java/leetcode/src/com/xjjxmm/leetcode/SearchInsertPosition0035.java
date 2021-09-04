package com.xjjxmm.leetcode;

public class SearchInsertPosition0035 extends ILeetCode{

    public int searchInsert(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;

        while (left < right) {
            int half = left + (right - left) / 2;

            int current = nums[half];

            if(current < target) {
                left = half + 1;
            }
            else if(current > target) {
                right = half;
            }
            else {
                return  half;
            }
        }

        if(nums[right]< target) {
            right ++;
        }

        return right;

    }


    @Override
    public void run() {
        int[] nums = new int[]{1,3,5,6};
        int target = 7;

        int result = searchInsert(nums, target);

        print(result);
    }
}
