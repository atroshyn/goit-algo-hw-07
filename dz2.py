def find_min_value(node):
    current = node
    while current.left is not None:
        current = current.left
    return current.value

# Приклад використання
root = TreeNode(20)
root.left = TreeNode(10)
root.right = TreeNode(30)
root.left.left = TreeNode(5)

print("Найменше значення:", find_min_value(root))  # Найменше значення: 5
