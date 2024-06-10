class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def find_max_value(node):
    current = node
    while current.right is not None:
        current = current.right
    return current.value

# Приклад використання
root = TreeNode(20)
root.left = TreeNode(10)
root.right = TreeNode(30)
root.right.right = TreeNode(40)

print("Найбільше значення:", find_max_value(root))  # Найбільше значення: 40
