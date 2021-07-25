class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack_length = len(haystack)
        needle_length = len(needle)

        if needle_length == 0:
            return 0                                                # 1
        elif haystack_length < needle_length:
            return -1                                               # 2
        else:
            for i in range((haystack_length - needle_length) + 1):  # 3a
                if haystack[i:i + needle_length] == needle:         # 3b
                    return i                                        # 3c
            return -1                                               # 4

# 1. given edge case, if needle is empty string, return 0
# 2. needle can't be found if haystack is smaller than needle, return -1

# 3a. traverse haystack until the 'needle_length'th last index
# 3b. check each consective substring of needle_length in haystack to match needle string
# 3c. return substring starting index (i)

# 4. return -1 if needle not found in haystack

#        needle : l l
# needle_length : 2
# iterator  (i) : 0 1 2
#      haystack : h e l l o
#        return :     2
# _______________________________________
# haystack[i:i + needle_length] == needle
# haystack[0:2] --> he
# haystack[1:3] --> el
# haystack[2:4] --> ll


assert(Solution().strStr(haystack="hello", needle="ll") == 2)
assert(Solution().strStr(haystack="aaaaa", needle="bba") == -1)
assert(Solution().strStr(haystack="", needle="") == 0)


def main():
    output = Solution().strStr(haystack="hello", needle="ll")
    print(f"Output: {output}")


if __name__ == '__main__':
    main()
