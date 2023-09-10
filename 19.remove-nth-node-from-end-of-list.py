#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return 
        
        result = cursor = head
        length = 0
        while head:
            head = head.next
            if length >= n+1:
                cursor = cursor.next
            length += 1
        if length == n:
            result = result.next
        else:
            cursor.next = cursor.next.next
        return result
# @lc code=end

# 