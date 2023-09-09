#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        cnt_a = 1
        a = headA
        b = headB
        while headA.next:
            cnt_a += 1
            headA = headA.next

        cnt_b = 1            
        while headB.next:
            cnt_b += 1
            headB = headB.next
        
        if cnt_a > cnt_b:
            while cnt_a != cnt_b:
                a = a.next
                cnt_a -= 1

        elif cnt_a < cnt_b:
            while cnt_a != cnt_b:
                b = b.next
                cnt_b -= 1
        
        while a:
            if id(a) == id(b):
                return a
            if a.next:
                a = a.next
                b = b.next
            else:
                break
        return

        # node_set = set()
        # while headA:
        #     node_set.add(headA)
        #     if headA.next:
        #         headA = headA.next
        #     else:
        #         break
        
        # while headB:
        #     if headB in node_set:
        #         return headB
        #     if headB.next:
        #         headB = headB.next
        #     else:
        #         break
        # return

# @lc code=end

