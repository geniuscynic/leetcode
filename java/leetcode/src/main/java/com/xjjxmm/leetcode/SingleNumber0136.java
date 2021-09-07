package com.xjjxmm.leetcode;

import java.util.HashMap;
import java.util.HashSet;

public class SingleNumber0136 extends ILeetCode {
    public int singleNumber(int[] nums) {
        HashSet<Integer> map = new HashSet<Integer>();

        for (int n: nums
             ) {
            if(map.contains(nums)) {
                map.remove(n);
            }
            else {
                map.add(n);
            }

        }

        return map.iterator().next();
    }

    @Override
    public void run() {
       //int nums = 3;

        //print(reverseBits(nums));

    }
}
