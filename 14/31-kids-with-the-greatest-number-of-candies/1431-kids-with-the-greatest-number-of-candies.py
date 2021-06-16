from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output = []

        for i in candies:
            num = i + extraCandies
            if num >= max(candies):
                output.append(True)
            else:
                output.append(False)

        # print(output)
        return output


def main():

    work = Solution()
    work.kidsWithCandies(ccandies=[2, 3, 5, 1, 3], extraCandies=3)


if __name__ == '__main__':
    main()
