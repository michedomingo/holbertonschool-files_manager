from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_length = len(nums)
        if nums_length <= 1:
            return nums_length         # 1

        i = 0                          # 2

        for j in range(1, nums_length):  # 3
            if nums[j] != nums[i]:     # 4a
                i += 1                 # 4b
                nums[i] = nums[j]      # 4c

        return i + 1                   # 5

# 1. if the list is empty or contains only one element, return 0 or 1 unique value(s) can be found
# 2. set 'slow-runner' pointer (i) to track index of last unique value found
# 3. set 'fast-runner' pointer (j) starting from index '1', finds unique values by skipping duplicate values, traverse until last index of list compared

# 4a. if new unique value found / ith & jth value are not the same
# 4b. move 'i' to the next index
# 4c. replace the current ith value with the newly found unique (jth) value

# 5. return 'i+1' number of unique values found

# index to overwrite on (i):  0
#                      nums: [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# iterator              (j):     1
# _________________________________________________________
#                       (i):              4
# final list           nums: [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]
#                       (j):                             8
# return i + 1      (4 + 1):              5


assert(Solution().removeDuplicates(nums=[1, 1, 2]) == 2)
assert(Solution().removeDuplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5)


def main():
    output = Solution().removeDuplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
    print(f"Output: {output}")


if __name__ == '__main__':
    main()
