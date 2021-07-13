from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum, answer = 0, []

        for i in range(len(nums) - 1):
            sum = nums[i] + nums[i+1]
            if sum == target:
                answer.append(i)
                answer.append(i + 1)
                break

        return answer


def main():

    output = Solution().twoSum(nums=[3, 2, 3], target=6)
    print(f"Output: {output}")


if __name__ == '__main__':
    main()
