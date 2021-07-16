value = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


class Solution:
    def romanToInt(self, s: str) -> int:
        total = value.get(s[-1])

        for i in reversed(range(len(s) - 1)):
            # check if symbol after (i+1) to determine whether current symbol should be 'added' or 'subtracted
            if value[s[i]] < value[s[i + 1]]:
                total -= value[s[i]]
            else:
                total += value[s[i]]
        return total


def main():
    output = Solution().romanToInt(s="MMMCXLIV")
    print(f"Output: {output}")


if __name__ == '__main__':
    main()
