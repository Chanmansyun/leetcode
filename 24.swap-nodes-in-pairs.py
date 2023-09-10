#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        pre = head
        result = head = head.next
        while head:
            temp = head.next
            pre.next = temp.next if temp else None
            head.next = pre
            head = head.next.next if head.next else None
            if temp and not head:
                head_cp = pre
            pre = temp
        
        if temp and not head:
            head_cp.next = pre
        
        return result
# @lc code=end

