package com.xjjxmm.leetcode;

import com.alibaba.fastjson.JSONObject;
import com.xjjxmm.leetcode.entity.Node;
import com.xjjxmm.leetcode.entity.TreeNode;

import java.util.Deque;
import java.util.LinkedList;
import java.util.Queue;

public class PopulatingNextRightPointersinEachNode0116 extends ILeetCode {
    public Node connect(Node root) {
        Queue<Node> next = new LinkedList<Node>();
        Deque<Node> realatoin = new LinkedList<Node>();
        next.offer(root.left);
        next.offer(root.right);

        while (!next.isEmpty()) {
            next.poll();
            next.poll();
            next.poll();
            next.poll();
        }


        return root;
    }

    public void next(Node root, Node res) {
        if(root == null) {
            return;
        }
        //res.val = root.val;
        res.left = new Node(root.left.val);
        res.right = new Node(root.right.val);
        res.left.next = res.right;

        next(root.left, res.left);
        next(root.right, res.right);
       /* root.left.next = root.right;
        if(root.left.right != null) {
            root.left.right = root.right.left;
        }
        next(root.left);
        next(root.right);*/
    }

    @Override
    public void run() {
        Node treeNode1 = new Node(1,
                new Node(2, new Node(4), new Node(5),null),
                new Node(3,new Node(7), new Node(7),null),
                null
        );



        Node res = connect(treeNode1);
        print(JSONObject.toJSONString(res));

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
