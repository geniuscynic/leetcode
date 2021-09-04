package com.xjjxmm.leetcode;

import com.xjjxmm.leetcode.entity.ListNode;

public class MiddleoftheLinkedList0876 extends ILeetCode {

    public ListNode middleNode(ListNode head) {
        int i =0;

        ListNode temp1 = head;
        ListNode temp2 = head;

        while (temp2 != null && temp2.next != null) {
           temp1 = temp1.next;

           temp2 = temp2.next;

           if(temp2!= null) {
               temp2 = temp2.next;
           }


        }


        return temp1;
    }

    public ListNode middleNode2(ListNode head) {
        int i =0;

        ListNode temp = head;
        while (temp.next != null) {
            i++;

            temp = temp.next;
        }

        temp = head;
        int half = (i + 1) / 2;
        while (temp.next != null && half > 0) {
            half--;

            temp = temp.next;
        }

        return temp;
    }


    @Override
    public void run() {
        ListNode head = new ListNode(1,
                new ListNode(2,
                        new ListNode(3,
                                new ListNode(4,
                                        new ListNode(5)
                                )
                        )
                )
        );

        ListNode res = middleNode(head);
        print(res.val);

        //run1();
    }


    public void run1() {
        int[] nums = new int[]{0, 1, 0, 3, 12};

        //moveZeroes(nums);

        print(nums);
    }
}
