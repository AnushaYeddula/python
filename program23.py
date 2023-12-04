class singlyLinkedListNode:
    def __init__(self, data):
        self.data =data
        self.next = None
def deleteNode(llist, position):
    if position == 0:
        # If delecting the head node,update the head to the nextnode
        llist = llist.next
    else:
        current = llist
        for _ in range(position - 1):
            # Traverse to the node before the one to be delected
            current = current.next
        # Skip the node to be delected
        current.next = current.next.next
    return llist
def printLinkedList(llist):
    current = llist
    while current is not None:
        print(current.data)
        current = current.next
# Example usage
n = 8
elements = [20, 6, 2, 19, 7, 4, 15, 9]
position_to_delete = 3
# Create a linked list
head = singlyLinkedListNode(elements[0])
current = head
for data in elements[1:]:
    current.next = singlyLinkedListNode(data)
    current = current.next
# Print the original linked list0
printLinkedList(head)
# Delect the node at the given position
head = deleteNode(head, position_to_delete)
# Print the modified linked list
print("\nLinked List after delection:")
printLinkedList(head)
