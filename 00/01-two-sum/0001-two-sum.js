/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  let map = {}; //# 1

  for (const [index, num] of nums.entries()) {
    //# 2
    if (num in map) {
      return [map[num], index]; //# 3
    } else {
      map[target - num] = index; //# 4
    }
  }
};

/* 
"""
complement = target - nums[index]

1. initialize map to store seen key(target's complement) and value(index of other complement)

2. get index of current iteration and num value/item at current iteration,
    by looping through iterable object nums with Array.prototype.entries()
    

3. if current num complement already exists in map, we found a solution,
    return the indices of the complement nums

4. add to map - complement key paired with value (index of other complement)

"""
# Input: nums=[2, 7, 11, 15], target=9
# _______________________________________
# step#4       index: 0       num: 2
#
#         [2, 7, 11, 15]      map = {}
#          ^
#      9 - 2 = 7 (complement)
# target - num
#
# map[complement] = index
#             map = {7:0}
# _______________________________________
# step#3       index: 1       num: 7
#
#       [2, 7, 11, 15]         map = {7:0}
#           ^
#       9 - 7 = 2 (complement)
#  target - num
#
# return [map[num], index]
#                ^  ^
# Ouput:        [0, 1]
# _______________________________________
*/

let assert = require('assert');
assert.deepStrictEqual(twoSum((nums = [2, 7, 11, 15]), (target = 9)), [0, 1]);
assert.deepStrictEqual(twoSum((nums = [3, 2, 4]), (target = 6)), [1, 2]);
assert.deepStrictEqual(twoSum((nums = [3, 3]), (target = 6)), [0, 1]);
