package com.xjjxmm.leetcode;

public class FirstBadVersion0278 extends ILeetCode {

    boolean isBadVersion(int version) {
        return version >= 1702766719;
    }
    public int firstBadVersion(int n) {

        int start = 1;
        int end = n;

        while (start < end) {
            int half = start + (end - start) / 2;

            boolean isCurrent = isBadVersion(half);

            if(isCurrent) {
                end = half;
            }
            else {
                start = half + 1;
            }
        }

      return end ;
    }


    @Override
    public void run() {
        int n = 2126753390;
        int result = firstBadVersion(n);

        print(result);
    }
}
