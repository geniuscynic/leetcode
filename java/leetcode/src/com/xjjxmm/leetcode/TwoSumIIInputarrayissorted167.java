package com.xjjxmm.leetcode;

import java.util.HashMap;

public class TwoSumIIInputarrayissorted167 extends ILeetCode {
    public int[] twoSum(int[] numbers, int target) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

        for (int i = 0; i < numbers.length; i++) {
            if(map.containsKey(target - numbers[i]) && map.get(target - numbers[i]) != i + 1) {
                return new int[] { target - numbers[i], i + 1}  ;
            }
            else {
                map.put(numbers[i], i + 1);
            }
        }

        return null;
    }

    @Override
    public void run() {
        int[] nums = new int[]{2, 0};
        //moveZeroes(nums);

        print(nums);

        run1();
    }


    public void run1() {
        int[] nums = new int[]{0,1,0,3,12};

        //moveZeroes(nums);

        print(nums);
    }
}
