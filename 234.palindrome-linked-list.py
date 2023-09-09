#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # result = []
        # while head.next:
        #     result.append(head.val)
        #     head = head.next
        # result.append(head.val)
        # for i, j in enumerate(result):
        #     if j != result[-i-1]:
        #         return False
        # return True
        
        two_step = one_step = head
        while two_step and two_step.next:
            one_step = one_step.next
            two_step = two_step.next.next
        pre_one = one_step
        one_step = one_step.next
        pre_one.next = None
        
        while one_step:
            temp = one_step
            one_step = one_step.next
            temp.next = pre_one
            pre_one = temp
            
            # one_step.next = pre_one
            # pre_one = one_step
            # one_step = one_step.next
        
        while pre_one:
            if pre_one.val != head.val:
                return False
            pre_one = pre_one.next
            head = head.next
        return True
            
# @lc code=end

