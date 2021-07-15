class Solution:
    def reverse(self, num: int) -> int:
        MIN_INT = -2**31     # -2147483648
        MAX_INT = 2**31 - 1  # 2147483647
        sum = 0

        def get_last_digit(num, mod):
            if num < 0:
                return num % -mod
            return num % mod

        def divide(num, divider):
            return int(num * 1.0 / divider)  # prevent incorrect floor division

        while num:
            pop = get_last_digit(num, 10)
            num = divide(num, 10)

            # sum must be within constraints -2**31 <= x <= 2**31 - 1 throughout calculation
            if (sum < divide(MIN_INT, 10)) or (sum == divide(MIN_INT, 10) and pop < -8):
                return 0
            if (sum > divide(MAX_INT, 10)) or (sum == divide(MAX_INT, 10) and pop > 7):
                return 0
            sum = sum * 10 + pop
            # from interview standpoint code sum check (MIN_INT <= sum <= MAX_INT) after calculation is incorrect

        return sum


def main():

    output = Solution().reverse(num=1534236469)
    print(f"Output: {output}")


if __name__ == '__main__':
    main()
