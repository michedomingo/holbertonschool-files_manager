/**
 * @param {string} s
 * @return {number}
 */
const value = {
  I: 1,
  V: 5,
  X: 10,
  L: 50,
  C: 100,
  D: 500,
  M: 1000,
};

var romanToInt = function (s) {
  let total = value[s.slice(-1)]; // # 1

  // # 2
  for (let i = s.length - 2; i >= 0; i--) {
    // # 3a
    if (value[s[i]] < value[s[i + 1]]) {
      total -= value[s[i]]; // # 3b
      // # 4a
    } else {
      total += value[s[i]]; // # 4b
    }
  }
  return total;
};

/* 
"""
1. Assign total the value of last item in s
2. Traverse s in reversed order, starting at 2nd to last item (length - 1)
3a. If left symbol value is less than right symbol value,
3b. Subtract lower value from total
4a. Else if, left symbol value is more than right symbol value,
4b. Add higher value to total
"""
# Input: s= "MCMXCIV"
#            0123456 index
# _______________________________________
# step#1
#                   V
# let total = value[s.slice(-1)];
#        5
# _______________________________________
# step#2
#                  7
# for (let i = s.length - 2; i >= 0; i--)
#          5  
# _______________________________________
# step#3a        i: 5         total: 5
#             5             6
# if (value[s[i]] < value[s[i + 1]])
#           I             V
#           1     <       5   true
# step#3b
#           5              5
#         total -= value[s[i]];
#                        I
#                        1
# _______________________________________
# step#3a        i: 4         total: 4
#             4             5
# if (value[s[i]] < value[s[i + 1]])
#           C             I
#          100    <       1   false
# step#4b
#           4              4
#         total += value[s[i]];
#                        C
#                       100
# _______________________________________
# step#3a        i: 3         total: 104
#           3               4
# if (value[s[i]] < value[s[i + 1]])
#           X             C
#           10    <      100   true
# step#3b
#          104             3
#         total -= value[s[i]];
#                        X
#                        10
# _______________________________________
# step#3a        i: 2         total: 94
#             2             3
# if (value[s[i]] < value[s[i + 1]])
#           M             X
#          1000   <      10   false
# step#4b
#           94             2
#         total += value[s[i]];
#                        M
#                       1000
# _______________________________________
# step#3a        i: 1         total: 1094
#             1             2
# if (value[s[i]] < value[s[i + 1]])
#           C             M
#          100    <     1000   true
# step#3b
#          1094            1
#         total -= value[s[i]];
#                        C
#                       100
# _______________________________________
# step#3a        i: 0          total: 994
#             0             1
# if (value[s[i]] < value[s[i + 1]])
#           M             C
#         1000    <      100   false
# step#4b
#          994             0
#         total += value[s[i]];
#                        M
#                       1000
# _______________________________________
# Output: 1994
 */

console.log(`Output: ${romanToInt((s = 'MCMXCIV'))}`);
console.assert(romanToInt((s = 'III')) === 3);
console.assert(romanToInt((s = 'IV')) === 4);
console.assert(romanToInt((s = 'IX')) === 9);
console.assert(romanToInt((s = 'LVIII')) === 58);
console.assert(romanToInt((s = 'MCMXCIV')) === 1994);
