package com.xjjxmm.leetcode;

import com.xjjxmm.leetcode.ILeetCode;

public class BinarySearch0704 extends ILeetCode {
    public int search(int[] nums, int target) {
        int leth = nums.length;

        int start = 0;
        int end = leth - 1;

        while (start <= end) {
            int middle = (end + 1 + start) / 2;
            if(nums[middle] == target) {
                return  middle;
            }
            else if(nums[middle] < target) {
                start = middle + 1;
            }
            else if(nums[middle] > target) {
                end= middle - 1;
            }

        }

        return -1;
    }

    @Override
    public void run() {
        int[] nums = new int[] {-1,0,3,5,9,12};
        int target = 9;

        System.out.println(search(nums, target));

    }
}
