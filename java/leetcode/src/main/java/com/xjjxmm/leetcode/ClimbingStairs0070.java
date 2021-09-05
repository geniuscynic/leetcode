package com.xjjxmm.leetcode;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class ClimbingStairs0070 extends ILeetCode {
    HashMap<Integer, Integer> map = new HashMap<>();
    public int climbStairs(int n) {
        if(n == 1) {
            return 1;
        }

        if(n ==  0) {
            return 1;
        }

        if(!map.containsKey(n)) {
            map.put(n, climbStairs(n - 1) + climbStairs( n - 2));

        }

        return map.get(n);
    }

    @Override
    public void run() {
        int n = 45;
        int k = 2;

        int res = climbStairs(n);

        print(res);
    }
}
