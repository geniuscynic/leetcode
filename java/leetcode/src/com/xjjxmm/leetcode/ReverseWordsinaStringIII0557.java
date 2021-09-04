package com.xjjxmm.leetcode;

public class ReverseWordsinaStringIII0557 extends ILeetCode {

    public String reverseWords(String s) {
        String[] sarray = s.split(" ");
        StringBuilder sb = new StringBuilder();

        for (int i =0; i < sarray.length; i++) {
            String sa = sarray[i];

            char[] res = sa.toCharArray();
            reverseString(res);

            sb.append(res);

            if(i != sarray.length - 1) {
                sb.append(" ");
            }
        }

        return  sb.toString();
    }

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
