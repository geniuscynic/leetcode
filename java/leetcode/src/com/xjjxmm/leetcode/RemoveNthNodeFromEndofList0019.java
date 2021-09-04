package com.xjjxmm.leetcode;

import com.xjjxmm.leetcode.entity.ListNode;

import java.util.ArrayList;

public class RemoveNthNodeFromEndofList0019 extends ILeetCode {

    public ListNode removeNthFromEnd(ListNode head, int n) {
        ArrayList<ListNode> nodes = new ArrayList<ListNode>();

        while (head != null) {
            nodes.add(head);

            head = head.next;
        }



        int delIndex = nodes.size() - n;
        nodes.add(null);

        if(delIndex == 0 ) {

                return nodes.get(1);

        }

        nodes.get(delIndex - 1).next = nodes.get(delIndex + 1);

        return nodes.get(0);
    }

    @Override
    public void run() {
        ListNode head = new ListNode(1, null
//                new ListNode(2,
//                        new ListNode(3,
//                                new ListNode(4,
//                                        new ListNode(5)
//                                )
//                        )
//                )
        );

        ListNode res = removeNthFromEnd(head,1);
        print(res.val);

        //run1();
    }


    public void run1() {
        int[] nums = new int[]{0, 1, 0, 3, 12};

        //moveZeroes(nums);

        print(nums);
    }
}
