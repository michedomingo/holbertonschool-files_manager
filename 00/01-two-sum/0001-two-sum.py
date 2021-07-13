from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for index, num in enumerate(nums):
            # value = target - num
            # if value in map and map[value] != index:
            #     return [map[value], index]
            if num in map:
                return [map[num], index]
            else:
                map[target-num] = index


def main():

    output = Solution().twoSum(nums=[3, 2, 3], target=6)
    print(f"Output: {output}")


if __name__ == '__main__':
    main()
