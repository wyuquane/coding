class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return f'tree node: {self.data}'

def in_order_traversal(node):
    if node is None:
        return
    in_order_traversal(node.left)
    print(node.data, end=", ")
    in_order_traversal(node.right)

def nlr(node):
    if node is None:
        return
    print(node.data, end=', ')
    nlr(node.left)
    nlr(node.right)


def search_value(node: TreeNode, value):
    if node is None:
        return None
    elif node.data == value:
        return node
    elif node.data < value:
        return search_value(node.right, value)
    else:
        return search_value(node.left, value)

def insert_value(node: TreeNode | None, value):
    if value > node.data:
        if node.right is None:
            leaf = TreeNode(value)
            node.right = leaf
        else:
            insert_value(node.right, value)
    elif value < node.data:
        if node.left is None:
            leaf = TreeNode(value)
            node.left = leaf
        else:
            insert_value(node.left, value)
    else:
        return

def lowest_value(node: TreeNode):
    cur = node
    while cur.left:
        cur = cur.left
    return cur

def delete(node, data):
    if node is None:
        return None

    if data < node.data:
        node.left = delete(node.left, data)
    elif data > node.data:
        node.right = delete(node.right, data)
    else:
        # Node with only one child or no child
        if node.left is None:
            temp = node.right
            return temp
        elif node.right is None:
            temp = node.left
            return temp

        # Node with two children, get the in-order successor
        node.data = lowest_value(node.right).data
        node.right = delete(node.right, node.data)

    return node




if __name__ == '__main__':
    root = TreeNode(1)
    value = [1, 4, 3, 8, 2, 9]
    for num in value:
        insert_value(root, num)
    nlr(root)


