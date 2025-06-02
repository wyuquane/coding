class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def pre_order_traversal(self):
        print(self.data, end=', ')
        if self.left:
            self.left.pre_order_traversal()
        if self.right:
            self.right.pre_order_traversal()

    def in_order_traversal(self):
        if self.left:
            self.left.in_order_traversal()
        print(self.data, end=', ')
        if self.right:
            self.right.in_order_traversal()

    def post_order_traversal(self):
        if self.left:
            self.left.post_order_traversal()
        if self.right:
            self.right.post_order_traversal()
        print(self.data, end=', ')

# if __name__ == "__main__":
#     root = TreeNode('R')
#     nodeA = TreeNode('A')
#     nodeB = TreeNode('B')
#     nodeC = TreeNode('C')
#     nodeD = TreeNode('D')
#     nodeE = TreeNode('E')
#     nodeF = TreeNode('F')
#     nodeG = TreeNode('G')
#
#     root.left = nodeA
#     root.right = nodeB
#
#     nodeA.left = nodeC
#     nodeA.right = nodeD
#
#     nodeB.left = nodeE
#     nodeB.right = nodeF
#
#     nodeF.left = nodeG
#
#     root.pre_order_traversal()
#     print()
#     root.in_order_traversal()
#     print()
#     root.post_order_traversal()

if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    root.pre_order_traversal()
    root.post_order_traversal()
