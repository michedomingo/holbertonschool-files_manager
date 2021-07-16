value = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


class Solution:
    def romanToInt(self, s: str) -> int:
        total, i = 0, 0

        while i < len(s):
            # if at least 2 symbols remaining AND current index value is less than next index value
            # add the difference of the next 2 symbols and go forward 2 places
            if (i + 1 < len(s)) and (value[s[i]] < value[s[i + 1]]):
                total += (value[s[i + 1]] - value[s[i]])
                i += 2
            else:
                total += value[s[i]]
                i += 1
            # add current symbol and go forward 1 place
        return total


def main():
    output = Solution().romanToInt(s="MMCMLXXXIX")
    print(f"Output: {output}")


if __name__ == '__main__':
    main()
