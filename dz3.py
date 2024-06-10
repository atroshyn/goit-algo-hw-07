def sum_of_values(node):
    if node is None:
        return 0
    return node.value + sum_of_values(node.left) + sum_of_values(node.right)

# Приклад використання
root = TreeNode(20)
root.left = TreeNode(10)
root.right = TreeNode(30)
root.left.left = TreeNode(5)
root.right.right = TreeNode(40)

print("Сума всіх значень:", sum_of_values(root))  # Сума всіх значень: 105
