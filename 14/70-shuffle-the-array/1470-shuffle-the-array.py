from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        output = []
        slice1 = nums[:-n]
        slice2 = nums[-n:]

        for i in slice1:
            output.append(i)
            j = slice2.pop(0)
            output.append(j)

        # print(output)
        return output


def main():

    work = Solution()
    work.shuffle(nums=[1, 1, 2, 2], n=2)


if __name__ == '__main__':
    main()
