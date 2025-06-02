class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def construct_tree(level_order: list):
    list_node = []
    for val in level_order:
        if val:
            list_node.append(TreeNode(val))
        else:
            list_node.append(None)

    def link_tree(i):
        if list_node[i] is None:
            return

        if 2 * i + 2 < len(list_node):

            list_node[i].left = list_node[2 * i + 1]
            list_node[i].right = list_node[2 * i + 2]

            link_tree(2 * i + 1)
            link_tree(2 * i + 2)

        elif 2 * i + 1 < len(list_node):

            list_node[i].left = list_node[2 * i + 1]
            link_tree(2 * i + 1)

    link_tree(0)

    return list_node[0]

def lnr(root):
    if root is None:
        return []
    return lnr(root.left) + [root.key] + lnr(root.right)

def is_ascending(arr):
    for i in range(len(arr) - 1):
        if arr[i] >= arr[i + 1]:
            return False
    return True

if __name__ == '__main__':
    array = input().strip().split()
    level_order = []
    for i in range(len(array)):
        if array[i] == 'null':
            level_order.append(None)
        else:
            level_order.append(int(array[i]))

    tree = construct_tree(level_order)
    print(lnr(tree))
    if is_ascending(lnr(tree)):
        print('Yes')
    else:
        print('No')