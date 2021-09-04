package com.xjjxmm.leetcode;

import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;

public class FloodFill0733 extends ILeetCode {
    //HashSet<String> set;
    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        int oldColor = image[sr][sc];

        //set = new HashSet<>();
        floodFill(image, sr, sc, oldColor, newColor);

        return  image;
    }

    public void floodFill(int[][] image, int sr, int sc, int oldColor, int newColor) {
//        String key = sr + "," + sc;
//        if(set.contains(key)) {
//            return;
//        }
//        else {
//            set.add(key);
//        }

        if(sr < 0) {
            return;
        }

        if(sr >= image.length) {
            return;
        }

        if(sc < 0) {
            return;
        }

        if(sc >= image[0].length) {
            return;
        }

        int color = image[sr][sc];

        if(oldColor != color) {
            return;
        }

        if(oldColor == newColor) {
            return;
        }

        image[sr][sc] = newColor;

        floodFill(image, sr + 1,sc, oldColor, newColor);
        floodFill(image, sr - 1,sc, oldColor, newColor);
        floodFill(image, sr,sc + 1, oldColor, newColor);
        floodFill(image, sr,sc - 1, oldColor, newColor);
    }

    @Override
    public void run() {
        int[][] image = new int[][]{
                {0,0,0},
                {0,1,1},
                //{1,0,1}
        };
        int sr = 1, sc = 1, newColor = 1;

        int[][] res = floodFill(image, sr,sc, newColor);
        print(res);
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
