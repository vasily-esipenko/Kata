// 8 kyu kata
// Reversed Strings
// Link: https://www.codewars.com/kata/5168bb5dfe9a00b126000018/csharp

// Description:

// Complete the solution so that it reverses the string passed into it.
// 'world'  =>  'dlrow'

//My solution:


using System;

public static class Kata
{
  public static string Solution(string str) 
  {
    return Reverse(str);
  }
  
  public static string Reverse(string text)
        {
            char[] cArray = text.ToCharArray();
            string reverse = string.Empty;
            for (int i = cArray.Length - 1; i > -1; i--)
            {
                reverse += cArray[i];
            }
            return reverse;
        }
}


// My profile on Codewars: https://www.codewars.com/users/vasilyesp
// My StackOverflow account: https://stackoverflow.com/users/13187161/vasily-esipenko
