package com.xjjxmm.leetcode;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;

public class Matrix0542 extends ILeetCode {

    public int[][] updateMatrix(int[][] mat) {

        int m = mat.length, n = mat[0].length;

        int[][] res = new int[m][n];

        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                res[i][j] = -1;
            }
        }

        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                res[i][j] = GetDistance(mat, res, i, j, 0);
            }
        }

        return res;
    }

    public int GetDistance(int[][] mat, int[][] res, int i, int j, int step) {
        if(mat[i][j] == 0) {
            return step;
        }

        if( i < 0 || i >= mat.length || j < 0 || j >= mat[0].length) {
            return Integer.MAX_VALUE;
        }

        if(res[i][j] > -1) {
            return res[i][j] + step;
        }


        if(i == 2 && j==1) {
            print(res);
        }
        int t1 = GetDistance(mat, res,i - 1, j,step + 1);
        if(t1 <= step + 1) {
            return t1;
        }

        int t2 = GetDistance(mat, res,i + 1, j,step + 1);
        if(t2 <= step + 1) {
            return t2;
        }

        int t3= GetDistance(mat, res,i , j-  1,step + 1);
        if(t3 <= step + 1) {
            return t3;
        }

        int t4 = GetDistance(mat, res,i, j + 1,step + 1);
        if(t4 <= step + 1) {
            return t4;
        }

        int d1 = Math.min(t1, t2);
        int d2 = Math.min(t3, t4);

        res[i][j] = Math.min(d1, d2);;
        return res[i][j] ;

    }

    @Override
    public void run() {
        int[][] image = new int[][]{
//                {1,1,0,0,0},
//                {1,1,0,0,0},
//                {0,0,0,1,1},
//                {0,0,0,1,1}
                // {0,0,1,0,0,0,0,1,0,0,0,0,0},
                //{0,0,0,0,0,0,0,1,1,1,0,0,0},
                // {0,1,1,0,1,0,0,0,0,0,0,0,0},
                /*{0,1,0,0,1,1,0,0,1,0,1,0,0},
                {0,1,0,0,1,1,0,0,1,1,1,0,0},
                {0,0,0,0,0,0,0,0,0,0,1,0,0},
                {0,0,0,0,0,0,0,1,1,1,0,0,0},
                {0,0,0,0,0,0,0,1,1,0,0,0,0}*/

                {0, 0, 0},
                {0, 1, 0},
                {1, 1, 1},

        };

        int[][] res = updateMatrix(image);
        print(res);
        //print(image);
//        run1();
//        run2();
//        run3();
//        run4();
//        run5();
//        run6();


    }

//    public void run1() {
//        String nums = "abcabcbb";
//
//        print(nums);
//        print(lengthOfLongestSubstring(nums));
//
//    }
//
//    public void run2() {
//        String nums = "bbbbb";
//
//        print(nums);
//        print(lengthOfLongestSubstring(nums));
//
//    }
//
//    public void run3() {
//        String nums = "pwwkew";
//
//        print(nums);
//        print(lengthOfLongestSubstring(nums));
//
//    }
//
//
//    public void run4() {
//        String nums = "";
//
//        print(nums);
//        print(lengthOfLongestSubstring(nums));
//
//    }
//
//    public void run5() {
//        String nums = "a";
//
//        print(nums);
//        print(lengthOfLongestSubstring(nums));
//
//    }
//
//    public void run6() {
//        String nums = "abba";
//
//        print(nums);
//        print(lengthOfLongestSubstring(nums));
//
//    }
//
//    public void run7() {
//        String nums = "dvdf";
//
//        print(nums);
//        print(lengthOfLongestSubstring(nums));
//
//    }


}
