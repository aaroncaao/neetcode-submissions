# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, trailing = head, None

        while curr:
            nxt = curr.next
            curr.next = trailing
            trailing = curr
            curr = nxt
        return trailing