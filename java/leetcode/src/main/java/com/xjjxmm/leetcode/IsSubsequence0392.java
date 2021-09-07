package com.xjjxmm.leetcode;

import java.util.*;

public class IsSubsequence0392 extends ILeetCode {
    public boolean isSubsequence(String s, String t) {
        if(s.equals(t)) {
            return true;
        }

        HashMap<Character, Queue<Integer>> map = new HashMap<>();

        for (int i=0; i < t.length();i++) {
            if(!map.containsKey(t.charAt(i))) {
                map.put(t.charAt(i), new LinkedList<>());
            }

            map.get(t.charAt(i)).offer(i);
        }

        int prev = 0;
        for (int i=0; i < s.length();i++) {
            Character c = s.charAt(i);

            if(map.containsKey(c)) {
                if(map.get(c).isEmpty()) {
                    return false;
                }
                int positon = map.get(c).poll();
                while (positon < prev && !map.get(c).isEmpty()) {
                    positon = map.get(c).poll();
                }

                if(positon < prev) {
                    return false;
                }



                prev = positon;
            }
            else {
                return false;
            }
        }

        return true;

    }



    @Override
    public void run() {
        String s = "aaaaaa", t = "bbaaaa";
        int k = 2;

        boolean res = isSubsequence(s, t);

        print(res);
    }
}
