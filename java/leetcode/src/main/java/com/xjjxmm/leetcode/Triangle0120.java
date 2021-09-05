package com.xjjxmm.leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Triangle0120 extends ILeetCode {
    public int minimumTotal(ArrayList<ArrayList<Integer>> triangle) {
        return 0;
    }

    @Override
    public void run() {
        ArrayList<ArrayList<Integer>> nums = new ArrayList<ArrayList<Integer>>() {
            {
                add(new ArrayList<Integer>(Arrays.asList(3, 4)));
                add(new ArrayList<Integer>(Arrays.asList(3, 4)));
                add(new ArrayList<Integer>(Arrays.asList(6, 5, 7)));
                add(new ArrayList<Integer>(Arrays.asList(4, 1, 8, 3)));
            }
        };

        int res = minimumTotal(nums);

        print(res);
    }
}
