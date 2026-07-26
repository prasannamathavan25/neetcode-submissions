class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)          # Dummy handles head deletion
        stack = []

        curr = dummy

        while curr:
            stack.append(curr)             # Store every node
            curr = curr.next

        for _ in range(n):
            stack.pop()                    # Remove last n nodes

        prev = stack[-1]                   # Node before target
        prev.next = prev.next.next         # Skip target node

        return dummy.next