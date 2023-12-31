class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def postOrder(root):
    if root:
        # Recursively travese the left subtree
        postOrder(root.left)
        # Recursively travese the right subtree
        postOrder(root.right)
        # Print the current node's data
        print(root.data, end=" ")
root = Node(1)
root.right = Node(2)
root.right.right = Node(5)
root.right.right.left = Node(3)
root.right.right.right = None(6)
root.right.right.left.right = Node(4)
# Calling postOrder function to print the postorder traversal
print("Postorder the Traversal:", end=" ")
postOrder(root)