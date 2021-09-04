package com.xjjxmm.leetcode;

import java.util.HashMap;

public class TwoSumIIInputarrayissorted0167 extends ILeetCode {
    public int[] twoSum(int[] numbers, int target) {
        int left =1, right = numbers.length;

        while (left < right) {
            if(target - numbers[right - 1] > numbers[left - 1]) {
                left ++;
            }
            else if(target - numbers[right - 1] < numbers[left - 1]) {
                right --;
            }
            else {
                return  new int[] {left, right};
            }
        }

        return  new int[] {left, right};

    }
        public int[] twoSum1(int[] numbers, int target) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

        for (int i = 0; i < numbers.length; i++) {
            if(map.containsKey(target - numbers[i]) && map.get(target - numbers[i]) != i + 1) {
                return new int[] { map.get(target - numbers[i]), i + 1}  ;
            }
            else {
                map.put(numbers[i], i + 1);
            }
        }

        return null;
    }

    @Override
    public void run() {
        int[] nums = new int[]{2,7,11,15};
        int[] res = twoSum(nums, 9);

        print(res);

        run1();
    }


    public void run1() {
        int[] nums = new int[]{0,1,0,3,12};

        //moveZeroes(nums);

        print(nums);
    }
}
