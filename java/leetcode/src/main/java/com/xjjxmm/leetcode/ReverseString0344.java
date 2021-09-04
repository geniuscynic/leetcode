package com.xjjxmm.leetcode;

import java.util.HashMap;

public class ReverseString0344 extends ILeetCode {
    public void reverseString(char[] s) {


        for (int i =0; i < s.length / 2; i++) {
            char temp = s[i];
            s[i] = s[s.length - 1 - i];

            s[s.length - 1 - i] = temp;
        }

    }


    @Override
    public void run() {
        char[] nums = new char[]{'h','e','l','l','o'};
        reverseString(nums);

        print(nums);

        //run1();
    }


    public void run1() {
        int[] nums = new int[]{0,1,0,3,12};

        //moveZeroes(nums);

        print(nums);
    }
}
