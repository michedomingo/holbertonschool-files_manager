from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = []
        total = 0

        for item in range(0, len(nums)):
            total += nums[item]
            output.append(total)

        return output


def main():

    work = Solution()
    work.runningSum([1, 2, 3, 4])


if __name__ == '__main__':
    main()
