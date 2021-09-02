package com.xjjxmm.leetcode;

public abstract class ILeetCode {
    public abstract void run();

    protected void print(int i) {
        System.out.println(i);
    }

    protected void print(int[] nums) {
        for (int num:nums) {
            System.out.print(num);
            System.out.print(", ");
        }

        System.out.println();
    }
}
