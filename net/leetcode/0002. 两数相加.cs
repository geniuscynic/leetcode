using System;
using System.Collections.Generic;
using net.entity;

namespace net.leetcode
{
    
    public class Solution2 : ILeetcode
    {
        public ListNode AddTwoNumbers(ListNode l1, ListNode l2)
        {

             var result = new ListNode();

             var temp = result;

             var flag = 0;
            while (l1 != null || l2 != null )
            {
                //var next = new ListNode(flag);

                if (l1 != null)
                {
                    result.val += l1.val;
                    l1 = l1.next;
                }

                if (l2 != null)
                {
                    result.val += l2.val;
                    l2 = l2.next;
                }

                flag = result.val / 10;
                result.val = result.val % 10;

                if (l1 != null || l2 != null || flag > 0)
                {
                    result.next = new ListNode(flag);

                    result = result.next;
                }

            }

            //if (flag > 0)
            //{
            //    result.next = new ListNode(flag);
            //}

            return temp;
        }

        public void Run()
        {
            var l1 = new ListNode(2, new ListNode(4, new ListNode(3)));
            var l2 = new ListNode(5, new ListNode(6, new ListNode(4)));

            var result = AddTwoNumbers(l1, l2);
            while (result != null)
            {
                
                    Console.WriteLine(result.val);

                    result = result.next;

            }
        }
    }
}
