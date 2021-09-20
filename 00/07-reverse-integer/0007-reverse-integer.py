class Solution:
    def reverse(self, num: int) -> int:
        MIN_INT = -2**31     # -2147483648
        MAX_INT = 2**31 - 1  # 2147483647
        sum = 0

        def get_last_digit(num, mod):         # 1b
            if num < 0:
                return num % -mod
            return num % mod

        def divide(num, divider):
            return int(num * 1.0 / divider)   # 2b

        while num:                            # 1
            pop = get_last_digit(num, 10)     # 1a
            num = divide(num, 10)             # 2a

            if (sum < divide(MIN_INT, 10)) or (sum == divide(MIN_INT, 10) and pop < -8):   # 3a
                return 0
            if (sum > divide(MAX_INT, 10)) or (sum == divide(MAX_INT, 10) and pop > 7):    # 3b
                return 0
            sum = sum * 10 + pop                                                           # 4

        return sum


"""
1.  While num is valid
1a. Get last digit of num
1b. Modulo num by 10 or -10 to extract remainder
2a. Divide num by 10, to access next digit to extract remainder
2b. Prevent incorrect floor division by casting from float to int
3.  sum must be within contraints -2**31 <= x <= 2**31 - 1 throughout calculation
3a. return 0, if sum < -214748364 OR sum == -214748364 & pop < -8 
3b. return 0, if sum > 214748364 OR sum == 214748364 & pop > 7
4.  Reverse num with remainders shifting to front
note: from interview standpoint code sum check (MIN_INT <= sum <= MAX_INT) after calculation is incorrect
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
# step#4    num: 12    pop: 3    sum: 0
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
# step#4    num: 1     pop: 2    sum: 3
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
# step#4    num: 0     pop: 1    sum: 32
#        32         1
# sum = sum * 10 + pop
# 321
# _______________________________________
# Output: 321

assert(Solution().reverse(x=123) == 321)
assert(Solution().reverse(x=-123) == -321)
assert(Solution().reverse(x=120) == 21)
assert(Solution().reverse(x=0) == 0)


def main():

    output = Solution().reverse(x=123)
    print(f"Output: {output}")


if __name__ == '__main__':
    main()
