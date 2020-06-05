// 8kyu kata
// IQ Test
// Link: https://www.codewars.com/kata/552c028c030765286c00007d
// Description:
// Bob is preparing to pass IQ test. 
// The most frequent task in this test is to find out which one of the given numbers differs from the others. 
// Bob observed that one number usually differs from the others in evenness. 
// Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.
// ! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)


// My solution:


function iqTest(numbers){
    let nums = numbers.split(" ").map(x => x % 2);  
    let sum = nums.reduce((a,b) => a + b);  
    let target = sum > 1 ? 0 : 1;
  
    return nums.indexOf(target) + 1;
  }


// My profile on Codewars: https://www.codewars.com/users/vasilyesp
// My StackOverflow account: https://stackoverflow.com/users/13187161/vasily-esipenko
