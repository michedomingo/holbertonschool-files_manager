
value = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900
}


class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        i = 0
        while i < len(s):
            # This is the subtractive case.
            if (i + 1 < len(s)) and s[i:i+2] in value:
                total += value[s[i:i+2]]
                i += 2
            else:
                total += value[s[i]]
                i += 1
        return total


def main():
    output = Solution().romanToInt(s="MMCMLXXXIX")
    print(f"Output: {output}")


if __name__ == '__main__':
    main()
