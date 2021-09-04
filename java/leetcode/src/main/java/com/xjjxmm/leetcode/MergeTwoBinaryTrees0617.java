package com.xjjxmm.leetcode;

import com.alibaba.fastjson.JSONObject;
import com.xjjxmm.leetcode.entity.TreeNode;

import java.util.LinkedList;
import java.util.Queue;

public class MergeTwoBinaryTrees0617 extends ILeetCode {
    public TreeNode mergeTrees(TreeNode root1, TreeNode root2) {
        if(root2 == null && root1 == null) {
            return null;
        }
        if(root1 == null) {
            return root2;
        }

        if(root2 == null) {
            return root1;
        }

        TreeNode res = new TreeNode();
        res.val = root1.val + root2.val;

        res.left = mergeTrees(root1.left, root2.left);
        res.right = mergeTrees(root1.right, root2.right);

        return  res;
    }





    @Override
    public void run() {
 TreeNode treeNode1 = new TreeNode(1,
         new TreeNode(3, new TreeNode(5), null),
         new TreeNode(2)
 );

        TreeNode treeNode2 = new TreeNode(2,
                new TreeNode(1, null, new TreeNode(4)),
                new TreeNode(3, null, new TreeNode(7))
        );

        TreeNode res = mergeTrees(treeNode1, treeNode2);
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
