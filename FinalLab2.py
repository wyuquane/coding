class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def get_height(root):
    if root is None:
        return 0
    return root.height

def get_balance(root):
    if root is None:
        return 0
    return get_height(root.left) - get_height(root.right)

def right_rotate(root):
    left_child = root.left

    root.left = left_child.right
    root.height = 1 + max(get_height(root.left), get_height(root.right))

    left_child.right = root
    left_child.height = 1 + max(get_height(left_child.left), get_height(root))

    return left_child

def left_rotate(root):
    right_child = root.right

    root.right = right_child.left
    root.height = 1 + max(get_height(root.left), get_height(root.right))

    right_child.left = root
    right_child.height = 1 + max(get_height(root), get_height(right_child.right))

    return right_child

def insert_node(root, key):
    if root is None:
        return TreeNode(key)

    if root.key > key:
        root.left = insert_node(root.left, key)
    elif root.key < key:
        root.right = insert_node(root.right, key)

    root.height = 1 + max(get_height(root.left), get_height(root.right))
    balance = get_balance(root)

    if balance > 1:
        if get_balance(root.left) >= 0:
            return right_rotate(root)
        else:
            root.left = left_rotate(root.left)
            return right_rotate(root)
    elif balance < -1:
        if get_balance(root.right) <= 0:
            return left_rotate(root)
        else:
            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root

def level_order(root):
    if root is None:
        return []
    queue = [root]
    result = [root.key]
    while queue:
        node = queue.pop(0)
        if node.left:
            queue.append(node.left)
            result.append(node.left.key)
        if node.right:
            queue.append(node.right)
            result.append(node.right.key)
    return result

def lca(root, p, q):
    if root.key > q:
        return lca(root.left, p, q)
    elif root.key < p:
        return lca(root.right, p, q)
    else:
        return root

def length_path(root, key):
    if root.key == key:
        return 0
    if root.key > key:
        return 1 + length_path(root.left, key)
    else:
        return 1 + length_path(root.right, key)

if __name__ == '__main__':
    n = int(input())
    values = list(map(int, input().strip().split()))
    p, q = map(int, input().strip().split())
    tree = None
    for val in values:
        tree = insert_node(tree, val)
    print(level_order(tree))

    if p > q:
        p, q = q, p
    lca_p_q = lca(tree, p, q)
    print(length_path(lca_p_q, p) + length_path(lca_p_q, q))