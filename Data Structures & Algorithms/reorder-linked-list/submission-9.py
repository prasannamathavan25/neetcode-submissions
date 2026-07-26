# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next:
            return

        slow , fast = head , head 

        while fast.next and fast.next.next : 
            slow = slow.next 
            fast = fast.next.next 
        
        second = slow.next
        slow.next = None 

        prev = None 
        cur = second 
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp 
        head2 = prev 

        p1 = head 
        p2 = head2 

        while p1 and p2 : 
            temp1 = p1.next
            temp2 = p2.next
            p1.next = p2
            p2.next = temp1

            p1 = temp1
            p2 = temp2
        

       