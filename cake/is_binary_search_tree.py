class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

def is_binary_search_tree(binary_tree: BinaryTreeNode):
    if not binary_tree:
        return True

    val = binary_tree.value
    left = binary_tree.left
    right = binary_tree.right

    if (not right or right.value < val) and (not left or left.value > val):
        return is_binary_search_tree(binary_tree.right) and is_binary_search_tree(binary_tree.left)
    else:
        return False




tree = BinaryTreeNode(50)
right = tree.insert_right(70)
right_right = right.insert_right(60)
right_right.insert_right(80)
result = is_binary_search_tree(tree)


print (is_binary_search_tree(tree))


def is_bst(root: BinaryTreeNode):
    node_and_bounds_stack = [(root, -float('inf'), float('inf'))]

    while len(node_and_bounds_stack):

        node, lower_bound, upper_bound = node_and_bounds_stack.pop()
        if (node.value <= lower_bound) or (node.value > upper_bound):
            return False

        if node.left:
            node_and_bounds_stack.append((node.left, lower_bound, node.value))

        if node.right:
            node_and_bounds_stack.append((node.right, node.value, upper_bound))
    return True

print(is_bst(tree))



