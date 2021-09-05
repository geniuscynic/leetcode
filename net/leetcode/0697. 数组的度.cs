using System;
using System.Collections.Generic;

namespace net.leetcode
{
    public class Solution697  : ILeetcode
    {
       
        public int FindShortestSubArray(int[] nums)
        {
            var freqDict = new Dictionary<int, int>();
            var posDict = new Dictionary<int, int>();

            var maxFreq = 0;
            int shortLength = 0;
            for (var i = 0; i < nums.Length; i++)
            {
                if (freqDict.ContainsKey(nums[i]))
                {
                    freqDict[nums[i]]++;

                    if (freqDict[nums[i]] > maxFreq)
                    {
                        maxFreq = freqDict[nums[i]];

                        shortLength = i - posDict[nums[i]];
                    }
                    else if (freqDict[nums[i]] == maxFreq)
                    {
                        
                        var len = i - posDict[nums[i]];
                        if (shortLength > len)
                        {
                            shortLength = len;
                        }
                    }
                }
                else
                {
                    freqDict.Add(nums[i], 1);
                    posDict.Add(nums[i], i);
                }
            }

            return shortLength + 1;
        }

        public int FindShortestSubArray2(int[] nums)
        {
            var dict = new Dictionary<int, int[]>();
            

            var maxFreq = 0;
            int shortLength = 0;
            for (var i = 0; i < nums.Length; i++)
            {
                if (dict.ContainsKey(nums[i]))
                {
                    dict[nums[i]][0]++;

                    if (dict[nums[i]][0] > maxFreq)
                    {
                        maxFreq = dict[nums[i]][0];

                        shortLength = i - dict[nums[i]][1];
                    }
                    else if (dict[nums[i]][0] == maxFreq)
                    {

                        var len = i - dict[nums[i]][1];
                        if (shortLength > len)
                        {
                            shortLength = len;
                        }
                    }
                }
                else
                {
                    dict.Add(nums[i], new [] {1, i});
                    
                }
            }

            return shortLength + 1;
        }

        public void Run()
        {
            var test = new[] { 1, 2, 2, 3, 1, 4, 2 };
            var result = FindShortestSubArray(test) ;

            Console.WriteLine(result);
        }
    }
}
