from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s)-1                   # 1
        while left < right:                         # 2
            s[left], s[right] = s[right], s[left]   # 3
            left += 1                               # 4
            right -= 1                              # 5

        print(s)


"""
1.
2.
3.
4.
5
"""
# Example 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]


def main():

    Solution().reverseString(s=["h", "e", "l", "l", "o"])


if __name__ == '__main__':
    main()
