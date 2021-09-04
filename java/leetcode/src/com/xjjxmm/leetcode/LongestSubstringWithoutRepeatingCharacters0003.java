package com.xjjxmm.leetcode;

import java.util.HashMap;
import java.util.HashSet;

public class LongestSubstringWithoutRepeatingCharacters0003 extends ILeetCode {
    public int lengthOfLongestSubstring(String s) {

        HashMap<Character, Integer> hashSet = new HashMap<Character, Integer>();

        int left = 0, right = 0;
        int distance = 0;
        while (right < s.length()) {
            char temp = s.charAt(right);

            if (hashSet.containsKey(temp)) {

                distance = Math.max(distance, right  - left);

                if(hashSet.get(temp) >= left) {
                    left = hashSet.get(temp) + 1;
                }

            }
            //distance = Math.max(distance, right - left);
            hashSet.put(temp, right);
            right++;
        }

        distance = Math.max(distance, right - left);

        return distance;
    }

    @Override
    public void run() {
       String nums = "tmmzuxt";

      System.out.println(lengthOfLongestSubstring(nums));

        run1();
        run2();
        run3();
        run4();
        run5();
        run6();


    }

    public void run1() {
        String nums = "abcabcbb";

        print(nums);
        print(lengthOfLongestSubstring(nums));

    }

    public void run2() {
        String nums = "bbbbb";

        print(nums);
        print(lengthOfLongestSubstring(nums));

    }

    public void run3() {
        String nums = "pwwkew";

        print(nums);
        print(lengthOfLongestSubstring(nums));

    }


    public void run4() {
        String nums = "";

        print(nums);
        print(lengthOfLongestSubstring(nums));

    }

    public void run5() {
        String nums = "a";

        print(nums);
        print(lengthOfLongestSubstring(nums));

    }

    public void run6() {
        String nums = "abba";

        print(nums);
        print(lengthOfLongestSubstring(nums));

    }

    public void run7() {
        String nums = "dvdf";

        print(nums);
        print(lengthOfLongestSubstring(nums));

    }


}
