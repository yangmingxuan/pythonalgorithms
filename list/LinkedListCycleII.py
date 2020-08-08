from list import ListNode


class LinkedListCycleII:
    def detectCycle(self, head: ListNode) -> ListNode:
        visited = set()
        node = head
        while node is not None:
            if node in visited:
                return node
            else:
                visited.add(node)
                node = node.next

        return None

    def detectCycle2(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return None

        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        if slow != fast:
            return None

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow
