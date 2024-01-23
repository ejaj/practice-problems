class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


# Creating a simple linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

middle_node = find_middle(head)
print("The middle of the linked list is: ", middle_node.value)
