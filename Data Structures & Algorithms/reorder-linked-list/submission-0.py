# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
    def middle(self, head:Optional[ListNode]) -> Optional[ListNode]:
        f = head
        s = head
        while f and f.next:
            s = s.next
            f = f.next.next
        return s

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        mid = self.middle(head)
        hs = self.reverse(mid.next)
        mid.next = None
        hf = head

        while hs:
            temp1 = hf.next
            temp2 = hs.next
            hf.next = hs
            

            hs.next = temp1
            hf = temp1
            hs = temp2
        