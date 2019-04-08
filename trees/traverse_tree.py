from trees.binary_tree import BinaryTree


def preorder(tree: BinaryTree):
    """
    Aka 'forward order'.
    In a preorder traversal, we visit the root node first,
    then recursively do a preorder traversal of the left
    subtree, followed by a recursive preorder traversal
    of the right subtree.
    """
    if tree:
        print(tree.get_root_value())
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())


def inorder(tree: BinaryTree):
    """
    Aka 'symmetric order'.
    In an inorder traversal, we recursively do an inorder
    traversal on the left subtree, visit the root node,
    and finally do a recursive inorder traversal of the
    right subtree.
    """
    if tree:
        inorder(tree.get_left_child())
        print(tree.get_root_value())
        inorder(tree.get_right_child())


def postorder(tree: BinaryTree):
    """
    Aka 'backward order'.
    In a postorder traversal, we recursively do a postorder
    traversal of the left subtree and the right subtree
    followed by a visit to the root node.
    """
    if tree:
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        print(tree.get_root_value())


if __name__ == '__main__':
    bt = BinaryTree('0')
    bt.insert_left('1')
    bt.insert_right('2')
    left = bt.get_left_child()
    right = bt.get_right_child()
    left.insert_left('1.1')
    left.insert_right('1.2')
    right.insert_left('2.1')
    right.insert_right('2.2')

    """ Tree representation:
         ___0___
        /       \
       1         2
     /   \      /  \
    1.1  1.2  2.1  2.2
    """

    print("Preorder traversal:")
    preorder(bt)
    print("-" * 20)

    print("Inorder traversal:")
    inorder(bt)
    print("-" * 20)

    print("Postorder traversal:")
    postorder(bt)
    print("-" * 20)
