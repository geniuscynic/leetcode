using System;
using System.Collections.Generic;
using net.entity;

namespace net.leetcode
{

    public class Solution3 : ILeetcode
    {
        public int LengthOfLongestSubstring(string s)
        {
            var dict = new Dictionary<char, int>();
            var p = 0;
            var q = 0;

            var maxLength = 0;
            while (q < s.Length)
            {
                var c = s[q];

                
                if (dict.ContainsKey(c))
                {
                    maxLength = Math.Max(q - p, maxLength);
                    p = Math.Max(dict[c] + 1, p);
                }

                dict[c] = q;


                q++;
            }

            return Math.Max(q - p, maxLength);
        }

        public void Run()
        {
            //var l1 = new ListNode(2, new ListNode(4, new ListNode(3)));
            //var l2 = new ListNode(5, new ListNode(6, new ListNode(4)));

            var result = LengthOfLongestSubstring("abba");

            Console.WriteLine(result);

        }
    }
}
