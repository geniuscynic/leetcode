using System;
using System.Collections.Generic;
using net.entity;

namespace net.leetcode
{
    public class Solution141 : ILeetcode
    {
       

        public bool HasCycle(ListNode head)
        {
             HashSet<ListNode> hashSet = new HashSet<ListNode>();

             while (head != null)
             {


                 if (!hashSet.Add(head))
                 {
                     return true;
                 }

                 head = head.next;
             }

             return false;
        }

        public bool HasCycle2(ListNode head)
        {
            if (head == null || head.next == null) return false;

            var fast = head.next;
            var slow = head;

            

            while (slow != fast)
            {
                if (fast == null || fast.next == null) return false;
                if (slow == null) return false;

                fast = fast.next.next;

                slow = slow.next;


            }

            return true;
        }

        public void Run()
        {
            var test1 = new ListNode(3);
            var test2 = new ListNode(2);
            var test3 = new ListNode(0);
            var test4 = new ListNode(-4);

            test1.next = test2;
            test2.next = test3;
            test3.next = test4;
            test4.next = test2;


            var result = HasCycle2(test1);

            Console.WriteLine(result);
        }
    }
}
