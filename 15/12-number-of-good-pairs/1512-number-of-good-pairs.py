from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        nums, freq = sorted(nums), {}

        for item in nums:
            if item in freq:
                freq[item] += 1
            else:
                freq[item] = 1

        goodPairs = 0
        for value in freq.values():
            if value != 0:
                goodPairs += (value**2 - value)//2

        # print(goodPairs)
        return goodPairs


def main():

    work = Solution()
    work.numIdenticalPairs(nums=[1, 2, 3, 1, 1, 3])


if __name__ == '__main__':
    main()
