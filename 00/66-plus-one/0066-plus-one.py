from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        len_of_digits = len(digits)

        for index in range(len_of_digits):
            rightmost_index = len_of_digits - 1 - index   # 1

            if digits[rightmost_index] == 9:              # 2
                digits[rightmost_index] = 0
            else:                                         # 3
                digits[rightmost_index] += 1
                return digits                             # 4

        return [1] + digits                               # 5


"""
1. start from rightmost index
2. set 9s to 0s
3. increase rightmost not-9 by 1
4. return...
5. return, if all 9s (e.g. [9, 9] -> [1,0,0] )
"""
# Input: digits = [9,9]
#
# _______________________________________
# Output: [1,0,0]
#
# _______________________________________

assert(Solution().plusOne(digits=[9, 9, 9]) == [1, 0, 0, 0])
assert(Solution().plusOne(digits=[1, 7, 8, 9]) == [1, 7, 9, 0])
assert(Solution().plusOne(digits=[1, 2, 3]) == [1, 2, 4])
assert(Solution().plusOne(digits=[4, 3, 2, 1]) == [4, 3, 2, 2])


def main():

    Solution().plusOne(digits=[9, 9, 9])


if __name__ == '__main__':
    main()
