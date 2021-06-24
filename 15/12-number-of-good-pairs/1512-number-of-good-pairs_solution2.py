from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        nums, memo = sorted(nums), {}

        for i in range(len(nums)-1):
            print("\n")
            print(f"*** ITERATION i = {i} ***")

            print(f"if {nums[i]} == {nums[i+1]}")
            if nums[i] == nums[i+1]:

                print(f"if {nums[i]} not in {memo}")
                if nums[i] not in memo:

                    print(f"memo BEFORE: {memo}")
                    memo[nums[i]] = 1
                    print(
                        f"AFTER memo[nums[i]] = 1 | memo is {memo} |  memo[nums[i]] is {memo[nums[i]]} | nums[i] is {nums[i]}")

                memo[nums[i]] = memo[nums[i]] + 1
                print(
                    f"Last line memo[nums[i]] = memo[nums[i]] + 1 | {memo[nums[i]]} = {memo[nums[i]]} + 1 | memo is {memo} |  memo[nums[i]] is {memo[nums[i]]} | nums[i] is {nums[i]}")

        answer = 0
        for n in memo.values():
            print("\n")
            print(f"*** ITERATION n = {n} ***")
            print(memo)
            print(f"memo values - {memo.values()}")
            print(
                f"Before answer += (n**2 - n)//2 | {answer} += ({n}**2 - {n})//2")
            answer += (n**2 - n)//2
            print(f"answer - {answer}")

        print(f"Final answer: {answer}")


def main():

    work = Solution()
    work.numIdenticalPairs(nums=[1, 1, 1, 1, 2, 2, 2, 3])


if __name__ == '__main__':
    main()
