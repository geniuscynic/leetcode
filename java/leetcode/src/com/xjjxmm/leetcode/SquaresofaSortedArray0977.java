package com.xjjxmm.leetcode;

public class SquaresofaSortedArray0977 extends ILeetCode{

    public int[] sortedSquares(int[] nums) {
        int left =0;
        int right = nums.length - 1;

        int[] res = new int[nums.length];
        int step = right;
        while (left <= right) {

                if(-nums[left] >= nums[right]) {
                    res[step] = nums[left] * nums[left];
                    left++;
                }
                else {
                    res[step] =  nums[right] * nums[right];
                    right--;
                }
                step--;

        }

        return res;
    }

    @Override
    public void run() {
        int[] nums = new int[]{1,3,5,6};

        int[] res = sortedSquares(nums);

        print(res);
    }
}
