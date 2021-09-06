package com.xjjxmm.leetcode;

import java.util.List;

public abstract class ILeetCode {
    public abstract void run();

    protected void print(Boolean i) {
        System.out.println(i);
    }

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

    protected void print(int[][] nums) {
        for (int[] num:nums) {
            print(num);
        }

        System.out.println();
    }

    protected void printList(List<Integer> nums) {
        for (int num:nums) {
            System.out.print(num);
            System.out.print(", ");
        }

        System.out.println();
    }

    protected void print(List<List<Integer>> nums) {
        for (List<Integer> num:nums) {
            printList(num);
        }

        System.out.println();
    }

    protected void print(String i) {
        System.out.println(i);
    }

    protected void print(char[] nums) {
        for (int num:nums) {
            System.out.print(num);
            System.out.print(", ");
        }

        System.out.println();
    }
}
