package com.xjjxmm.leetcode;

import java.util.Arrays;
import java.util.HashMap;

public class PermutationinString0567 extends ILeetCode {
    public boolean checkInclusion(String s1, String s2) {
        int[] cnt1 = new int[26];
        int[] cnt2 = new int[26];

        int n = s1.length(), m = s2.length();
        if (n > m) {
            return false;
        }

        for (int i=0; i< n;  i++) {
            ++cnt1[s1.charAt(i) - 'a'];
            ++cnt2[s2.charAt(i) - 'a'];
        }

        if (Arrays.equals(cnt1, cnt2)) {
            return true;
        }

        for (int i = n; i < m; ++i) {
            ++cnt2[s2.charAt(i) - 'a'];
            --cnt2[s2.charAt(i - n) - 'a'];
            if (Arrays.equals(cnt1, cnt2)) {
                return true;
            }
        }
        return false;


    }

    public boolean checkInclusion1(String s1, String s2) {
        int n = s1.length();

        HashMap<Character, Integer> map1 = new HashMap<>();
        for (int i=0; i< n;  i++) {
            if(map1.containsKey(s1.charAt(i))) {
                map1.put(s1.charAt(i), map1.get(s1.charAt(i))+1);
            }
            else {
                map1.put(s1.charAt(i), 1);
            }
        }

        int left = 0, right = left + n;
        while (right <= s2.length()) {
            HashMap<Character, Integer> map2 = new HashMap<>();

            for (int i= left; i < right;  i++) {
                if(!map1.containsKey(s2.charAt(i))) {
                    break;
                }
                if(map2.containsKey(s2.charAt(i))) {
                    map2.put(s2.charAt(i), map2.get(s2.charAt(i))+1);
                }
                else {
                    map2.put(s2.charAt(i), 1);
                }
            }

            if(map1.equals(map2)) {
                return true;
            }

            left++;
            right++;
        }

        return false;
    }

    @Override
    public void run() {
       String s1 = "ab", s2 = "eidboaoo";

      System.out.println(checkInclusion(s1, s2));

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
