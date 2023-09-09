#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        add_one = 0
        result = cursor = ListNode()
        while l1 or l2:
            sum =  (l1.val if l1 else 0) + (l2.val if l2 else 0) + add_one
            cursor.val = sum % 10
            add_one = sum // 10
            if l1: l1 = l1.next
            if l2: l2 = l2.next

            if l1 or l2:
                cursor.next = ListNode()
                cursor = cursor.next
            elif not l1 and not l2 and add_one != 0:
                cursor.next = ListNode()
                cursor = cursor.next
                cursor.val = add_one
        return result
            
# @lc code=end

