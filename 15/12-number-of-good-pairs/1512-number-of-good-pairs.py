from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        nums, freq = sorted(nums), {}

        for item in nums:
            print("\n")
            print(f"if item in freq | if {item} in {freq}")
            if item in freq:

                print(f"freq[item] += 1 | {freq[item]} += 1")
                freq[item] += 1
            else:
                freq[item] = 1
                print(f"else... freq[item] = 1 | {freq[item]} = 1")

        print(freq)

        answer = 0
        for value in freq.values():
            if value != 0:
                answer += (value**2 - value)//2

        print(f"Final answer: {answer}")


def main():

    work = Solution()
    work.numIdenticalPairs(nums=[1, 2, 3, 1, 1, 3])


if __name__ == '__main__':
    main()
