using System;
using System.Collections.Generic;
using System.Text;

namespace net.leetcode
{
    public class Solution1417 : ILeetcode
    {
        public string Reformat(string s)
        {
            var numberStack = new Queue<char>();
            var charStack = new Queue<char>();

            var result = new StringBuilder();

            
            foreach (var c in s)
            {
                if (char.IsNumber(c))
                {
                    numberStack.Enqueue(c);
                }
                else
                {
                    charStack.Enqueue(c);
                }
            }

            var i = charStack.Count - numberStack.Count;
            if (Math.Abs(i) > 1)
            {
                return "";
            }

            if (i == 0)
            {
                i = 1;
            }

            while (charStack.Count > 0 || numberStack.Count > 0)
            {
                if (i == 1 && charStack.Count > 0)
                {
                    result.Append(charStack.Dequeue());
                    i = -i;
                }
                else if (i == -1 && numberStack.Count > 0)
                {
                    result.Append(numberStack.Dequeue());
                    i = -i;
                }
            }

            return result.ToString();
        }

        public void Run()
        {
            var test = "ab123";
            var result = Reformat(test);

            Console.WriteLine(result);
        }
    }
}
