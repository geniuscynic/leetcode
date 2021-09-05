package com.xjjxmm.leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class BestTimetoBuyandSellStock121 extends ILeetCode {
    public int maxProfit(int[] prices) {

        int left = 0;
        int res = -1;
        for(int i = 1; i< prices.length; i++) {
            if(prices[i] < prices[left]) {
                left = i;
            }
            else {
                res = Math.max(prices[i] - prices[left], res);
            }

            //int temp = prices[i] - prices[left];
        }

        return Math.max(res, 0);


    }

    @Override
    public void run() {
       int nums[] = new int[] {7,1,5,3,6,4};

        print(maxProfit(nums));

    }
}
