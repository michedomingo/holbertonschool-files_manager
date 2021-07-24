# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = ListNode(-1)  # 1
        prev = prehead  # 2

        while l1 and l2:  # 3
            if l1.val <= l2.val:  # 4a
                prev.next = l1  # 4b
                l1 = l1.next  # 4c
            else:  # 5a
                prev.next = l2  # 5b
                l2 = l2.next  # 5c
            prev = prev.next  # 6

        prev.next = l1 if l1 is not None else l2  # 7
        return prehead.next  # 8


# 1. set up false 'prehead' node to maintain unchanging reference to node ahead of the return node, allows to easily return head of merged list later
# 2. maintain prev pointer, points to current node considering adjusting its next pointer
# 3. iterate through both lists, as long as both lists have at least one node / until at least one of l1 or l2 points to null

# 4a. if value at l1 is less than or equal to value at l2
# 4b. connect previous node to l1
# 4c. increment l1

# 5a. if value at l2 is less than value at l1
# 5b. connect previous node to l2
# 5c. increment l2

# 6. regardless of which list connected, increment prev to keep it one step behind one of the list heads

# 7. connect non-null list (either l1 or l2 still have nodes) to end of the merged list
# 8. return head of merged list


# Accepted on Leetcode
# Run in terminal - AttributeError: 'list' object has no attribute 'val' - pending solution research
# def main():
#     output = Solution().mergeTwoLists(l1=[1, 2, 4], l2=[1, 3, 4])
#     print(f"Output: {output}")


# if __name__ == '__main__':
#     main()
