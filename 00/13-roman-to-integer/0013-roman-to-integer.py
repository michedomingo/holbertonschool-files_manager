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
        total = value.get(s[-1])                # 1

        for i in reversed(range(len(s) - 1)):   # 2

            if value[s[i]] < value[s[i + 1]]:   # 3a
                total -= value[s[i]]            # 3b
            else:                               # 4a
                total += value[s[i]]            # 4b

        return total


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
# total = value.get(s[-1])
#   5
# _______________________________________
# step#2
#                          7
# for i in reversed(range(len(s) - 1)):
#                               6
# _______________________________________
# step#3a        i: 5         total: 5
#            5               6
# if value[s[i]] < value[s[i + 1]]:
#          I             V
#          1     <       5   true
# step#3b
#           5              5
#         total -= value[s[i]]
#                        I
#                        1
# _______________________________________
# step#3a        i: 4         total: 4
#            4               5
# if value[s[i]] < value[s[i + 1]]:
#          C             I
#         100    <       1   false
# step#4b
#           4              4
#         total += value[s[i]]
#                        C
#                       100
# _______________________________________
# step#3a        i: 3         total: 104
#            3               4
# if value[s[i]] < value[s[i + 1]]:
#          X             C
#          10    <      100   true
# step#3b
#          104             3
#         total -= value[s[i]]
#                        X
#                        10
# _______________________________________
# step#3a        i: 2         total: 94
#            2               3
# if value[s[i]] < value[s[i + 1]]:
#          M             X
#         1000   <      10   false
# step#4b
#           94             2
#         total += value[s[i]]
#                        M
#                       1000
# _______________________________________
# step#3a        i: 1         total: 1094
#            1               2
# if value[s[i]] < value[s[i + 1]]:
#          C             M
#         100    <     1000   true
# step#3b
#          1094            1
#         total -= value[s[i]]
#                        C
#                       100
# _______________________________________
# step#3a        i: 0          total: 994
#            0               1
# if value[s[i]] < value[s[i + 1]]:
#          M             C
#        1000    <      100   false
# step#4b
#          994             0
#         total += value[s[i]]
#                        M
#                       1000
# _______________________________________
# Output: 1994

# assert(Solution().romanToInt(s="III") == 3)
# assert(Solution().romanToInt(s="IV") == 4)
# assert(Solution().romanToInt(s="IX") == 9)
# assert(Solution().romanToInt(s="LVIII") == 58)
# assert(Solution().romanToInt(s="MCMXCIV") == 1994)


def main():
    output = Solution().romanToInt(s="MCMXCIV")
    print(f"Output: {output}")


if __name__ == '__main__':
    main()
