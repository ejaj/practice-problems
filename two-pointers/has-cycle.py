class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def has_cycle(head):
    if not head:
        return False

    slow = head
    fast = head.next

    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next

    return False


# Creating a linked list with a cycle for demonstration
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # Creating a cycle here

print("Does the linked list have a cycle? ", has_cycle(node1))
