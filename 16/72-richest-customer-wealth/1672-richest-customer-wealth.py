from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        result = list(map(sum, accounts))
        return max(result)


def main():

    work = Solution()
    work.maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]])


if __name__ == '__main__':
    main()
