package com.xjjxmm.leetcode;

import com.alibaba.fastjson.JSONObject;
import com.xjjxmm.leetcode.entity.ListNode;

public class MergeTwoSortedLists0021 extends ILeetCode {

    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {



         ListNode root = new ListNode();
        ListNode temp = root;
         while (l1 != null && l2 != null) {
             if(l1.val <= l2.val) {
                 temp.next = l1;


                 l1 = l1.next;
             }
             else  {
                 temp.next = l2;


                 l2 = l2.next;
             }

             temp = temp.next;
         }

         if(l1 != null) {
             temp.next = l1;
         }

        if(l2 != null) {
            temp.next = l2;
        }

        return root.next;
    }


    @Override
    public void run() {
        ListNode l1 = new ListNode(1,
                new ListNode(2,
                        new ListNode(4)
                )
        );

        ListNode l2 = new ListNode(1,
                new ListNode(3,
                        new ListNode(4)
                )
        );

        ListNode res = mergeTwoLists(l1, l2);
        print(JSONObject.toJSONString(res));

        //run1();
    }


    public void run1() {
        int[] nums = new int[]{0, 1, 0, 3, 12};

        //moveZeroes(nums);

        print(nums);
    }
}
