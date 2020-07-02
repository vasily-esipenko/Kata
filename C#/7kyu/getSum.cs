// 7 kyu kata
// Beginner Series #3 Sum of Numbers
// Link: https://www.codewars.com/kata/55f2b110f61eb01779000053/csharp

// Description:

// Given two integers a and b, which can be positive or negative, find the sum of all the numbers between including them too and return it. If the two numbers are equal return a or b.
// Note: a and b are not ordered!
// Examples
// GetSum(1, 0) == 1   // 1 + 0 = 1
// GetSum(1, 2) == 3   // 1 + 2 = 3
// GetSum(0, 1) == 1   // 0 + 1 = 1
// GetSum(1, 1) == 1   // 1 Since both are same
// GetSum(-1, 0) == -1 // -1 + 0 = -1
// GetSum(-1, 2) == 2  // -1 + 0 + 1 + 2 = 2

//My solution:


using System;
public class Sum
{
    public int GetSum(int a, int b)
    {
       int res = 0;
       int min = Math.Min(a, b);
       int max = Math.Max(a, b);
       if (a == b) {
           return a;
       } else {
            for (int i = min; i < max; i++) {
                res += i;
            }
            return res + max;
       }
    }
}


// My profile on Codewars: https://www.codewars.com/users/vasilyesp
// My StackOverflow account: https://stackoverflow.com/users/13187161/vasily-esipenko
