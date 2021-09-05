package com.xjjxmm.leetcode;

import java.util.ArrayList;
import java.util.List;

public class PascalsTriangle118 extends ILeetCode {
    public List<List<Integer>> generate(int numRows) {

        List<List<Integer>> res = new ArrayList<List<Integer>>();

        List<Integer> temp = new ArrayList<>();
        temp.add(1);

        res.add(temp);

        for(int i = 1; i < numRows; i++) {
            temp = new ArrayList<>();
            temp.add(1);
            List<Integer> prev = res.get(i - 1);

            for(int j = 1; j< prev.size(); j++) {
                temp.add(prev.get(j - 1) + prev.get(j));
            }

            temp.add(1);

            res.add(temp);
        }

        return res;
    }

    @Override
    public void run() {
       int nums = 5;

        print(generate(nums));

    }
}
