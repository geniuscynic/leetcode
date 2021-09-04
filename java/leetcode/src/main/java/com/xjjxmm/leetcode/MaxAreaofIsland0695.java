package com.xjjxmm.leetcode;

import java.util.LinkedList;
import java.util.Queue;

public class MaxAreaofIsland0695 extends ILeetCode {
    public int maxAreaOfIsland(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int maxDistince = 0;

        Queue<Integer> queueX = new LinkedList<>();
        Queue<Integer> queueY = new LinkedList<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int distince = 0;

                //if(grid[i][j] == 1) {
                queueX.offer(i);
                queueY.offer(j);

                while (!queueX.isEmpty()) {
                    int x = queueX.poll(), y = queueY.poll();
                    if (x < 0 || y < 0 || x == grid.length || y == grid[0].length || grid[x][y] != 1) {
                        continue;
                    }
                    grid[x][y] = -1;
                    distince++;
                    //print(grid);

                    queueX.offer(x + 1);
                    queueY.offer(y);

                    queueX.offer(x - 1);
                    queueY.offer(y);

                    queueX.offer(x);
                    queueY.offer(y + 1);

                    queueX.offer(x);
                    queueY.offer(y - 1);


                }

                maxDistince = Math.max(maxDistince, distince);
            }
        }

        return maxDistince;
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

                {1, 0, 1, 0, 0},
                {1, 1, 1, 0, 0},
                {0, 0, 1, 0, 0},

        };

        int res = maxAreaOfIsland(image);
        print(res);
        print(image);
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
