from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        s1, s2 = min(strs), max(strs)
        i = 0
        while i < len(s1) and s1[i] == s2[i]:
            i += 1
        return s1[:i]


def main():
    output = Solution().longestCommonPrefix(strs=["flower"])
    print(f"Output: {output}")


if __name__ == '__main__':
    main()
