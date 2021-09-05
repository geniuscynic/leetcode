package com.xjjxmm.leetcode;

import com.alibaba.fastjson.JSONObject;
import com.xjjxmm.leetcode.entity.ListNode;

import java.util.Deque;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class ReverseLinkedList0206 extends ILeetCode {

    public ListNode reverseList(ListNode head) {
        ListNode root = new ListNode();
        ListNode temp = root;

        Stack<ListNode> nodes = new Stack<ListNode>();
        while (head != null) {
            nodes.add(new ListNode(head.val));
            head = head.next;
        }

        while (!nodes.isEmpty()) {
            temp.next = nodes.pop();
            temp = temp.next;
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

        ListNode res = reverseList(l1);
        print(JSONObject.toJSONString(res));

        //run1();
    }


    public void run1() {
        int[] nums = new int[]{0, 1, 0, 3, 12};

        //moveZeroes(nums);

        print(nums);
    }
}
