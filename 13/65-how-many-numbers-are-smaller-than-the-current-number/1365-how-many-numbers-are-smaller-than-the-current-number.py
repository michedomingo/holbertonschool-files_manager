from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedNums = sorted(nums)
        output = []

        for num in nums:
            output.append(sortedNums.index(num))

        # print(output)
        return output


def main():

    work = Solution()
    work.smallerNumbersThanCurrent(nums=[8, 1, 2, 2, 3])


if __name__ == '__main__':
    main()
