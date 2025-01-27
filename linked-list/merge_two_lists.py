# Definition for a singly linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Create a dummy node to act as the start of the merged list
        dummy = ListNode(-1)
        tail = dummy  # Tail points to the last node in the merged list

        # Merge the two lists
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1  # Attach l1's node to the merged list
                l1 = l1.next  # Move l1 to its next node
            else:
                tail.next = l2  # Attach l2's node to the merged list
                l2 = l2.next  # Move l2 to its next node
            tail = tail.next  # Move the tail to the new last node

        # Attach any remaining nodes from l1 or l2
        tail.next = l1 if l1 else l2

        # Return the merged list (skip the dummy node)
        return dummy.next


# Function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# Function to print a linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" → ")
        current = current.next
    print("null")


# Example Usage:
# Input lists
l1 = create_linked_list([1, 3, 5])
l2 = create_linked_list([2, 4, 6])

# Print input lists
print("List 1:")
print_linked_list(l1)
print("List 2:")
print_linked_list(l2)

# Merge the lists
solution = Solution()
merged_list = solution.mergeTwoLists(l1, l2)

# Print the merged list
print("Merged List:")
print_linked_list(merged_list)
