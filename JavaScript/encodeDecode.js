// 6kyu kata
// The Vowel Code
// link: https://www.codewars.com/kata/53697be005f803751e0015aa
// Description:
// Step 1: Create a function called encode() to replace all the lowercase vowels in a given string with numbers according to the following pattern:
// a -> 1
// e -> 2
// i -> 3
// o -> 4
// u -> 5
// For example, encode("hello") would return "h2ll4". There is no need to worry about uppercase vowels in this kata.
// Step 2: Now create a function called decode() to turn the numbers back into vowels according to the same pattern shown above.
// For example, decode("h3 th2r2") would return "hi there".
// For the sake of simplicity, you can assume that any numbers passed into the function will correspond to vowels.


// My solution:


function encode(string) {
    string = string.split("");
    let new_string = string.map(letter => {
        switch(letter) {
            case "a":
              return letter = "1";
            case "e":
              return letter = "2";
            case "i":
              return letter = "3";
            case "o":
              return letter = "4";
            case "u":
              return letter = "5";
            default:
                return letter;
        }
})
    return new_string.join("");
}


function decode(string) {
    string = string.split("");
    let dec_string = string.map(letter => {
        switch(letter) {
            case "1":
              return letter = "a";
            case "2":
              return letter = "e";
            case "3":
              return letter = "i";
            case "4":
              return letter = "o";
            case "5":
              return letter = "u";
            default:
                return letter;
        }
})
    return dec_string.join("");
}


// My profile on Codewars: https://www.codewars.com/users/vasilyesp
// My StackOverflow account: https://stackoverflow.com/users/13187161/vasily-esipenko
