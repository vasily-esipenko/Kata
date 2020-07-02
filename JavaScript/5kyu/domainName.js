// 5 kyu kata
// Extract the domain name from a URL
// Link: https://www.codewars.com/kata/514a024011ea4fb54200004b

// Description:

// Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:
// domain_name("http://github.com/carbonfive/raygun") == "github" 
// domain_name("http://www.zombie-bites.com") == "zombie-bites"
// domain_name("https://www.cnet.com") == "cnet"

//My solution:


function domainName(url) {
    let arr;
    if (/www/.test(url)) {
      arr = url.split('.');
      return arr[1];
    } else if (/http/.test(url)) {
      arr = url.split('//');
      arr = arr[1].split('.');
      return arr[0];
    } else {
      arr = url.split('.');
      return arr[0];
    }
}


// My profile on Codewars: https://www.codewars.com/users/vasilyesp
// My StackOverflow account: https://stackoverflow.com/users/13187161/vasily-esipenko
