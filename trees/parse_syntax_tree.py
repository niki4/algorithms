import operator

from trees.binary_tree import BinaryTree


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
