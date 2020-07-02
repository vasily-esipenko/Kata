// 8 kyu kata
// Find numbers which are divisible by given number
// Link: https://www.codewars.com/kata/55edaba99da3a9c84000003b

// Description:

// Complete the function which takes two arguments and returns all numbers which are divisible by the given divisor. 
// First argument is an array of numbers and the second is the divisor.

//My solution:


function divisibleBy(numbers, divisor){
    let result = numbers.filter(num => num % divisor == 0);
    return result;
}


// My profile on Codewars: https://www.codewars.com/users/vasilyesp
// My StackOverflow account: https://stackoverflow.com/users/13187161/vasily-esipenko
