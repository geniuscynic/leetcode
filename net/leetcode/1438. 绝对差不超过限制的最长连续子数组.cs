using System;

namespace net.leetcode
{
    public class Solution1438  : ILeetcode
    {

        public int LongestSubarray(int[] nums, int limit)
        {
            var left = 0;
            var right = 0;

            var minsIndex = 0;
            var maxsIndex = 0;
            var result = 0;

            while (right < nums.Length)
            {
                if (nums[minsIndex] >= nums[right])
                {
                    minsIndex = right;
                }
                else if (nums[maxsIndex] <= nums[right])
                {
                    maxsIndex = right;
                }

                //Console.WriteLine($"{mins}:{maxs}:{left}:{i}:{nums[i]}");
                if (nums[maxsIndex] - nums[minsIndex]  <= limit)
                {
                    result = Math.Max(right - left + 1, result);

                    right ++;
                }
                else if(nums[maxsIndex] == nums[right])
                {
                    minsIndex++;
                    left = minsIndex;

                    right = left;
                }
                else if (nums[minsIndex] == nums[right])
                {
                    maxsIndex++;

                    left = maxsIndex;
                    right = left;

                }
                else
                {
                    var a = nums[right];
                }

                if (result >= nums.Length - left)
                {
                    break;
                }

                Console.WriteLine($"{left}:{right}:{minsIndex}:{maxsIndex}:{result}");
            }

            return result;
        }
            //while (right < nums.Length)
            //{
            //    if (nums[mins] >= nums[right])
            //    {
            //        if (nums[maxs] - nums[right] <= limit)
            //        {
            //            result = Math.Max(right - left + 1, result);
            //            mins = right;
            //        }
            //        else
            //        {
            //            left++;
            //        }
            //    }
            //    else if (nums[maxs] <= nums[right])
            //    {

            //    }
            //    else
            //    {
            //        result = Math.Max(i - left + 1, result);
            //    }
            //}

            //for (var i = 1; i < nums.Length; i++)
            //{
            //    if (nums[mins] >= nums[i])
            //    {
            //        if (nums[maxs] - nums[i] <= limit)
            //        {
            //            result = Math.Max(i - left + 1, result);
            //            mins = i;
            //        }
            //        else
            //        {

            //        }
            //    }
            //    else if (nums[maxs] <= nums[i])
            //    {

            //    }
            //    else
            //    {
            //        result = Math.Max(i - left + 1, result);
            //    }

            //    mins = Math.Min(mins, nums[i]);
            //    maxs = Math.Max(maxs, nums[i]);

            //    Console.WriteLine($"{mins}:{maxs}:{left}:{i}:{nums[i]}");
            //    if (maxs - mins <= limit)
            //    {
            //        result = Math.Max(i - left + 1, result);
            //    }
            //    else if (nums[i] == maxs)
            //    {
            //        left += 1;

            //    }
            //    else
            //    {
            //        mins = nums[i];
            //        maxs = nums[i];
            //        left = i;

            //    }

            //    if (result >= nums.Length - left)
            //    {
            //        break;
            //    }
            //}



            //return result;

        //}

      
        public void Run()
        {
            var test = new[] { 7, 40, 10, 10, 40, 39, 96, 21, 54, 73, 33, 17, 2, 72, 5, 76, 28, 73, 59, 22, 100, 91, 80, 66, 5, 49, 26, 45, 13, 27, 74, 87, 56, 76, 25, 64, 14, 86, 50, 38, 65, 64, 3, 42, 79, 52, 37, 3, 21, 26, 42, 73, 18, 44, 55, 28, 35, 87 };
            var limit = 63;
            var result = LongestSubarray(test, limit) ;

            Console.WriteLine(result);
        }
    }
}
