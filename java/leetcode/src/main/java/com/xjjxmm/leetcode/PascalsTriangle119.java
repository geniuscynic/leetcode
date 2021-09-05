package com.xjjxmm.leetcode;

import java.util.ArrayList;
import java.util.List;

public class PascalsTriangle119 extends ILeetCode {
    public List<Integer> generate(int rowIndex) {

        List<Integer> prev = new ArrayList<>();
        prev.add(1);

        for(int i = 1; i <= rowIndex; i++) {
            List<Integer> temp = new ArrayList<>();
            temp.add(1);

            for(int j = 1; j< prev.size(); j++) {
                temp.add(prev.get(j - 1) + prev.get(j));
            }

            temp.add(1);

            prev = temp;

        }

       return  prev;
    }

    @Override
    public void run() {
       int nums = 5;

        printList(generate(nums));

    }
}
