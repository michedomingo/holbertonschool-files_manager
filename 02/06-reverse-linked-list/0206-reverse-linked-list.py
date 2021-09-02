# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None            # 1

        while head:            # 2a
            temp = head        # 2b
            head = head.next   # 2c
            temp.next = prev   # 2d
            prev = temp        # 2e

        return prev            # 3


"""
1. since head does not have reference to its previous node, initialize prev node to none/null

2a. while head is present, this while loop executes
2b. initialize temp pointer to maintain reference of current head
2c. increment head to next element
2d. connect/reverse temp pointer direction from right to left/prev node
2e. update/assign prev node with old temp value (at start of iteration) before head incremented to next element

3. return new head reference called prev which is now start of list (value of 'head' is now none)
"""
# 2b.
#    None    1 -> 2 -> 3 -> 4 -> 5 -> None
#       ^    ^
#    prev   head
#           temp
# _______________________________________
# 2c.
#    None    1 -> 2 -> 3 -> 4 -> 5 -> None
#       ^    ^    ^
#    prev   temp  head
#
# _______________________________________
# 2d.
#    None <- 1    2 -> 3 -> 4 -> 5 -> None
#       ^    ^    ^
#    prev   temp  head
#
# _______________________________________
# 2e.
#    None <- 1    2 -> 3 -> 4 -> 5 -> None
#            ^    ^
#           temp  head
#           prev
# _______________________________________
# LAST ITERATION
#    None <- 1 <- 2 <- 3 <- 4 <- 5    None
#                                ^    ^
#                               temp  head
#                               prev


# AttributeError: 'list' object has no attribute 'next'
# assert(Solution().reverseList(head=[1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1])
# assert(Solution().reverseList(head=[1, 2]) == [2, 1])
# assert(Solution().reverseList(head=[]) == [])

# Accepted on Leetcode
# Run in terminal - AttributeError: 'list' object has no attribute 'val' - pending solution research
# def main():
#     output = Solution().reverseList(head=[1, 2, 3, 4, 5])
#     print(f"Output: {output}")


# if __name__ == '__main__':
#     main()
