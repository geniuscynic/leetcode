using System;
using System.Collections.Generic;
using net.entity;

namespace net.leetcode
{
    public class Solution1 : ILeetcode
    {

        public int[] TwoSum(int[] nums, int target)
        {
            var hashSet = new Dictionary<int,int>();
            for (var i = 0; i < nums.Length; i++)
            {
                var num = nums[i];

               
                var prev = target - num;
                if (hashSet.ContainsKey(prev) && hashSet[prev] != i)
                {
                    return new[] { hashSet[prev], i };
                }

                hashSet[num] = i;

            }

            return new int[2];
        }

        public int[] TwoSum2(int[] nums, int target)
        {
            var p = 0;
            var q = nums.Length - 1;
            while (p < q)
            {
                var result = target - nums[p];

                if (result == nums[q])
                {
                    return new[] {q, p};
                }
                else if (nums[q] < result)
                {
                    p++;
                }
                else
                {
                    q--;
                }

            }
           

            return new int[2];
        }

        public void Run()
        {
            var test1 = TwoSum(new [] {0,3,2,0}, 0);

            foreach (var result in test1)
            {
                Console.WriteLine(result);
            }
        }
    }
}
