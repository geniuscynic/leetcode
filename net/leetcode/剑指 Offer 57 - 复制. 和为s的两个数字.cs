using System;
using System.Collections.Generic;
using net.entity;

namespace net.leetcode
{
    public class SolutionOffer57 : ILeetcode
    {

        public int[] TwoSum(int[] nums, int target)
        {
            var hashSet = new HashSet<int>();
            foreach (var num in nums)
            {
                if (num >= target)
                {
                    continue;
                }

                var prev = target - num;
                if (hashSet.Contains(prev))
                {
                    return new[] {prev, num};
                }

                hashSet.Add(num);

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
                    return new[] {nums[q], nums[p]};
                }
                else if (result > nums[q])
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
            var test1 = TwoSum2(new [] {2, 7, 11, 15 }, 9);

            foreach (var result in test1)
            {
                Console.WriteLine(result);
            }


           
        }
    }
}
