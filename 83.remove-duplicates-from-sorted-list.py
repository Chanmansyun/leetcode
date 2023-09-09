#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if not head or not head.next:
        #     return head

        # start = cursor = ListNode()
        # while head.next:
        #     if head.val != head.next.val:
        #         cursor.next = head
        #         cursor = cursor.next
        #     head = head.next
        # if cursor.next:
        #     cursor.next.next = None
        # if not start.next:
        #     return head
        # return start.next
        if not head:
            return None
        
        cursor = head
        while cursor.next:
            if cursor.val == cursor.next.val:
                cursor.next = cursor.next.next
            else:
                cursor = cursor.next
        return head
            
# @lc code=end

