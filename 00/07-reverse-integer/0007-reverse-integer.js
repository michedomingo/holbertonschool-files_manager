/**
 * @param {number} x
 * @return {number}
 */
var reverse = function (num) {
  let sum = 0;

  // # 1b
  let getLastDigit = (num, mod) => {
    if (num < 0) {
      return num % -mod;
    }
    return num % mod;
  };

  let divide = (num, divider) => {
    return parseInt((num * 1.0) / divider); // # 2b
  };

  // # 1
  while (num) {
    let pop = getLastDigit(num, 10); // # 1a
    num = divide(num, 10); // # 2a

    sum = sum * 10 + pop; // # 3

    // # 4
    if (Math.abs(sum) > 2147483648) {
      return 0;
    }
  }
  return sum;
};

/* 
"""
1.  While num is valid
1a. Get last digit of num
1b. Modulo num by 10 or -10 to extract remainder
2a. Divide num by 10, to access next digit to extract remainder
2b. Prevent incorrect floor division by casting from float to int
3.  Reverse num with remainders shifting to front
4.  sum must be within contraints -2**31 <= x <= 2**31 - 1
note: from interview standpoint code sum check (MIN_INT <= sum <= MAX_INT) after calculation is incorrect???
"""
# Input: x = 123
# _______________________________________
# step#1b
#       123
# pop = num % 10
#  3
# _______________________________________
# step#2a
#           123         10
# num = int(num * 1.0 / divider)
#  12       12.3
# _______________________________________
# step#3    num: 12    pop: 3    sum: 0
#        0          3
# sum = sum * 10 + pop
#  3
# _______________________________________
# step#1b
#       12
# pop = num % 10
#  2
# _______________________________________
# step#2a
#           12          10
# num = int(num * 1.0 / divider)
#  1        1.2
# _______________________________________
# step#3    num: 1     pop: 2    sum: 3
#        3          2
# sum = sum * 10 + pop
#  32
# _______________________________________
# step#1b
#       1
# pop = num % 10
#  1
# _______________________________________
# step#2a
#           1           10
# num = int(num * 1.0 / divider)
#  0        0.1
# _______________________________________
# step#3    num: 0     pop: 1    sum: 32
#        32         1
# sum = sum * 10 + pop
# 321
# _______________________________________
# Output: 321
*/

console.log(`Output: ${reverse((num = -123))}`);
console.assert(reverse((num = 123)) === 321);
console.assert(reverse((num = -123)) === -321);
console.assert(reverse((num = 120)) === 21);
console.assert(reverse((num = 0)) === 0);
console.assert(reverse((num = 1534236469)) === 0);
console.assert(reverse((num = 8192)) === 2918);
