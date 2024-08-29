class TreeNode:
    """- Implement:
    - [x] [insert    // insert value into tree](https://leetcode.com/problems/insert-into-a-binary-search-tree/submissions/987660183/)
    - [x] get_node_count // get count of values stored
    - [x] print_values // prints the values in the tree, from min to max
    - [x] delete_tree
    - [x] is_in_tree // returns true if a given value exists in the tree
    - [x] [get_height // returns the height in nodes (single node's height is 1)](https://www.geeksforgeeks.org/find-the-maximum-depth-or-height-of-a-tree/)
    - [x] get_min   // returns the minimum value stored in the tree
    - [x] get_max   // returns the maximum value stored in the tree
    - [x] [is_binary_search_tree](https://leetcode.com/problems/validate-binary-search-tree/)
    - [x] delete_value
    - [x] get_successor // returns the next-highest value in the tree after given value, -1 if none
    """

    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    if not root:
        return TreeNode(value)
    else:
        if root.value > value:
            if not root.left:
                root.left = TreeNode(value)
            else:
                insert(root.left, value)
        else:
            if not root.right:
                root.right = TreeNode(value)
            else:
                insert(root.right, value)


def print_values(root):
    if not root:
        return
    if root.left:
        print_values(root.left)
    print(root.value)
    if root.right:
        print_values(root.right)


def is_in_tree(root, value):
    if not root:
        return False
    if root.value == value:
        return True
    is_in_left_tree = (
        is_in_tree(root.left, value) if root.value > value and root.left else False
    )
    is_in_right_tree = (
        is_in_tree(root.right, value) if root.value < value and root.right else False
    )
    return is_in_left_tree or is_in_right_tree


def get_height(root):
    if not root:
        return 0
    return _get_height_helper(root, 0)


def _get_height_helper(root, cur_depth):
    if not root.left and not root.right:
        return cur_depth
    left_depth = (
        _get_height_helper(root.left, cur_depth + 1) if root.left else cur_depth
    )
    right_depth = (
        _get_height_helper(root.right, cur_depth + 1) if root.right else cur_depth
    )
    return max(left_depth, right_depth)


def get_min(root):
    if not root.left:
        return root.value
    return get_min(root.left)


def get_max(root):
    if not root.right:
        return root.value
    return get_max(root.right)


def is_bst(root):
    if not root:
        return False
    if (root.left and root.value < root.left.value) or (
        root.right and root.value > root.right.value
    ):
        return False
    is_left_bst = is_bst(root.left) if root.left else True
    is_right_bst = is_bst(root.right) if root.right else True
    return is_left_bst and is_right_bst


def delete_value(root, value):
    if not root:
        return None

    if root.value > value:
        root.left = delete_value(root.left, value)
    elif root.value < value:
        root.right = delete_value(root.right, value)
    else:
        if not root.left and not root.right:
            return None
        elif not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            min_val = get_min(root.right)
            root.value = min_val
            root.right = delete_value(root.right, min_val)
    return root


def get_successor(root, value):
    if not root:
        return None
    if root.value < value:
        return get_successor(root.right, value)
    elif root.value > value:
        return get_successor(root.left, value)
    else:
        if not root.right:
            return None
        next_node = root.right
        while next_node.left:
            next_node = next_node.left
        return next_node.value


if __name__ == "__main__":
    root = TreeNode(2)
    insert(root, 1)
    insert(root, 3)
    print_values(root)
    assert is_in_tree(root, 3)
    assert get_height(root) == 1
    print("---")
    insert(root, 4)
    insert(root, 6)
    insert(root, 5)
    insert(root, 10)
    insert(root, 8)
    print_values(root)
    assert get_height(root) == 5
    assert get_min(root) == 1
    print("---")
    insert(root, 0)
    insert(root, -4)
    insert(root, -3)
    insert(root, -5)
    print_values(root)
    assert get_min(root) == -5
    assert is_bst(root)
    print("---")
    delete_value(root, 10)
    print_values(root)
    assert get_successor(root, 6) == 8
