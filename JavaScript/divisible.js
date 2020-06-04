// 8kyu kata
// Find numbers which are divisible by given number
// link: https://www.codewars.com/kata/55edaba99da3a9c84000003b

//Solution:

function divisibleBy(numbers, divisor){
    let result = numbers.filter(num => num % divisor == 0);
    return result;
}
