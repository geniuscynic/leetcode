﻿using System;
using System.Collections.Generic;
using System.Text;

namespace net.entity
{
    //public class ListNode
    //{
    //    public int val;
    //    public ListNode next;

    //    public ListNode(int x)
    //    {
    //        val = x;
    //        next = null;
    //    }
    //}

    public class ListNode
    {
        public int val;
        public ListNode next;

        public ListNode(int val = 0, ListNode next = null)
        {
            this.val = val;
            this.next = next;
        }
    }
}
