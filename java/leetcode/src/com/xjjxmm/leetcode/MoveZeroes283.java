package com.xjjxmm.leetcode;

public class MoveZeroes283 extends ILeetCode {
    public void moveZeroes(int[] nums) {
        int left = 0, right = 0;

       while (left  < nums.length) {
            if(nums[left] == 0) {

                right++;
            }
            else {
                int tmp = nums[left - right];
                nums[left - right] = nums[left];
                nums[left] = tmp;
            }

            left++;
       }

    }

    @Override
    public void run() {
        int[] nums = new int[]{2, 0};
        moveZeroes(nums);

        print(nums);

        run1();
    }


    public void run1() {
        int[] nums = new int[]{0,1,0,3,12};

        moveZeroes(nums);

        print(nums);
    }
}
