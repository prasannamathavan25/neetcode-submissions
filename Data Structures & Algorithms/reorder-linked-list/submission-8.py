# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # Count the number of nodes
        n = 0
        p = head

        while p:
            p = p.next
            n += 1

        # Find the split position
        if n % 2 == 0:
            k = n // 2
        else:
            k = (n // 2) + 1

        # Move to the middle node
        p = head
        cnt = 1

        while cnt < k:
            p = p.next
            cnt += 1

        # Split into two lists
        list2_head = p.next
        p.next = None

        # ----------------------------
        # Reverse the second half
        # ----------------------------
        prev, cur = None, list2_head

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        list2_head = prev      # BUG FIX: prev is the new head after reversal

        # ----------------------------
        # Merge the two halves
        # ----------------------------
        p1, p2 = head, list2_head

        while p1 and p2:

            temp1 = p1.next     # BUG FIX: Save next node of first list
            temp2 = p2.next     # BUG FIX: Save next node of second list

            p1.next = p2
            p2.next = temp1     # BUG FIX: Connect second list back to first

            p1 = temp1          # BUG FIX: Move first pointer using saved node
            p2 = temp2          # BUG FIX: Move second pointer using saved node

    