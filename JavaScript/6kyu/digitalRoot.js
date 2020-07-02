// 6 kyu kata
// Sum of Digits / Digital Root
// Link: https://www.codewars.com/kata/541c8630095125aba6000c00

// Description:

// Digital root is the recursive sum of all the digits in a number.
// Given n, take the sum of the digits of n. 
// If that value has more than one digit, continue reducing in this way until a single-digit number is produced. 
// This is only applicable to the natural numbers.

// My solution:


function digital_root(n) {
    return (n - 1) % 9 + 1;
  }


// My profile on Codewars: https://www.codewars.com/users/vasilyesp
// My StackOverflow account: https://stackoverflow.com/users/13187161/vasily-esipenko
