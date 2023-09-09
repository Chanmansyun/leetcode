#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if not head:
        #     return head

        # cursor = head
        # cnt = 1
        # while cursor.next:
        #     cursor = cursor.next
        #     cnt += 1
        # cursor.next = head
        
        # result = cursor2 = ListNode(cursor.val)
        # for _ in range(cnt-1):
        #     for _ in range(cnt-1):
        #         cursor = cursor.next
        #     cursor2.next = ListNode(cursor.val)
        #     cursor2 = cursor2.next
        # cursor2.next = None
        # return result
        pre = None
        cursor = head
        while cursor:
            next = cursor.next
            cursor.next = pre
            pre = cursor
            cursor = next
        return pre
            
            
# @lc code=end

