class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" ->")
            current = current.next
        print("null")

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def insert_after(self, target_data, data):
        current = self.head  # Start at the head (first node of the list)

        # Search for the target node
        while current is not None:  # Keep going until the end of the list
            if current.data == target_data:  # Check if this is the target node
                break  # Stop the loop, target node is found
            current = current.next  # Move to the next node

        # If the target node is found
        if current is not None:  # Means target_data exists in the list
            new_node = Node(data)  # Create the new node
            new_node.next = current.next  # Point new node to the node after target
            current.next = new_node  # Update target node to point to new node
        else:
            print(f"Node with data {target_data} not found.")  # Handle if target doesn't exist

    def delete(self, data):
        if not self.head:  # If the list is empty
            print("List is empty.")
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        if current.next:  # If the node to be deleted is found
            current.next = current.next.next
        else:
            print(f"Node with data {data} not found.")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


linked_list = SinglyLinkedList()

# Insert at the beginning
linked_list.insert_at_beginning(30)
linked_list.insert_at_beginning(20)
linked_list.insert_at_beginning(10)

print("After inserting at the beginning:")
linked_list.traverse()

# Insert at the end
linked_list.insert_at_end(40)
print("After inserting at the end:")
linked_list.traverse()

# Insert after a specific node
linked_list.insert_after(20, 25)
print("After inserting 25 after 20:")
linked_list.traverse()
#
# # Delete a node
# linked_list.delete(20)
# print("After deleting 20:")
# linked_list.traverse()


linked_list.reverse()
print("Reversed List:")
linked_list.traverse()
