import operator


class BinaryTree:
    def __init__(self, root_obj):
        self.parent = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def get_root_value(self):
        return self.parent

    def set_root_value(self, obj):
        self.parent = obj

    def post_order(self):
        pass


def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = list()
    eTree = BinaryTree('')
    pStack.append(eTree)
    currentTree = eTree

    for i in fplist:
        if i == '(':
            currentTree.insert_left('')
            pStack.append(currentTree)
            currentTree = currentTree.get_left_child()
        elif i.isdigit():
            currentTree.set_root_value(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.set_root_value(i)
            currentTree.insert_right('')
            pStack.append(currentTree)
            currentTree = currentTree.get_right_child()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree


def evaluate(parseTree):
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

    left_child = parseTree.get_left_child()
    right_child = parseTree.get_right_child()

    if left_child and right_child:
        fn = opers[parseTree.get_root_value()]
        return fn(evaluate(left_child), evaluate(right_child))
    else:
        return parseTree.get_root_value()


if __name__ == '__main__':
    src1 = '( ( 10 + 5 ) * 3 )'
    src2 = '( 3 + ( 4 * 5 ) )'
    pt1 = buildParseTree(src1)
    pt2 = buildParseTree(src2)
    assert evaluate(pt1) == 45
    assert evaluate(pt2) == 23
