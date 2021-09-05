using System;

namespace net.leetcode
{
    public class Solution766 : ILeetcode
    {
        public bool IsToeplitzMatrix(int[][] matrix)
        {
            for (var i = 0; i < matrix.Length - 1; i++)
            {
                for (var j = 0; j < matrix[i].Length - 1; j++)
                {
                    if (matrix[i][j] != matrix[i + 1][j + 1])
                    {
                        return false;
                    }
                }
            }

            return true;
        }

        public void Run()
        {
            var test = new int[][] { new []{ 1, 2}, new []{2,2 }};

            var result = IsToeplitzMatrix(test);

            Console.WriteLine(result);
        }
    }
}
